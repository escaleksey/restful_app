import datetime
from flask import jsonify
from flask_restful import abort, reqparse, Resource
from data import db_session
from data.db_session import create_session
from data.jobs import Jobs


def abort_if_job_not_found(job_id):
    session = create_session()
    job = session.query(Jobs).get(job_id)
    if not job:
        abort(404, message=f"job {job_id} not found")


class JobResource(Resource):
    def get(self, job_id):
        abort_if_job_not_found(job_id)
        session = create_session()
        job = session.query(Jobs).get(job_id)
        return jsonify({'jobs': job.to_dict(
            only=('team_leader', 'job', 'work_size', 'collaborators', 'end_date', 'start_date', 'is_finished'))})

    def delete(self, job_id):
        abort_if_job_not_found(job_id)
        session = create_session()
        job = session.query(Jobs).get(job_id)
        session.delete(job)
        session.commit()
        return jsonify({'success': 'OK'})
    

class JobsListResource(Resource):
    def get(self):
        session = db_session.create_session()
        jobs = session.query(Jobs).all()
        return jsonify({'jobs': [item.to_dict(
            only=('team_leader', 'job', 'work_size',
                  'collaborators', 'end_date', 'start_date', 'is_finished')) for item in jobs]})

    def post(self):
        keys = ['team_leader', 'job', 'work_size', 'collaborators', 'end_date', 'start_date', 'is_finished']

        args = parser.parse_args()
        session = db_session.create_session()
        job = Jobs(
            team_leader=args['team_leader'],
            job=args['job'],
            work_size=args['work_size'],
            collaborators=args['collaborators'],
            start_date=datetime.datetime.now(),
            end_date=datetime.datetime.now(),
            is_finished=args['is_finished']
        )
        session.add(job)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('job', required=True)
parser.add_argument('work_size', required=True, type=int)
parser.add_argument('collaborators', required=True)
parser.add_argument('is_finished', required=True, type=bool)
parser.add_argument('team_leader', required=True, type=int)
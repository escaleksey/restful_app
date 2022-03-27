from flask import Blueprint, jsonify, request
from data.db_session import create_session
from data.jobs import Jobs
from datetime import datetime


blueprint = Blueprint(
    'jobs',
    __name__,
    template_folder='templates',
    url_prefix="/api/jobs"
)


@blueprint.route('/')
def get_job():
    db_sess = create_session()
    jobs = db_sess.query(Jobs).all()
    return jsonify(
        {
            'job':
                [item.to_dict(only=('team_leader',
                                    'job',
                                    'work_size',
                                    'collaborators',
                                    'end_date',
                                    'start_date',
                                    'is_finished'))
                 for item in jobs]
        }
    )


@blueprint.route('/<int:job_id>', methods=['GET'])
def get_one_job(job_id):
    db_sess = create_session()
    job = db_sess.query(Jobs).get(job_id)
    if not job:
        return jsonify({'error': 'Not found'})
    return jsonify(
        {
            'job': job.to_dict(only=('team_leader',
                                     'job',
                                     'work_size',
                                     'collaborators',
                                     'end_date',
                                     'start_date',
                                     'is_finished'))
        }
    )


@blueprint.route('/', methods=['POST'])
def create_job():
    keys = ['id', 'team_leader',
            'job',
            'work_size',
            'collaborators',
            'end_date',
            'start_date',
            'is_finished']
    if not request.json:
        return jsonify({'error': 'Empty request'})
    elif not all(key in request.json for key in keys
                 ):
        return jsonify({'error': 'Bad request'})
    db_sess = create_session()
    exist_job = db_sess.query(Jobs).get(request.json['id'])
    if exist_job:
        return jsonify({'error': ' Id already exists'})
    data = {key: request.json[key] for key in keys}
    data['start_date'] = datetime.now()
    data['end_date'] = datetime.now()
    job = Jobs(**data)
    db_sess.add(job)
    db_sess.commit()
    return jsonify({'success': 'OK'})


@blueprint.route('/<int:job_id>', methods=['DELETE'])
def delete_job(job_id):
    db_sess = create_session()
    job = db_sess.query(Jobs).get(job_id)
    if job:
        db_sess.delete(job)
        db_sess.commit()
        db_sess.close()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found ID'})


@blueprint.route('/<int:job_id>', methods=["PUT"])
def put_job(job_id):
    keys = ['team_leader',
            'job',
            'work_size',
            'collaborators',
            'end_date',
            'start_date',
            'is_finished']
    db_sess = create_session()
    job = db_sess.query(Jobs).get(job_id)
    if job:
        if not request.json:
            return jsonify({'error': 'Empty request'})
        elif not any(key in request.json for key in keys):
            return jsonify({'error': 'Bad request'})

        for key, new_value in request.json.items():
            setattr(job, key, new_value)

        db_sess.commit()
        return jsonify({'success': 'OK'})
    else:
        return jsonify({'error': 'Not found'})

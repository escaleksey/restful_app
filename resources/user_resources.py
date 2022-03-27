import datetime

from flask import jsonify
from flask_restful import abort, reqparse, Resource

from data import db_session
from data.db_session import create_session
from data.users import User


def abort_if_user_not_found(user_id):
    session = create_session()
    user = session.query(User).get(user_id)
    if not user:
        abort(404, message=f"User {user_id} not found")


class UserResource(Resource):
    def get(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        return jsonify({'user': user.to_dict(
            only=('name', 'about', 'email', 'created_date'))})

    def delete(self, user_id):
        abort_if_user_not_found(user_id)
        session = create_session()
        user = session.query(User).get(user_id)
        session.delete(user)
        session.commit()
        return jsonify({'success': 'OK'})


class UserListResource(Resource):
    def get(self):
        session = db_session.create_session()
        user = session.query(User).all()
        return jsonify({'user': [item.to_dict(
            only=('name', 'about', 'email', 'created_date')) for item in user]})

    def post(self):
        keys = ['name', 'about', 'email', 'created_date', 'hashed_password']

        args = parser.parse_args()
        session = db_session.create_session()
        emails = session.query(User.email).filter(User.email == args['email']).first()
        if emails:
            return jsonify({'error': 'this email is already in use'})
        user = User(
            name=args['name'],
            about=args['about'],
            email=args['email'],
            created_date=datetime.datetime.now()
        )
        user.set_password(args['hashed_password'])
        session.add(user)
        session.commit()
        return jsonify({'success': 'OK'})


parser = reqparse.RequestParser()
parser.add_argument('name', required=True)
parser.add_argument('about', required=True)
parser.add_argument('hashed_password', required=True)
parser.add_argument('email', required=True)
parser.add_argument('created_date', required=True, type=bool)
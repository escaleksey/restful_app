from flask import Flask, jsonify
from data.db_session import global_init
from routes import jobs_blueprint, news_blueprint
from flask import make_response
from resources import NewsResource, NewsListResource, UserResource, UserListResource, JobResource, JobsListResource
from flask_restful import reqparse, abort, Api, Resource


from resources import NewsListResource, NewsResource


app = Flask(__name__)
api = Api(app)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


def main():
    global_init("db/blogs.db")

    app.register_blueprint(jobs_blueprint)
    app.register_blueprint(news_blueprint)
    api.add_resource(NewsResource, "/api/v2/news/<int:news_id>")
    api.add_resource(NewsListResource, "/api/v2/news")
    api.add_resource(UserResource, "/api/v2/user/<int:user_id>")
    api.add_resource(UserListResource, "/api/v2/user")
    api.add_resource(JobResource, "/api/v2/job/<int:job_id>")
    api.add_resource(JobsListResource, "/api/v2/job")
    app.run()


if __name__ == '__main__':
    main()


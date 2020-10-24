import os
import random

from flask import Flask, abort, jsonify, request
from flask.views import MethodView
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

from flaskr.controllers import categories_api, questions_api, quizzes_api
from flaskr.serializers import ma
from flaskr.utils import generic_error_message
from models import db


def create_app(config_path="flaskr.config.local"):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_path)

    db.init_app(app)
    CORS(app)
    ma.init_app(app)

    @app.after_request
    def after_request(response):
        response.headers.add("Access-Control-Allow-Origin", "*")
        response.headers.add(
            "Access-Control-Allow-Headers", "Content-Type,Authorization"
        )
        response.headers.add(
            "Access-Control-Allow-Methods", "GET,PUT,PATCH,POST,DELETE"
        )
        return response

    register_error_handlers(app)
    register_routes(app)
    return app


def register_routes(app):
    app.register_blueprint(questions_api, url_prefix="/api/v1")
    app.register_blueprint(categories_api, url_prefix="/api/v1")
    app.register_blueprint(quizzes_api, url_prefix="/api/v1")


def register_error_handlers(app):
    @app.errorhandler(400)
    def handle_400(e):
        # Bad Request
        return generic_error_message(400, "bad request, invalid request message")

    @app.errorhandler(404)
    def handle_404(e):
        # Not Found
        return generic_error_message(
            404, "not found, the requested URL was not found on the server"
        )

    @app.errorhandler(422)
    def handle_422(e):
        # Unprocessable Entity
        return generic_error_message(
            422, "unprocessable entity, data sent is incomplete/incorrect"
        )

    @app.errorhandler(500)
    def handle_500(e):
        # Server Error
        return generic_error_message(
            500, "server error, we cannot process your request right now"
        )

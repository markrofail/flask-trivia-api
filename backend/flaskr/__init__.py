import os
import random

from flask import Flask, abort, jsonify, request
from flask.views import MethodView
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from models import Category, Question, setup_db

from flaskr.controllers import categories_api, questions_api
from flaskr.utils import generic_error_message

from flaskr.serializers import ma

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

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


  '''
  @TODO: 
  Create an endpoint to handle GET requests for questions, 
  including pagination (every 10 questions). 
  This endpoint should return a list of questions, 
  number of total questions, current category, categories. 

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions. 
  '''

  '''
  @TODO: 
  Create an endpoint to DELETE question using a question ID. 

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page. 
  '''

  '''
  @TODO: 
  Create an endpoint to POST a new question, 
  which will require the question and answer text, 
  category, and difficulty score.

  TEST: When you submit a question on the "Add" tab, 
  the form will clear and the question will appear at the end of the last page
  of the questions list in the "List" tab.  
  '''

  '''
  @TODO: 
  Create a POST endpoint to get questions based on a search term. 
  It should return any questions for whom the search term 
  is a substring of the question. 

  TEST: Search by any phrase. The questions list will update to include 
  only question that include that string within their question. 
  Try using the word "title" to start. 
  '''

  '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the "List" tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''


  '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the "Play" tab, after a user selects "All" or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

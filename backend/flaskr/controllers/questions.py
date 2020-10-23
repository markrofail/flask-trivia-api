from flask import Blueprint, abort, jsonify, request
from flaskr.serializers import question_schema
from flaskr.services.categories import get_all_categories, get_category
from flaskr.services.questions import (create_question, get_all_questions,
                                       get_question, search_question_by_text)
from marshmallow import ValidationError
from models import Category, Question

questions_api = Blueprint("questions", "")


@questions_api.route("/categories/<category_id>/questions/")
def get_question_by_category(category_id):
    current_category = get_category(category_id, return_json=True)
    categories = get_all_categories(return_json=True)

    page = request.args.get("page", 1, type=int)
    questions = get_all_questions(category_id, page, return_json=True)

    return jsonify(
        dict(
            current_category=current_category,
            questions=questions,
            question_count=len(questions),
            categories=categories,
        )
    )


@questions_api.route("/questions/<question_id>", methods=["GET"])
def get_question_detail(question_id):
    question = get_question(question_id, return_json=True)
    return jsonify(dict(question=question, success=True))


@questions_api.route("/questions", methods=["POST"])
def add_question():
    json_data = request.get_json()
    if not json_data:
        abort(400)

    try:
        data = question_schema.load(json_data)
    except ValidationError as err:
        abort(422)

    question = create_question(data)
    return jsonify(question=question_schema.dump(question), success=True)


@questions_api.route("/questions/<question_id>", methods=["DELETE"])
def delete_question_detail(question_id):
    question = get_question(question_id)
    question.delete()

    return jsonify(dict(question_id=question_id, success=True))


@questions_api.route("/questions/search", methods=["POST"])
def search_question():
    search_query = request.json.get("query", None)
    if not search_query:
        abort(422)

    questions = search_question_by_text(search_query, return_json=True)
    return jsonify(
        dict(questions=questions, question_count=len(questions), success=True)
    )

from flask import jsonify, request, Blueprint

from models import Question, Category
from flaskr.services.categories import get_all_categories, get_category
from flaskr.services.questions import get_all_questions, get_question

questions_api = Blueprint('questions', '')


@questions_api.route("/categories/<category_id>/questions/")
def get_question_by_category(category_id):
    current_category = get_category(category_id, return_json=True)
    categories = get_all_categories(return_json=True)

    page = request.args.get('page', 1, type=int)
    questions = get_all_questions(category_id, page, return_json=True)

    return jsonify(
        dict(
            current_category=current_category,
            questions=questions,
            question_count=len(questions),
            categories=categories
        )
    )


@questions_api.route("/questions/<question_id>", methods=['GET'])
def get_question_detail(question_id):
    question = get_question(question_id, return_json=True)
    return jsonify(dict(question=question, success=True))


@questions_api.route("/questions/<question_id>", methods=['DELETE'])
def delete_question_detail(question_id):
    question = get_question(question_id)
    question.delete()

    return jsonify(dict(question_id=question_id, success=True))

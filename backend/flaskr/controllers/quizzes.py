from flask import Blueprint, jsonify, request

from flaskr.services.quizzes import play_quiz_turn

quizzes_api = Blueprint("quizzes", "")


@quizzes_api.route("/quizzes/play", methods=["POST"])
def play_quiz():
    json_data = request.get_json()

    previous_questions = json_data.get("previous_questions", [])
    category_id = json_data.get("category_id", 0)

    if category_id == 0:
        category_id = None

    next_question = None
    if len(previous_questions) < 5:
        next_question = play_quiz_turn(
            category_id=category_id,
            previous_questions=previous_questions,
            return_json=True,
        )
    return jsonify(question=next_question)

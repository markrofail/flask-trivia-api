import random

from .questions import get_all_questions


def play_quiz_turn(category_id, previous_questions, return_json=False):
    questions = get_all_questions(category_id=category_id)
    questions = list(filter(lambda q: q.id not in previous_questions, questions))
    if not questions:
        return None

    question = random.choice(questions)

    if return_json:
        question = question.format(details=True)
    return question

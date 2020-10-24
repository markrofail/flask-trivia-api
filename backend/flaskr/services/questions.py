from models import Question, db, func

QUESTIONS_PER_PAGE = 10


def get_all_questions(category_id=None, page=None, return_json=False):
    queryset = Question.query

    if category_id:
        queryset = queryset.filter_by(category_id=category_id)

    if page:
        questions = queryset.paginate(page, QUESTIONS_PER_PAGE, False).items
    else:
        questions = queryset.all()

    if return_json:
        questions = [q.format(details=True) for q in questions]
    return questions


def get_question(question_id, return_json=False):
    question = Question.query.get_or_404(question_id)

    if return_json:
        question = question.format(details=True)
    return question


def search_question_by_text(search_query, return_json=False):
    questions = Question.query.filter(
        Question.question.ilike(f"%{search_query}%")
    ).all()

    if return_json:
        questions = [q.format() for q in questions]
    return questions


def create_question(data):
    question = Question(**data)
    question.insert()
    return question


def get_total_question_count():
    return db.session.query(func.count(Question.id)).scalar()

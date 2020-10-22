from models import Question

QUESTIONS_PER_PAGE = 10

def get_all_questions(category_id, page=1, return_json=False):
    questions = (
        Question.query
        .filter_by(category=category_id)
        .paginate(page, QUESTIONS_PER_PAGE, False)
        .items
    )
    
    if return_json:
        questions=[q.format() for q in questions]
    return questions

def get_question(question_id, return_json=False):
    question = Question.query.get_or_404(question_id)

    if return_json:
        question=question.format(detail=True)
    return question

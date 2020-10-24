import json
import os
import unittest

from flask import url_for
from flask_fixtures import FixturesMixin
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import Category, Question, db
from pprint import pprint


class TriviaTestCase(unittest.TestCase, FixturesMixin):
    """This class represents the trivia test case"""

    app = create_app("flaskr.config.test")
    client = app.test_client()
    db = db

    fixtures = ['trivia.json']

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()


class CategoriesApiTestCase(TriviaTestCase):

    def test_api_list_categories(self):
        """Categories List: list all available categories"""
        response = self.client.get(url_for('categories.list_categories'))
        self.assertEqual(len(response.json), 6)

class QuestionsApiTestCase(TriviaTestCase):

    def test_api_list_all_questions(self):
        """Question List ALL: list all available questions"""
        response = self.client.get(url_for('questions.get_all_question'))
        json_data = response.json

        self.assertEqual(len(json_data['questions']), 10)
        self.assertEqual(json_data['total_questions'], 19)

        self.assertEqual(len(json_data['categories']), 6)
        self.assertEqual(json_data['current_category'], None)

    def test_api_list_all_questions_page2(self):
        """Question List ALL paginated: list all available questions in page 2"""
        response = self.client.get(url_for('questions.get_all_question', page=2))
        json_data = response.json

        self.assertEqual(len(json_data['questions']), 9)
        self.assertEqual(json_data['total_questions'], 19)

        self.assertEqual(len(json_data['categories']), 6)
        self.assertEqual(json_data['current_category'], None)

    def test_api_list_questions_bycategory(self):
        """Question List ByCategory: list all available questions in a category"""
        response = self.client.get(url_for('questions.get_question_by_category', category_id=1))
        json_data = response.json

        self.assertEqual(len(json_data['questions']), 3)
        self.assertEqual(json_data['total_questions'], 19)

        self.assertEqual(len(json_data['categories']), 6)
        self.assertEqual(json_data['current_category'], {'id': 1, 'type': 'Science'})

    def test_api_list_questions_bycategory_alt(self):
        """Question List ByCategory (alternative): list all available questions in a category"""
        payload = dict(category_id=1)
        response = self.client.post(url_for('questions.get_question_by_category_'), json=payload)
        json_data = response.json

        self.assertEqual(len(json_data), 3)


    def test_api_detail_question(self):
        """Question Detail: get details about one question"""
        payload = dict(category_id=1)
        response = self.client.get(url_for('questions.get_question_detail', question_id=2))
        json_data = response.json['question']

        self.assertEqual(json_data['answer'], "Apollo 13")
        self.assertEqual(json_data['difficulty'], 4)
        self.assertEqual(json_data['category'], 5)

    def test_api_add_question(self):
        """Question Create: create a question"""
        payload = dict(
            category_id=1,
            answer="Some Answer",
            question="Some Question?",
            difficulty=1,
        )
        response = self.client.post(url_for('questions.add_question'), json=payload)
        json_data = response.json['question']

        self.assertEqual(json_data['answer'], payload['answer'])
        self.assertEqual(json_data['difficulty'], payload['difficulty'])
        self.assertEqual(json_data['category_id'], payload['category_id'])

    def test_api_add_question_invalid_category_id(self):
        """Question Create: create a question with invalid category id"""
        payload = dict(
            category_id=10,
            answer="Some Answer",
            question="Some Question?",
            difficulty=1,
        )
        response = self.client.post(url_for('questions.add_question'), json=payload)
        json_data = response.json

        self.assertEqual(response.status_code, 422)
        self.assertEqual(json_data['success'], False)

    def test_api_add_question_invalid_difficulty(self):
        """Question Create: create a question with invalid difficulty"""
        payload = dict(
            category_id=1,
            answer="Some Answer",
            question="Some Question?",
            difficulty=10,
        )
        response = self.client.post(url_for('questions.add_question'), json=payload)
        json_data = response.json

        self.assertEqual(response.status_code, 422)
        self.assertEqual(json_data['success'], False)

    def test_api_delete_question(self):
        """Question Delete: delete a question"""
        response = self.client.delete(url_for('questions.delete_question_detail', question_id=2))
        json_data = response.json

        self.assertEqual(json_data['question_id'], '2')

    def test_api_search_question(self):
        """Question Search: search for question by text"""
        payload=dict(query="what")
        response = self.client.post(url_for('questions.search_question'), json=payload)
        json_data = response.json

        self.assertEqual(json_data['question_count'], 8)

class QuizzesApiTestCase(TriviaTestCase):

    def test_api_play_quiz(self):
        """Quiz Turn: paly a quiz turn"""
        payload=dict(previous_questions=[])

        response = self.client.post(url_for('quizzes.play_quiz'), json=payload)
        json_data = response.json['question']

        self.assertIsNotNone(json_data['question'])
        self.assertIsNotNone(json_data['category'])
        self.assertIsNotNone(json_data['difficulty'])
        self.assertIsNotNone(json_data['answer'])

    def test_api_play_quiz_end(self):
        """Quiz Turn: end a quiz turn"""

        payload=dict(previous_questions=[10, 11], category_id=6)
        response = self.client.post(url_for('quizzes.play_quiz'), json=payload)
        json_data = response.json

        self.assertIsNone(json_data['question'])

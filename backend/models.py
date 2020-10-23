import json
import os

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, ForeignKey, Integer, String, create_engine
from sqlalchemy.orm import relationship

database_name = "trivia"
database_path = "postgres://{}@{}/{}".format(
    "postgres", "localhost:5432", database_name
)

db = SQLAlchemy()


def setup_db(app, database_path=database_path):
    """
    setup_db(app)
        binds a flask application and a SQLAlchemy service
    """
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()


class Category(db.Model):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True)
    type = Column(String)

    questions = relationship("Question", back_populates="category")

    def __init__(self, type):
        self.type = type

    def format(self):
        return {"id": self.id, "type": self.type}


class Question(db.Model):
    __tablename__ = "questions"

    id = Column(Integer, primary_key=True)
    question = Column(String)
    answer = Column(String)
    difficulty = Column(Integer)

    category_id = Column(Integer, ForeignKey("categories.id"))
    category = relationship(Category, back_populates="questions")

    def __init__(self, question, answer, category, difficulty):
        self.question = question
        self.answer = answer
        self.category = category
        self.difficulty = difficulty

    def insert(self):
        db.session.add(self)
        db.session.commit()

    def update(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def format(self, details=False):
        payload = {
            "id": self.id,
            "question": self.question,
        }

        if details:
            payload.update(
                {
                    "answer": self.answer,
                    "category": self.category,
                    "difficulty": self.difficulty,
                }
            )
        return payload

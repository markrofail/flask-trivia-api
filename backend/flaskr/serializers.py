from flask_marshmallow import Marshmallow
from marshmallow import ValidationError, validates

from models import Category, Question

ma = Marshmallow()


class CategorySchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Category
        include_fk = True


class QuestionSchema(ma.SQLAlchemyAutoSchema):
    @validates("category_id")
    def category_exists(self, value):
        category_exists = Category.query.filter_by(id=value).count() >= 1
        if not category_exists:
            raise ValidationError("no matching category found")

    @validates("difficulty")
    def difficulty_within_range(self, value):
        if not 1 <= value <= 5:
            raise ValidationError("difficulty not within range")

    class Meta:
        model = Question
        include_fk = True


question_schema = QuestionSchema()

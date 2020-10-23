from flask_marshmallow import Marshmallow
from marshmallow import Schema, ValidationError, fields, validates
from models import Category, Question

ma = Marshmallow()

class CategorySchema(ma.SQLAlchemyAutoSchema):

    class Meta:
        model = Category
        include_fk = True

class QuestionSchema(ma.SQLAlchemyAutoSchema):

    @validates('category_id')
    def category_exists(self, value):
        """'value' is the datetime parsed from time_created by marshmallow"""

        category_exists = Category.query.filter_by(id=value).count() >= 1
        if not category_exists:
            raise ValidationError("no matching category found")
        # if the function doesn't raise an error, the check is considered passed

    class Meta:
        model = Question
        include_fk = True

question_schema = QuestionSchema()

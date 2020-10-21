from flask import jsonify, views

from models import Category

class CategoryAPI(views.MethodView):

    def get(self):
        categories = Category.query.all()
        return jsonify([category.format() for category in categories])


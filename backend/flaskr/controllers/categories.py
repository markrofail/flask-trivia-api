from flask import jsonify, views

from flaskr.services.categories import get_all_categories

class CategoryAPI(views.MethodView):

    def get(self):
        categories = get_all_categories(return_json=True)
        return jsonify(categories)

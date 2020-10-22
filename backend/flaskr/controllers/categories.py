from flask import jsonify, views, Blueprint

from flaskr.services.categories import get_all_categories

categories_api = Blueprint('categories', '')

class CategoryAPI(views.MethodView):

    def get(self):
        categories = get_all_categories(return_json=True)
        return jsonify(categories)

categories_api.add_url_rule('/categories', view_func=CategoryAPI.as_view('categories'))

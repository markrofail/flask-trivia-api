from flask import Blueprint, jsonify, views
from flaskr.services.categories import get_all_categories

categories_api = Blueprint("categories", "")


@categories_api.route('/categories')
def list_categories(self):
    categories = get_all_categories(return_json=True)
    return jsonify(categories)

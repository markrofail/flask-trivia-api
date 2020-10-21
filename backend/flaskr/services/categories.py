from models import Category

def get_all_categories(return_json=False):
    categories = Category.query.all()

    if return_json:
        categories=[c.format() for c in categories]
    return categories

def get_category(category_id, return_json=False):
    category = Category.query.get_or_404(category_id)

    if return_json:
        category=category.format()
    return category

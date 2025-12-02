from . import orders, order_details, resources, dishes, payment_info, customers, promotions, rating_reviews, recipes

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    dishes.Base.metadata.create_all(engine)
    payment_info.Base.metadata.create_all(engine)
    customers.Base.metadata.create_all(engine)
    promotions.Base.metadata.create_all(engine)
    rating_reviews.Base.metadata.create_all(engine)
    recipes.Base.metadata.create_all(engine)



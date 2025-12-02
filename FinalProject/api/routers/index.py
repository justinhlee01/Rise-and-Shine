from . import orders, order_details, dishes, promotions, customers, resources, rating_reviews, payment_info


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(dishes.router)
    app.include_router(promotions.router)
    app.include_router(customers.router)
    app.include_router(resources.router)
    app.include_router(rating_reviews.router)
    app.include_router(payment_info.router)



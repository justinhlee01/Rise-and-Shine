from . import orders, order_details, dishes, promotions


def load_routes(app):
    app.include_router(orders.router)
    app.include_router(order_details.router)
    app.include_router(dishes.router)
    app.include_router(promotions.router)

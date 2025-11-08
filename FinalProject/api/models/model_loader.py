from . import orders, order_details, resources, dishes, payment_info

from ..dependencies.database import engine


def index():
    orders.Base.metadata.create_all(engine)
    order_details.Base.metadata.create_all(engine)
    resources.Base.metadata.create_all(engine)
    dishes.Base.metadate_create_all(engine)
    payment_info.Base.metadata.create_all(engine)

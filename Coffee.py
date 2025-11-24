# coffee.py
class Coffee:
    all = []

    def __init__(self, name):
        self.name = name
        Coffee.all.append(self)

    def orders(self):
        from Order import Order
        return [order for order in Order.all if order.coffee == self]

    def customers(self):
        from Order import Order
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        orders = self.orders()
        if not orders:
            return None
        return sum(order.price for order in orders) / len(orders)

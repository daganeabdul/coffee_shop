
class Customer:
    all = []

    def __init__(self, name):
        self.name = name
        Customer.all.append(self)

    def orders(self):
        from Order import Order  
        return [order for order in Order.all if order.customer == self]

    def coffees(self):
        from Order import Order
        return list({order.coffee for order in self.orders()})

    def create_order(self, coffee, price):
        from Order import Order
        return Order(self, coffee, price)

if __name__ == "__main__":
    from Customer import Customer
    from Coffee import Coffee
    from Order import Order

    c1 = Customer("Ali")
    c2 = Customer("Ayan")

    latte = Coffee("Latte")

    c1.create_order(latte, 5)
    c2.create_order(latte, 6)


    print("All orders:")
    for order in Order.all:
        print(f"{order.customer.name} ordered {order.coffee.name} for ${order.price}")

    print("Ali's coffees:", [coffee.name for coffee in c1.coffees()])
    print("Total Latte orders:", latte.num_orders())

# exp - operator overloading

class PizzOrder:
    def __init__(self,x):
        self.x = x

    def __add__(self, other):
        total_orders = self.x + other.x
        return PizzOrder(total_orders)

    def __str__(self):
        return f"Total Orders {self.x}"


or1 = PizzOrder(10)
ord2 = PizzOrder(3)

tot = or1 + ord2

print(tot)
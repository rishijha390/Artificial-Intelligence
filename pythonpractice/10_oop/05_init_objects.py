class chaiOrder:
    def __init__(self, type_, size):
        self.type = type_
        self.size = size

    def summary(self):
        return f"A {self.size}ml {self.type} chai"
    
order = chaiOrder("Masala", 200)
print(order.summary())

order_two = chaiOrder("Ginger", 220)
print(order_two.summary())
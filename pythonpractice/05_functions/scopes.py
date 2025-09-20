def serve_type():
    chai_type = "masala"
    print(f"Inside function: { chai_type}")


chai_type = "ginger"
serve_type()
print(f"outside function: {chai_type}")


def chai_counter():
    chai_order = "lemon"
    def print_order():
        chai_order = "ginger"
        print("Inner:",chai_order)
    print_order()
    print("outer: ",chai_order)

chai_order = "Tulsi"
chai_counter()
print("Global:",chai_order)
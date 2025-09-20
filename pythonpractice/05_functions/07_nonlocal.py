def update_order():
    chai_type = "Elachi"

    def kitchen():
        nonlocal chai_type
        chai_type = "ginger"
    kitchen()
    print("After kitchen update" , chai_type)

update_order()
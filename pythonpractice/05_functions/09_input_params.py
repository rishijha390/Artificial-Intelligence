# chai = "ginger chai"

# def prepare_chai(order): #parameter
#     print("preparing" , order)

# prepare_chai(chai) #argument
# print(chai)


# chai = [1,2,3]

# def edit_chai(cup):
#     cup[1] = 10

# edit_chai(chai)
# print(chai)


# def make_chai(tea,milk,sugar):
#     print(tea,milk,sugar)

# make_chai("ginger","no","low")
# make_chai(tea = "Green" , sugar = " 1 tea spoon" , milk = "No")



def special_chai(*ingredients , **extras):
    print("Ingredients" , ingredients)
    print("Extras" , extras)

special_chai("Cinamon" , "Cardamon" , sweetener = "Honey" ,foam = "Yes")

def chai_order(order = None):
    if order is None:
        order = []
    print(order)

chai_order()
chai_order()




chai_order = dict(type="Masala tea" , size="large" , sugar= 2)
print(f"Chai order: {chai_order}")

chai_recipe = {}
chai_recipe["base"] = "black tea"
chai_recipe["liquid"] = "milk"
print(f"Recipe base =  {chai_recipe['base']}")
print(f"Recipe {chai_recipe}")
del chai_recipe["liquid"]
print(f"Recipe {chai_recipe}")


chai_order = {"type" : "Ginger Tea" , "size" : "large" , "sugar" : 1}

print(f" order details(keys) : {chai_order.keys()}")
print(f"Order details(values) : {chai_order.values()} ")
print(f"Order details(items) : {chai_order.items()}")

last_item = chai_order.popitem()
print(f"Removed last item: {last_item}")


ingredients = {"chicken" , "Mushroom"}
extra_spices = {"cigrate" , "alcohal"}
ingredients.update(extra_spices)

print(f"Updated chai recipe {ingredients}")

customer_note = chai_order.get("note","No note")
print(f"customer note is: {customer_note}")
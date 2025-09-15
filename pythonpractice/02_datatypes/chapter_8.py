ingredients = ["Water","milk","tea leaves"]
ingredients.append("sugar")
print(f"Ingredients in the tea are - {ingredients}")

ingredients.remove("milk")
print(f"New ingridients for making tea are - {ingredients}")


spice_ingredients = ["cardamon","cinnamon"]

tea_ingredients = ["tea leaves" , " sugar"]

tea_ingredients.extend(spice_ingredients)
print(f"chai : {tea_ingredients}")

tea_ingredients.insert(2,"black tea")
print(f"new ingridients are: {tea_ingredients}")


last_added = tea_ingredients.pop()
print(f"item removed is: {last_added}")
print(f"new ingridients are: {tea_ingredients}")

tea_ingredients.reverse()
print(f"ingridents in reverse order: {tea_ingredients}")

tea_ingredients.sort()
print(f"sorted ingridients are: {tea_ingredients}")

sugar_levels = [1,2,3,4,5]
print(f"maximum sugar level is : {max(sugar_levels)}")
print(f"maximum sugar level is : {min(sugar_levels)}")

# overloading

base_liquid = ["ginger" , "water"]
extra_liquid = ["milk"]
full_liquid_mix = base_liquid + extra_liquid
print(f"Liquid mix: {full_liquid_mix}")

strong_brew = ["ginger", "water"] * 3
print(f"Strong brew: {strong_brew}")

raw_spice_data = bytearray(b"CINNAMON")
raw_spice_data = raw_spice_data.replace(b"CINNA" , b"CARD")
print(f"Bytes: {raw_spice_data}")





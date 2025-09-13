# Integer

black_tea_grams = 14
ginger_grams = 3

total_grams = black_tea_grams + ginger_grams
print(f"Total grams of base tea is: {total_grams}")

remaining_tea = black_tea_grams - ginger_grams
print(f"Total grams of remaining tea is: {remaining_tea}")


milk = 7
serving = 4

per_person_serving = (milk / serving)
print(f"Per person get milk in liter: {per_person_serving}")


tea_bags = 7
no_of_pots = 4

per_pot_tea_bags = (tea_bags // no_of_pots)
print(f"Each pots gets no of tea bags = {per_pot_tea_bags}")

total_cardamon_pods = 10
pods_per_cup = 3 
remaining_pods = total_cardamon_pods % pods_per_cup
print(f"Remaing pods are: {remaining_pods}")

base_flavour_strength = 2
scale_factor = 3
powerful_flavour = base_flavour_strength ** scale_factor
print(f"scaled flavour strength {powerful_flavour}")

total_tea_leaves_harvested = 1_00_00_000
print(f"Total tea leaves are: {total_tea_leaves_harvested}")

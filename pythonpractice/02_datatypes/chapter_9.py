essential_spices = {"ginger", "cardamon", "cinnamon"}
extra_spices = {"cloves","ginger"}

all_spices = essential_spices | extra_spices
print(f"All spices: {all_spices}")

common_spices =  essential_spices & extra_spices
print(f"Common spices are: {common_spices}")

important_spices = essential_spices - extra_spices
print(f"Important spices are: {important_spices}")

print(f"Is cloves in extra spices? {'cloves' in extra_spices}")
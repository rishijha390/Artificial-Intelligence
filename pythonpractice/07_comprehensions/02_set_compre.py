favorite_chai = [
    "Masala chai" , "Green chai" , "Masala chai",
    "Lemon chai" , "Green chai" , "Elaichi chai"
]

unique_chai = {chai for chai in favorite_chai}
print(unique_chai)


recipes = {
    "Masala chai":["ginger" , "cardamon" , "clove"],
    "Elaichi chai":["cardamon" , "milk"],
    "Spicy chai":["ginger" , "black pepper" , "clove"],
}

unique_spices = {spice for ingredients in recipes.values() for spice in ingredients}

print(unique_spices)
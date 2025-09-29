chai_menu = {"masala":40 , "ginger":50}

try:
    chai_menu["elaichi"]
except KeyError:
    print("The key that you are trying to access does not exists")

print("Hello chai code")
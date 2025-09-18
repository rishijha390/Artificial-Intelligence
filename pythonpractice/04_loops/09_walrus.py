# value = 17

# remainder = value % 5
# if remainder:
#     print(f"Not divisible, remainder is {remainder}")


# value = 17

# if (remainder := value % 5):
#     print(f"Not divisiblle ,remainder is {remainder}")

# sizes = ["small","medium","large"]

# if (requested_size := input("Enter the desired size of the chai cup: ")) in sizes:
#     print(f"Serving {requested_size} chai")
# else:
#     print(f"Size is unavailable - {requested_size}")

flavors = ["chocolate" , "strawberry" , "wildberry", "hazle nut"]

print(f"Available flavors are: ", flavors)
while (flavor := input("Enter the desired flavor: ")) not in flavors:
    print(f"Sorry , the requested {flavor} flavor is not available")

print(f"You choose {flavor} haha you know what!")

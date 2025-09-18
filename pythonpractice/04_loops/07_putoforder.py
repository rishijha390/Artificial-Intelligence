flavours = ["Strawberry" , "Chocolate",  "out of stock" , "Discontinued","vanilla"]

for flavor in flavours:
    if flavor == "out of stock":
     continue
    if flavor == "Discontinued":
     break
    print(f"{flavor} item found")

print(f"out side of loop")



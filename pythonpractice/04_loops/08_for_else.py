staffs = [("Rishi" , 17),("Abhishek" , 16) , ("Umakant" , 15)]

for name , age in staffs:
    if age >= 18:
        print(f"{name} is allowed to manage the staff")
        break
else:
    print(f"No one is eligible to manage the staff")
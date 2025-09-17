names = ["Rishi","Doraemon","Abid","Dhoni"]
bills = [50,85,105,60]

for name,amount in zip(names,bills):
    print(f"{name} paid {amount} rupees")
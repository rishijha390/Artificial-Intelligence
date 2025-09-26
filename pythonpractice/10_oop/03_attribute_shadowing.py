class chai:
    temperature = "hot"
    strength = "Strong"


cutting = chai()
print(cutting.temperature)

cutting.temperature = "mild"
cutting.cup = "small"
print("After changing ",cutting.temperature)
print("cup size is  ",cutting.cup)
print("Direct look into the class ", chai.temperature)

del cutting.temperature
del cutting.cup
print(cutting.temperature)
print(cutting.cup)
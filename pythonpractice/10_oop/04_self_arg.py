class chaicup:
    size = 150 #ml

    def describe(self):
        return f"A {self.size}ml chai cup"
    
cup = chaicup()
print(cup.describe())
print(chaicup.describe(cup))

cup_two = chaicup()
cup_two.size = 100 #ml
print(chaicup.describe(cup_two))
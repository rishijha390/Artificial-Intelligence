class chai:
    origin = "India"

print(chai.origin)

chai.is_hot = True
print(chai.is_hot)

#creating obect from class chai

masala = chai()
print(f"Masala {masala.origin}")
print(f"Masala {masala.is_hot}")

masala.is_hot = False

print(f"Class: {chai.is_hot}")
print(f"Masala {masala.is_hot}")

masala.flavor = "Masala"
print(masala.flavor)
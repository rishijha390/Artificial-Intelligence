masala_spices = ("cinnamon","cardamon","cloves")
(spice1,spice2,spice3) = masala_spices

print(f"Main masala spices: {spice1},{spice2},{spice3}")

ginger_ratio , cardamon_ratio = 2,1
print(f"Ratio of G:{ginger_ratio} and C: {cardamon_ratio}")
ginger_ratio ,  cardamon_ratio = cardamon_ratio , ginger_ratio
print(f"Ratio of G:{ginger_ratio} and C: {cardamon_ratio}")


#membership
print(f"is cloves present in masala spices ? {'cloves' in masala_spices}")
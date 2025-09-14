chai_type = "ginger tea"
customer_name = "Rishi"
print(f"Order for {customer_name} :  {chai_type} please!")

chai_description = "aromatic and bold"
print(f"First word {chai_description[:8]}")
print(f"Second word {chai_description[12:]}")

label_text = "doraemon love"
encoded_level = label_text.encode("utf-8")
print(f"Non Encoded Level: {label_text}")
print(f"Encoded Level: {encoded_level}")
decoded_label = encoded_level.decode("utf-8")
print(f"Decoded Level: {decoded_label}")
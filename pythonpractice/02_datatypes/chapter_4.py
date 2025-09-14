is_boiling = True
stri_count = 5
total_events = is_boiling + stri_count #upcasting 
print(f"Total nummbers of events are: {total_events}")

milk_present = "rishi" # no milk
print(f"Milk present ? {bool(milk_present)}")


water_hot = True
tea_added = False

serve_tea = water_hot and tea_added
print(f"Can tea be served: {serve_tea}")
    
device_status = input("Enter the status of the system: ").lower()
temperature = float(input("Enter the temperature: "))
if device_status == "active" and temperature > 35:
    print("High Temperature Alert! ")

else:
    print("Device is Offline")
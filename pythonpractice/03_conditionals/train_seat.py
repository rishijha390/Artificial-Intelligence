seat_type = input("Enter the preference of the seat sleeper/ac/general/luxury:- ").lower()

match seat_type:
    case "sleeper":
        print("Non Ac reserved seat with beds")
    case "ac":
        print("Air conditioned seat with beds")
    case "general":
        print("Non reserved seat")
    case "luxury":
        print("Premium seats with meals and personal attendant")
    case _:
        print("Invalid seat type")
        

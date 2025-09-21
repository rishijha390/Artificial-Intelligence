# def make_chai():
#    # return "Here is you masala chai"
#    print("Here is your masala chai")

# return_value = make_chai()

# print(return_value)



# def idle_chaiwala():
#     pass

# print(idle_chaiwala())

#example of one  value 

# def sold_cups():
#     return 120

# total = sold_cups()
# print(total)



#  example of early from a function

# def chai_status(cups_left):
#     if cups_left == 0:
#         return("Sorry chai over")
#     return("chai is ready")

# print (chai_status(0))
# print (chai_status(5))


# example of multiple value

def chai_report():
    return 120 , 20

sold , remaining = chai_report()
print("sold: " , sold)
print("remaining: " , remaining)

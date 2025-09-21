#pure functions
def pure_chai(cups):
    return cups * 10

#impure functions
    total_chai = 0

def impure_chai(cups):
    global total_chai
    total_chai += cups


def pour_chai(n):
    print(n)
    if (n==0):
        return "All cups poured"
    return pour_chai(n-1)

print(pour_chai(5))


chai_types = ["ginger","cinnamon","tulsi","cinnamon"]

strong_chai  = list(filter(lambda chai:chai != "cinnamon", chai_types))

print(strong_chai)
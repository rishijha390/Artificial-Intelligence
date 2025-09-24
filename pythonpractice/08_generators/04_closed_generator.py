def local_chai():
    yield "Masala chai"
    yield "Ginger chai"

def imported_chai():
    yield "oolong"
    yield "Matcha"


def full_menu():
    yield from local_chai()
    yield from imported_chai()

for chai in full_menu():
    print(chai)


def chai_stall():
    try:
        while True:
            order = yield "Waiting for chai order"
    except:
        print("Stall closed, no more chai")


stall = chai_stall()
print(next(stall))
stall.close()
 
     
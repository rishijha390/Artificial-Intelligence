def serve_chai():
    yield "Cup 1: Masala Chai"
    yield "Cup 2: Green Chai"
    yield "Cup 3: Ginger Chai"

stall = serve_chai()
for cup in stall:
    print(cup)

def get_chai_list():
    return ["Cup 1", "Cup 2", "Cup 3"]

def get_chai_gen():
    yield "Cup 1"
    yield "Cup 2"
    yield "Cup 3"


chai = get_chai_gen()
print(next(chai))
print(next(chai))
print(next(chai))

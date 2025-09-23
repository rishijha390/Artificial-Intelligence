def infinite_generator():
    count = 1
    while True:
        yield f"Refil #{count}"
        count += 1

refill = infinite_generator()
user2 = infinite_generator()

for _ in range(5):
    print(next(refill))

for _ in range(6):
    print(next(user2))
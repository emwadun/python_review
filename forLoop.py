friends = ["Mike", "Alex", "William", "Judy"]
print(len(friends))

for i in friends:
    print(i)
print("\n")


for index in range(10):
    print(index)
print("\n")


for index in range(2, 10):
    print(index)
print("\n")

for index in range(len(friends)):
    print(index)
print("\n")


for index in range(5):
    if index == 0:
        print("This is first iteration")
    else:
        print("Not the first iteration")
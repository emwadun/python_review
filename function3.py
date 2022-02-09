def myFunc():
    global x #Global variable now not only inside the fuction.
    x = "fantastic"
    print(f"python is {x}")

myFunc()

print(f"python is {x}")
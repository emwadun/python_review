
from dis import dis


myLuckyNumbers = [43, 5, 1, 34, 78, 89, 9, 10]

dishes = ["rice", "beans", "chapo", "cake", "spaghetti"]

print(myLuckyNumbers)
print(dishes)

myLuckyNumbers.append(dishes)
print(myLuckyNumbers)

myLuckyNumbers.append("books")
print(myLuckyNumbers)

dishes.insert(3,"meat")
print(dishes)

dishes.remove("rice")
print(dishes)

#dishes.clear()
#print(dishes)

dishes.pop()
print(dishes)

print(dishes.index("cake"))

dishes.sort()
print(dishes)

dishes.reverse()
print(dishes)

dishes2 = dishes.copy()
print(f"This is the output of the copy array: {dishes2}")
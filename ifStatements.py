
isRaining = True
isWindy = True

if isRaining and not (isWindy):
    print("The season is Autumn")
elif isRaining or isWindy:
    print("The season is Spring")
else:
    print("None of the above")
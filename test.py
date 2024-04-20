L = [11,21,51,101]

print(dir(type(L)))

value1 = int(input("Enter First number"))
value2 = int(input("Enter Second number"))

m = 0
if(value1 > value2):
    m = value1
else:
    m = value2

print("m : ",m)
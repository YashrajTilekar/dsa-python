List = [10 ,20 ,30 ,40 ,50 ,15]

print("Before L : " ,List)

key = List[len(List) - 1]

i =len(List) - 2
while(i > -1 and List[i] > key):
    List[i+1] = List[i]
    i = i - 1

List[i+1] = key
print("After L : " ,List) 
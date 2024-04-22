def findMax(L):
    maxElement = L[0]

    Cnt = 1
    while(Cnt < len(L)):
        if(L[Cnt] > maxElement):
            maxElement = L[Cnt]    
        Cnt = Cnt+1

    return maxElement

maxRet = findMax([11,21,51,1912,23])
print(maxRet)
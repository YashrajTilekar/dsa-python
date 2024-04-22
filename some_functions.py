a = 10
print(type(a))

a = 3.142
print(type(a))

def findMax(L : list[int]) -> int:
    """_summary_

    Args:
        L (list[int]): _description_

    Raises:
        TypeError: _description_
        ValueError: _description_

    Returns:
        int: _description_
    """
    if(type(L) != list):
        raise TypeError("L must be a list object")
    elif(len(L) == 0):
        raise ValueError("L must be non empty")
    
    maxElement = L[0]

    Cnt = 1
    while(Cnt < len(L)):
        if(L[Cnt] > maxElement):
            maxElement = L[Cnt]    
        Cnt = Cnt+1

    return maxElemen

#findMax("sadasdads")
help(print)
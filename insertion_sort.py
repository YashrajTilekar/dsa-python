def getList(N : int) -> None:
    """
    Args:
        N (int): expected size of list
    
    Output :
        Populates newly created the list @numList with N random number
        stipulated between 0 to 1000 
    """

    from random import randint

    if(type(N) != int):
        raise TypeError("N must be an int")

    if(N <= 0):
        raise ValueError("N must be positive")

    numList = []
    startingNumber = 0
    endingNumber = 1001

    for i in range(N):
        numList.append(randint(startingNumber ,endingNumber))
    
    return numList

def showList(numList : list[int] ,msg : str) -> None:
    """
    Args:
        numList (list[int]): list of integers
        msg (str): string message
    """

    print(msg)

    for i in range(len(numList)):
        print(f"List[{i}] : {numList[i]}")

def insertAtSortingPosition(numList : list[int] ,N : int) -> None:
    """
    Args:
        numList (list[int]): non-empty li
        N (int): _description_
    """

    if(type(numList) != list or type(N) != int):
        raise TypeError("Bad type for input data")
    if(N < 2):
        raise ValueError("N must be greater than or equal to 2")
    
    

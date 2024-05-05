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
     @input: 
        @L: non-empty list of integers 
        @N: length of list (not necessarily equal to len(L))
    @output: 
        None 
    @precondition: 
        1) N >= 2 
        2) L[0] to L[N-2] are sorted in non-decreasing order 
        3) Value of L[N-1] may be preventing from L[0] to L[N-1] 
            from being sorted
    @postcondition: 
        1) L[0] to L[N-1] is sorted  
    """
    if(type(numList) != list or type(N) != int):
        raise TypeError("Bad type for input data")
    if(N < 2):
        raise ValueError("N must be greater than or equal to 2")
    
    key = numList[N - 1]
    i = N - 2

    while(i >= 0 and numList[i] > key):
        numList[i + 1] = numList[i]
        i = i - 1 
    
    numList[i + 1] = key

def insertionSort(numList : list[int]) -> None :
    """
    @input: 
        @L: L is a non-empty list of integers with no order 
    @output: 
        @L is sorted in place 
    """ 

    if(type(numList) != list):
        raise TypeError("Bad input data")
    elif(len(numList) <= 1):
        return None
    
    N = len(numList)

    for i in range(2 ,N+1):
        insertAtSortingPosition(numList ,i)
    
def main(): 
    N = int(input("Enter the size of the list:(greater than 2):"))
    if N < 2: 
        print("Bad size")
        sys.exit(-1)

    L = getList(N)
    showList(L, "Before sort:")
    insertionSort(L)
    showList(L, "After sort:")

main()    
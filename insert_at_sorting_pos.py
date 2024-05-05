import sys

def insertAtSortingPos(numList):
    N = len(numList)
    key = numList[N - 1] #last element
    i = N - 2  

    while(i >= 0 and numList[i] > key):
        numList[i + 1] = numList[i]
        i = i - 1

    numList[i + 1 ] = key


def main():
    data = [10 ,20 ,30 ,40 ,50 ,60 ,15]
    
    print("Before" ,data)
    insertAtSortingPos(data)
    print("After" ,data)

    sys.exit()

main()
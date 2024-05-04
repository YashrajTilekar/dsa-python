def recursiveBinarySearch(numList : list[int] ,searchData : int ,startIndex : int ,endIndex : int) -> bool:
    midIndex = (startIndex + endIndex) // 2 

    if(startIndex > endIndex):
        return False

    if(searchData == numList[midIndex]):
        return True
    elif(searchData >= numList[midIndex]):
        return recursiveBinarySearch(numList ,searchData ,midIndex+1 ,endIndex)
    elif(searchData < numList[midIndex]):
        return recursiveBinarySearch(numList ,searchData ,startIndex ,midIndex-1)


def main():
    Data = [11 ,21 ,51 ,101 ,121 ,151 ,201 ,221 ,250]
    ret = recursiveBinarySearch(Data ,221 ,0 ,len(Data)-1)

    print(ret)

if(__name__ == "__main__"):
    main()

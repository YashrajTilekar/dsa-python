class Node:
    def __init__(self ,newData : int) -> None:
        if(type(newData) != int):
            raise TypeError("Bad Type : newData")
        
        self.data = newData
        self.next = None


def main():
    nObj1 = Node(100)
    print(nObj1.__dict__)

    nObj2 = Node(200)
    print(nObj2.__dict__)

main()
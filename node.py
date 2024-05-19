class Node:
    def __init__(self) -> None:
        print("Inside Node.__init__()")
        print("Inside Node.__init__():id(self)" ,id(self))


def main():
    nObj = Node()
    print(type(nObj))
    print(id(nObj))
    print(nObj.__dict__)

main()
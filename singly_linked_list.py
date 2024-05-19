"""
@author : Yashraj Tilekar
@goal : To implement & test singly linked list
"""

class Node :
        def __init__(self ,newData : any) -> None:
            self.data = newData
            self.next = None

class SinglyLinkedList :
    def __init__(self) -> None:
        self.headNode = Node(None)

def main():
    L = SinglyLinkedList()

    print('L.__dict__' ,L.__dict__)
    print('L.headNode.__dict__' ,L.headNode.__dict__)

main()
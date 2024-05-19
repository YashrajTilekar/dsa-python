class Node:
    def __init__(self ,data : any) -> None:
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self) -> None:
        self.headNode = Node(None)

    def insertStart(self ,newData : any) -> bool:
        newNode = Node(newData)
        newNode.next = self.headNode.next
        self.headNode.next = newNode

        return True

    def insertEnd(self ,newData : any) -> bool:
        newNode = Node(newData)
        run = self.headNode

        while(run.next != None):
            run = run.next

        run.next = newNode
        return True

    def insertAfter(self ,existingData : any ,newData : any) -> bool:
        run = self.headNode
    
        while(run != None):
            if(run.data == existingData):
                break

            run = run.next
        
        if(run == None):
            raise ValueError(f'{existingData} is NOT found')
        
        newNode = Node(newData)
        newNode.next = run.next
        run.next = newNode
        
        return True

    def insertBefore(self ,existingData : any ,newData : any) -> bool:
        run = self.headNode
    
        while(run != None):
            if(run.next.data == existingData):
                break

            run = run.next
        
        if(run == None):
            raise ValueError(f'{existingData} is NOT found')
        
        newNode = Node(newData)
        newNode.next = run.next
        run.next = newNode
        
        return True
    
    def getStart(self) -> any:
        pass

    def getEnd(self) -> any:
        pass

    def popStart(self) -> any:
        pass

    def popEnd(self) -> any:
        pass

    def removeStart(self) -> any:
        pass

    def removeEnd(self) -> any:
        pass

    def removeData(self ,data) -> any:
        pass

    def isEmpty(self) -> any:
        pass

    def getLength(self) -> any:
        pass

    def show(self) -> any:
        run = self.headNode.next

        while(run != None):
            print(f'|{run.data}|->' ,end='')
            run = run.next

        print('None')

def main():
    L = SinglyLinkedList()
    
    L.insertStart(11)
    L.insertStart(21)

    L.insertEnd(51)
    L.insertEnd(101)

    L.show()

    L.insertAfter(11 ,15)
    L.show()
    L.insertBefore(101 ,75)
    L.show()

main()
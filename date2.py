class Date:
    def __init__(self):
        print("self.__dict__ -->" ,self.__dict__)
        self.day = 25

        print("self.__dict__ -->" ,self.__dict__)
        self.month = 11

        print("self.__dict__ -->" ,self.__dict__)
        self.year = 2001

dObj = Date()
print("dObj.__dict__ -->" ,dObj.__dict__)
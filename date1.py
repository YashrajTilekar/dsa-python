class Date:
    def __init__(self):
        print("Date.__init__() : Entered")
        print("Date.__init__() : type(self)" ,type(self))
        print("Date.__init__() : id(self)" ,id(self))
        print("Date.__init__() : Leaving")

dObj1 = Date()
dObj2 = Date()

print("id(dObj1)" ,id(dObj1))
print("id(dObj2)" ,id(dObj2))
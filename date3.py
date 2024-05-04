"""
@author : Yashraj Tilekar
@date : 4th May 2024
@goal : To implement Date class with getter and setters
"""

import sys

class Date:
    """
    Date class
    @__init__() : constructor accepting day ,month ,year
    @getDay() : getter for day attribute
    @getMonth() : getter for month attribute
    @getYear() : getter for year attribute
    @setDay() : setter for day attribute
    @setMonth() : setter for month attribute
    @setYear() : setter for year attribute
    @show() : displays object contents
    """
    @staticmethod
    def isValid(day : int ,month : int ,year : int) -> bool:
        return True

    def __init__(self ,init_day : int ,init_month : int ,init_year : int) -> None:
        if(type(init_day) != int or type(init_month) != int or type(init_year) != int):
            raise TypeError("day ,month ,year initializer must be an integer")

        self.day = init_day
        self.month = init_month
        self.year = init_year

    def getDay(self) -> int:
        return self.day
    
    def getMonth(self) -> int:
        return self.month
    
    def getYear(self) -> int:
        return self.year
    
    def setDay(self ,newDay : int) -> None:
        if(type(newDay) != int):
            raise TypeError("Day must be int")

        self.day = newDay
    
    def setMonth(self ,newMonth : int) -> None:
        if(type(newMonth) != int):
            raise TypeError("Month must be int")

        self.month = newMonth
    
    def setYear(self ,newYear : int) -> None:
        if(type(newYear) != int):
            raise TypeError("Year must be int")

        self.year = newYear

    def show(self) -> None:
        print(f"{self.day}/{self.month}/{self.year}")
    

def main():
    dObj = Date(4 ,5 ,2024)
    dObj.show()

    dObj.setDay(25)
    dObj.setMonth(11)
    dObj.setYear(2001)

    dObj.show()


    sys.exit()

main()
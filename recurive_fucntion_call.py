def f5():
    print("I am the last call")
    return None

def f4():
    print("Inside F4s")
    f5()
    return None

def f3():
    print("Inside F3")
    f4()
    return None

def f2():
    print("Inside F2")
    f3()
    return None

def f1():
    print("Inside F1")
    f2()
    return None

f1()
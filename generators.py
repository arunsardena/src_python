# program on generators


# #A Generator in Python is a function that returns an iterator using the Yield keyword. 
# def generator():
#     yield statement


def simplegeneratorfun():
    yield 1
    yield 2
    yield 3

for key in simplegeneratorfun():
    print(key)
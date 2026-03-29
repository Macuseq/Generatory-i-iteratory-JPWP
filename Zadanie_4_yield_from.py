#Zadanie 4 - yield from
#Połącz dwa osobne generatory w jeden generator używając yield from

def gen1():
    yield 1
    yield 2

def gen2():
    yield 3
    yield 4

def combined():
    # TODO

for x in combined():
    print(x)
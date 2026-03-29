#Zadanie 2a - Własny iterator
#Uzupełnij klasę tak, aby:

#działała jak iterator,
#zwracała kolejne liczby parzyste zaczynając od 0,
#kończyła się na wartości max_value (włącznie, jeśli parzysta),
#po przekroczeniu zakresu rzucała StopIteration.

#Podpowiedź:
#Dodaj:

#__iter__
#__next__


class EvenNumbers:
    def __init__(self, max_value):
        self.max_value = max_value


nums = EvenNumbers(10)

for n in nums:
    print(n)
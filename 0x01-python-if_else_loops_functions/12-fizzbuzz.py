#!/usr/bin/python3
def fizzbuzz():
   for n_ in range(1, 101):
        if n_ % 3 == 0 and n_ % 5 == 0:
            print("FizzBuzz", end=" ")
        elif n_ % 3 == 0:
            print("Fizz", end=" ")
        elif n_ % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(n_), end=" ")

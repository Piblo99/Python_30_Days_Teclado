import fractions
from math import fsum
import random as rand


numbers = [1.43, 1.1, 5.32, 87.032, 0.2, 23.4]
print(fsum(numbers))

fraction = fractions.Fraction(2.25)
print(fraction)


target_number = rand.randint(1, 100)


guess = int(input("Enter a number: "))

while guess != target_number:
    if guess > target_number:
        print("Guess lower!")
    elif guess < target_number:
        print("Guess higher!")
    guess = int(input("Enter a number: "))
	    

print("You guessed correctly!")
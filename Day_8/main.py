target_number = 47

guess = int(input("Enter a number: "))

while guess != target_number:
	if guess > target_number:
		print("Too high!")
	else:
		print("Too low!")

	guess = int(input("Enter a number: "))

print("You guessed correctly!")

sample_string = "Python"

for character in sample_string:
	if character == "o":
		continue

	print(character)

primes = []

for dividend in range(2, 101):
	for divisor in range(2, dividend):
		if dividend % divisor == 0:
			break
	else:
		primes.append(str(dividend))

print(", ".join(primes))


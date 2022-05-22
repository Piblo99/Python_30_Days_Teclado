s = set()
s.update(range(1, 4))

random_values = {"r", 1, ("Python", "C", "Rust")}

print(s.union(random_values))
print(s.symmetric_difference(random_values))
print(s.intersection(random_values))

numbers = range(27, 54)
user_number = int(input("Enter a number: "))

if user_number in numbers:
	print("Your number is in the valid range.")
else:
	if user_number < numbers[0]:
		print("Your number is too low.")
	else:
		print("Your number is too high.")
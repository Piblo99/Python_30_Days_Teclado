def exponentiate(base, exponent):
	return exponent ** base

def process_string(raw_string):
	return raw_string.strip().lower()

("Tom Hardy", "English", 42)

def dictify(actor):
	name, nationality, age = actor

	return {
		"name": name,
		"nationality": nationality,
		"age": age
	}

dividend = int(input("Please enter a number: "))

def is_prime(dividend):
	if dividend < 2:
		return False

	for divisor in range(2, dividend):
		if dividend % divisor == 0:
			return False

	return True
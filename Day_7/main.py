names = input("Please enter your full name: ").split()

given_name = names[0]
surname = names[1]

print(f"given name = {given_name}")
print(f"surname name = {surname}")

base_numbers = [1, 2, 3, 4, 5]
processed_numbers = []

for number in base_numbers:
	processed_numbers.append(str(number))

print(" | ".join(processed_numbers))

quotes = [
	"'What a waste my life would be without all the beautiful mistakes I've made.'",
	"'A bend in the road is not the end of the road... Unless you fail to make the turn.'",
	"'The very essence of romance is uncertainty.'",
	"'We are not here to do what has already been done.'"
]

for quote in quotes:
	print(quote.strip("'"))

sample_string = input("Please enter a word: ").strip()

character_count = len(sample_string)
word_count = len(sample_string.split())

print(f"Character count: {character_count}")
print(f"Word count: {word_count}")
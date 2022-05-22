def add(a, b):
	print(a + b)

def subtract(a, b):
	print(a - b)

def multiply(a, b):
	print(a * b)

def divide(a, b):
	if b == 0:
		print("You can't divide by 0!")
	else:
		print(a / b)

def print_show_info(show):
	print(f"{show['title']} ({show['initial_release']}) - {show['seasons']} season(s)")

series_data = [
	{"title": "Breaking Bad", "seasons": 5, "initial_release": 2008},
	{"title": "Fargo", "seasons": 4, "initial_release": 2014},
	{"title": "Firefly", "seasons": 1, "initial_release": 2002},
	{"title": "Rick and Morty", "seasons": 4, "initial_release": 2013},
	{"title": "True Detective", "seasons": 3, "initial_release": 2014},
	{"title": "Westworld", "seasons": 3, "initial_release": 2016},
]

for show in series_data:
	print_show_info(show)


def is_palindrome(word):
	word = word.strip().lower()
	reversed_word = word[::-1]

	if word == reversed_word:
		print(True)
	else:
		print(False)

is_palindrome("Hannah")  # True
is_palindrome("Fred")    # False
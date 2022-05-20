main_characters = [
	("BoJack Horseman", "Will Arnett", "Horse"),
	("Princess Carolyn", "Amy Sedaris", "Cat"),
	("Diane Nguyen", "Alison Brie", "Human"),
	("Mr. Peanutbutter", "Paul F. Tompkins", "Dog"),
	("Todd Chavez", "Aaron Paul", "Human")
]

for character, actor, species in main_characters:
	print(f"{character} is a {species.lower()} voiced by {actor}.")

student = ("John Smith", 11743, ("Computer Science", "Mathematics"))

name, id_number, (major, minor) = student
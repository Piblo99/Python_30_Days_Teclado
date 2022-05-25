grades = input("Please enter your grades, separated by commas: ").split(",")

try:
	grades = [int(grade) for grade in grades]
except ValueError:
	print("The grades you entered were in an invalid format.")

def func():
	try:
		return "Returned from the try clause!"
	finally:
		return "Returned from the finally clause!"

print(func())  # "Returned from the finally clause!"

try:
	with open("data.txt", "r") as text_file:
		print(text_file.read())
except FileNotFoundError:
	print("Error: Couldn't find data.txt")
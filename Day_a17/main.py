def multi_add(*numbers):
	print(sum(numbers))

def arg_printer(*args, **kwargs):
	args = [repr(arg) for arg in args]
	print(f"Positional arguments are: {', '.join(args)}")

	kwargs = [f"{key}={repr(value)}" for key, value in kwargs.items()]
	print(f"Keyword arguments are: {', '.join(kwargs)}")

countries = [
{
	"name": "Germany",
	"population": "83 million",
	"capital": "Berlin",
	"currency": "Euro"
},
{
	"name": "Spain",
	"population": "89 million",
	"capital": "Madrid",
	"currency": "Euro"
},

]

country_template = """
Name: {name}
Population: {population}
Capital: {capital}
Currency: {currency}"""

for country in countries:
    print(country_template.format(**country))

print(*range(1, 21), sep=", ")

print(*range(1, 21), sep="\n")
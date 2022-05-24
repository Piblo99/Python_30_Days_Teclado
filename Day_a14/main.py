with open("iris.csv", "r") as iris_file:
	iris_data = iris_file.readlines()
print(iris_data)


irises = []

for row in iris_data[1:]:
	sepal_length, sepal_width, petal_length, petal_width, species = row.strip().split(",")

	iris_dict = {
		"sepal_length": sepal_length,
		"sepal_width": sepal_width,
		"petal_length": petal_length,
		"petal_width": petal_width,
		"species": species
	}

	irises.append(iris_dict)
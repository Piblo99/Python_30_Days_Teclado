numbers = [(23, 3, 56), (98, 1034, 54), (254, 344, 5), (45, 2), (122, 63, 74)]
totals = map(sum, numbers)

print(next(totals))  # 82
print(next(totals))  # 1186

import itertools

employees = itertools.cycle(["Peter", "Fiona", "Carl", "Helen"])
days = itertools.cycle(["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"])

for day_number in range(1, 31):
	print(f"Day {day_number} ({next(days)}): {next(employees)} closes.")
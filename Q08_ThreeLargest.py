A = [int(x) for x in input("Enter elements: ").split(" ")]

first = second = third = -9999999999

for x in A:
	if first < x:
		third = second
		second = first
		first = x
	elif second < x:
		third = second
		second = x
	elif third < x:
		third = x
print(first, second, third)
"""
Print Nth fibonacci no.
"""
N = int(input("Enter N for Nth Fibonacci No: "))
if N == 1:
	print(1)
elif N > 1:
	print(1, 1, end = " ")
i = 1
a = b = 1
while i <= N - 2:
	c = a + b
	print(c, end = " ")
	a = b
	b = c
	i += 1
print()
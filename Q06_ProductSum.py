'''
Given an array A[] of integers find sum of product of all pairs of array elements
i. e., we need to find of product after execution of following pseudo code.
'''
A = [int(x) for x in input().split()]

sum_all = 0
sum_square_all = 0

for x in A:
	sum_all += x
	sum_square_all += x**2

ProductSum = (sum_all**2 - sum_square_all)//2
print(ProductSum)
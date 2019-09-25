"""
Write a program that,
given an array A[] of n numbers and another number x,
determines whether or not there exist two elements in A whose sum is exactly x.
"""

A = [int(x) for x in input().split()]
x = int(input())
S = set()
L = []
for i in A:
	if x-i in S:
		L.append([i, x-i])
	else:
		S.add(i)
print(L)
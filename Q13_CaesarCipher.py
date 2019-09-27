choice =int(input("Enter 1 to encrypt text or 2 to decrypt: "))
A = input("Enter text: ")
n = int(input("Enter shift: "))
if choice == 1:
	Ans = ''
	for x in A:
		j = ord(x)
		if j >= 65 and j <= 90:
			j += n%26
			if j > 90:
				j = 64 + j - 90
		elif j >= 97 and j <= 122:
			j += n%26
			if j > 122:
				j = 96 + j - 122
		Ans += chr(j)
	print(Ans)
elif choice == 2:
	Ans = ''
	for x in A:
		j = ord(x)
		if j >= 65 and j <= 90:
			j -= n%26
			if j < 65:
				j = 91 - 65 + j
		elif j >= 97 and j <= 122:
			j -= n%26
			if j < 97:
				j = 123 + j - 97
		Ans += chr(j)
	print(Ans)
else:
	print(A)
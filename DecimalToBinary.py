def DecimalToBinary(num):
	binary = ""
	
	while num>0:
		binary += str(num % 2)
		num //= 2

	for i in binary[::-1]:
		print(i, end="")

num = int(input("Enter Decimal: "))
DecimalToBinary(num)
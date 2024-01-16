def ArmstrongNum(num):
	sum = 0
	counter = 0
	list = []
	while num:
		list.append(num%10)
		num //= 10 
		counter += 1	
	for i in list:
		sum += i**counter
	
	return sum

num = int(input("Enter num: "))
if ArmstrongNum(num) == num:
	print("{} is an Armstrong Number" .format(num))
else:
	print("{} is not an Armstrong Number" . format(num))
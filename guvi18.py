lower = int(input("enter the low range:"))
higher = int(input("enter the high range:"))
for num in range (lower+higher+1):
	order=len(str(num))
	sum = 0
	temp = num
	while temp > 0:
		digit = temp % 10
		sum += digit**3
		temp //=10
if (sum==num):
	print ("num")
		

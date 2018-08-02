#Factorial of a number

num=int(input("Enter a number:"))
f=1
if (num<0):
	print("Factorial of negative numbers does not exist")
elif (num==0):
	print("Factorial of zero is 1")
else:
	for i in range (1,num+1):
		print(i)
		f=f*i
	print("The factorial of",num,"is",f)

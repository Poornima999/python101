class Lcm_Gcd:
	def __init__(self,num1,num2):
		self.num1=num1
		self.num2=num2

	#LEAST COMMON MULTIPLE OF TWO NUMBERS

	def lcm_fun(self):
		mul1=[]
		mul2=[]
		for i in range(1,10):
			mul1.append(self.num1*i)
		print(mul1)
	
		for j in range(1,10):
			mul2.append(self.num2*j)
		print(mul2)

		c_mul= [i for i in mul1 if i in mul2]
		print("common multiples are:",c_mul)
		print("lcm of ",self.num1, "and ",self.num2, "is: ",min(c_mul))

	#GREATEST COMMON DIVISOR

	def gcd_fun(self):
		f1=[]
		f2=[]
		for k in range(1,self.num1+1):
			if ((self.num1%k)==0):
				f1.append(k)
		print(f1)

		for k in range(1,self.num2+1):
			if ((self.num2%k)==0):
				f2.append(k)
		print(f2)

		c_factor= [i for i in f1 if i in f2]
		print("common factors are:",c_factor)
		print("gcd of ",self.num1, "and ",self.num2, "is: ",max(c_factor))



L=Lcm_Gcd(25,50)
L.lcm_fun()
L.gcd_fun()
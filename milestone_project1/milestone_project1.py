
#MILESTONE PROJECT 1
#====================

class MileStone_1:

	def __init__(self,w,h,str1,sent_1,sent_2):
		self.w = w
		self.h = h
		self.str1 = str1
		self.sent_1 = sent_1
		self.sent_2 = sent_2
	# BMI CALCULATOR
	#===================
	def bmi_calc(self):
		#self.h=float(input("Enter your height in centimeter:"))
		temp_height=self.h/100
		#Sself.w=float(input("enter your weight in kilo gram:"))
		bmi = round(self.w/ (temp_height*temp_height))
		
		#bmi=weight/(temp_height*temp_height)
		print("Your height is:",self.h)
		print("Your weight is:",self.w)
		
		print("Your Body Mass Index is ", round(bmi))
		if (bmi<18.5):
			print("You are underweight...")
		elif((bmi >= 18.5) & (bmi<=24.9) ):
			print("You have normal weight...")
		elif((bmi>=25) & (bmi<=29.9)):
			print("You are overweight......")
		else:
			print("Obese.....")

#COUNT THE NUMBER OF VOWELS IN THE STRING
#=========================================

	def vowel_count(self):
		#self.str1=str(input("Enter the string:"))
		c=0
		vowel='aeiou'
		print("The string that you entered is",self.str1)
		for letter in self.str1:
			if letter in vowel:
				c=c+1
		print("There are {} vowels in the word {}".format(c,self.str1))

#FIND THE REVERSE OF THE STRING
#==============================

	def reverse(self):
		#self.str1=input("Enter a string:")
		rev=self.str1[::-1]
		print("The reverse of the string is :",rev)

#FIND THE STRING IS PALINDROME OR NOT
#===================================

	def palindrome(self):
		#self.str1=input("Enter a string:")
		rev=self.str1[::-1]
		if self.str1==rev:
  			print("The string is palindrome")
		else:
			print("The string is not palindrome")

#SPLIT AND SORT A SENTENCE
#=========================

	def split_sort(self):
		#self.sent_2=input("Enter the sentence:\n")
		#print(self.sent_2)
		splitsentence=self.sent_2.split()
		print("The splited sentence is:\n",splitsentence)
		print("The sorted sentence is:\n",sorted(splitsentence))

#REMOVE THE PUNCTUATIONS FROM A SENTENCE
#=======================================

	def punctuations(self):
		punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
		#self.sent_2=input("Enter the string with punctuations:")
		new_str=""
		for p in self.sent_2:
			if p not in  punctuations :
				new_str= new_str+p
		print("The string with punctuations:",self.sent_2)
		print("The string after removing punctuations:",new_str)
		
 
   

obj_milestone1=MileStone_1(60,157,'python','hello friends',"hello [[[[hdd 099999jh")
obj_milestone1.bmi_calc()
obj_milestone1.vowel_count()
obj_milestone1.reverse()
obj_milestone1.palindrome()
obj_milestone1.split_sort()
obj_milestone1.punctuations()
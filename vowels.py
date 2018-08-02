str=input("Enter a string:")
count=0
vowel=['a','e','i','o','u']
for letter in str:
	if letter in vowel: 
		count = count + 1
print("There are {} vowels in the word {}".format(count,str))
  

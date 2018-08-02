punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
str_p=input("Enter the string with punctuations:")
new_str=""
for p in str_p:
	if p not in  punctuations :
		new_str= new_str+p
print("The string with punctuations:",str_p)
print("The string after removing punctuations:",new_str)



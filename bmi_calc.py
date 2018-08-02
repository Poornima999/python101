#BMI CALCULATOR
#BMI=WEIGHT/(HEIGHT*HEIGHT)
height=float(input("Enter your height in centimeter:"))
temp_height=height/100
weight=float(input("enter your weight in kilo gram:"))
bmi = round(weight/ (temp_height*temp_height))
#bmi=weight/(temp_height*temp_height)
print("Your Body Mass Index is ", round(bmi))
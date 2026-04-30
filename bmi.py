def calculate_bmi(weight,height):
    print("Height="+ str(height))
    print("Weight="+ str(weight))
    
    bmi= weight/(height**2)
    print("BMI= "+str(bmi))
    return bmi

bmi = calculate_bmi(weight=57, height=1.73)   
if bmi < 18.5:
    print("under weight")
elif bmi <= 25.0 or 18.5 <= bmi:
    print("normal weight")
else:
    print("overweight")

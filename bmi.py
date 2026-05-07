def calculate_bmi(weight,height):
    print("Height="+ str(height))
    print("Weight="+ str(weight))
    
    bmi= weight/(height**2)
    print("BMI= "+str(bmi))

    if bmi < 18.5:

        print("under weight")
        return -1
    elif 18.5 <= bmi <= 25.0:
        print("normal weight")
        return 0
    else:
        print("overweight")
        return 1
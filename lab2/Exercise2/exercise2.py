def calculate_bmi(height, weight):
    result = 0.0
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    height = float(height)
    weight = float(weight)
    bmi = float(weight/(height*height))
    if bmi < 18.5:
        print("Underweight")
        result = -1
    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        result = 0
    else:
        print("Overweight")
        result = 1
    print(result)
    return result


result = calculate_bmi(weight=57, height=1.73)
def calc_average_temperature():
    Temperature = get_values()
    print("Average temperature:", sum(Temperature)/len(Temperature))
def calc_min_max_temperature():
    Temperature = get_values()
    min_temp = min(Temperature)
    max_temp = max(Temperature)
    print("The min Temperature is ", min_temp, "\nThe max Temperature is ", max_temp)
def calc_median_temperature():
    Temperature = get_values()
    Temperature.sort()
    length_of_Temp = len(Temperature)
    if length_of_Temp % 2 == 1:
        median = Temperature[length_of_Temp//2]
    else:
        median = (Temperature[length_of_Temp//2 - 1] + Temperature[length_of_Temp// 2])/2

    print("The median is ", median)






def get_values():
    Input = input("enter temperature separated by a comma: ")
    Input = Input.split(",")
    Input = [float(num) for num in Input]
    return Input


Choice = input("Enter 1 for average \nEnter 2 for min and max\nEnter 3 for median temperature\n")
if (Choice == "1"):
    calc_average_temperature()

if (Choice == "2"):
    calc_min_max_temperature()

if (Choice == "3"):
    calc_median_temperature()
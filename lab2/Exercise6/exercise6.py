def calc_average_temperature(Temperature):
    average = sum(Temperature) / len(Temperature)
    print("Average temperature:", average)
    return average


def calc_min_max_temperature(Temperature):
    min_temp = min(Temperature)
    max_temp = max(Temperature)
    print("The min Temperature is ", min_temp, "\nThe max Temperature is ", max_temp)
    return [min_temp, max_temp]


def calc_median_temperature(Temperature):
    Temperature.sort()
    length_of_Temp = len(Temperature)
    if length_of_Temp % 2 == 1:
        median = Temperature[length_of_Temp // 2]
    else:
        median = (Temperature[length_of_Temp // 2 - 1] + Temperature[length_of_Temp // 2]) / 2

    print("The median is ", median)
    return median


def get_values():
    Input = input("enter temperature separated by a comma: ")
    Input = Input.split(",")
    Input = [float(num) for num in Input]
    return Input



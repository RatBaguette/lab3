def calc_average_temperature():
    Temperature = get_values()
    print("Average temperature:", sum(Temperature)/len(Temperature))
def calc_min_max_temperature():
    Temperature = get_values()
    min_temp = min(Temperature)
    max_temp = max(Temperature)
    print("The min Temperature is ", min_temp, "\nThe max Temperature is ", max_temp)

def get_values():
    Input = input("enter temperature separated by a comma: ")
    Input = Input.split(",")
    Input = [float(num) for num in Input]
    return Input


Choice = input("Enter 1 for average \nEnter 2 for min and max\n")
if (Choice == "1"):
    calc_average_temperature()

if (Choice == "2"):
    calc_min_max_temperature()

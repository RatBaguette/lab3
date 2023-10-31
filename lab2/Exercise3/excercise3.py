def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
def calc_average():
    Input = get_user_input()
    Split_Input = Input.split(",")
    numbers = [float(num) for num in Split_Input]
    print(sum(numbers)/len(numbers))
def get_user_input():
    Input = input()
    return Input
display_main_menu()
calc_average()

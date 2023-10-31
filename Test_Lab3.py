import Lab3

print("Test_Lab3")


def test_bubble_sort_ascending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [11, 12, 22, 25, 34, 64, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == test_arr)

def test_bubble_sort_descending():
    result = []
    input_arr = [64, 34, 25, 12, 22, 11, 90]
    test_arr = [90, 64, 34, 25, 22, 12, 11]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_DESCENDING)

    assert (result == test_arr)

def test_bubble_sort_number_greater_10():
    expected_result = 1
    input_arr = [12,123,25,12,35,123,345,234,234,12,32,334,42,3]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result== expected_result)

def test_bubble_sort_no_number():
    expected_result = 0
    input_arr = []

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == expected_result)

def test_bubble_sort_invalid():
    expected_result = 2
    input_arr = [64, "Five", 25, 12, 22, 11, 90]

    result = Lab3.bubble_sort(input_arr, Lab3.SORT_ASCENDING)

    assert (result == expected_result)
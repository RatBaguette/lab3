from lab2.Exercise6 import exercise6

def test_calc_median_temperature():
    expected_result = 3
    arr = [1,2,3,4,5]
    result = exercise6.calc_median_temperature(arr)
    assert (expected_result == result)

def test_clac_average_temperature():
    expected_result = 2
    arr = [1,2,3]
    result = exercise6.calc_average_temperature(arr)
    assert (expected_result == result)

def test_min_max_temperature():
    expected_result = [1,3]
    arr = [1,2,3]
    result = exercise6.calc_min_max_temperature(arr)
    assert (expected_result==result)
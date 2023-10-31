from lab2.Exercise2 import exercise2

def test_bmi_normal_weight():
    expected_result= 0
    result = exercise2.calculate_bmi(height=1.75, weight=70)
    assert (expected_result == result )

def test_bmi_over_weight():
    expected_result = 1
    result = exercise2.calculate_bmi(height=1.75, weight=90)
    assert (expected_result == result )

def test_bmi_under_weight():
    expected_result = -1
    result = exercise2.calculate_bmi(1.75,50);
    assert (expected_result == result )
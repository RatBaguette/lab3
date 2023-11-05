import price_info

def test_total_cost_shopping():
    expected_price = 12.0
    quantity_list = {'apple': 10, 'orange': 0, 'watermelon': 0, 'pineapple': 0, 'pear': 0, 'papaya': 0,
                     'pomegranate': 0}
    assert (expected_price == price_info.total_cost_shopping(quantity_list))

def test_cost_of_fruits():
    expected_output = 14
    input_fruit = 'orange'
    input_quantity = 10
    result = price_info.cost_of_fruits(input_fruit,input_quantity)
    assert (expected_output == result)
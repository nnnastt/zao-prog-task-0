from GrudininaAA import two_sum

def test_example_1():
    """тест1"""
    nums = [2, 7, 11, 15]
    target = 9
    assert two_sum(nums, target) == [0, 1]

def test_example_2():
    """тест 2"""
    nums = [3, 2, 4]
    target = 6
    assert two_sum(nums, target) == [1, 2]

def test_example_3():
    """тест 3"""
    nums = [3, 3]
    target = 6
    assert two_sum(nums, target) == [0, 1]

def test_no_solution():
    """Когда решения нет"""
    nums = [1, 2, 3]
    target = 10
    assert two_sum(nums, target) is None

def test_empty_array():
    """Массив пустой"""
    nums = []
    target = 5
    assert two_sum(nums, target) is None

def test_single_element():
    """один элемент"""
    nums = [5]
    target = 5
    assert two_sum(nums, target) is None

def test_negative_numbers():
    """отрицательные числа"""
    nums = [-1, -2, -3, -4, -5]
    target = -8
    assert two_sum(nums, target) == [2, 4]

def test_zeros_in_array():
    """нули"""
    nums = [0, 0, 1, 2]
    target = 0
    assert two_sum(nums, target) == [0, 1]

def test_large_numbers():
    """большие числа"""
    nums = [1000000, 2000000, 3000000]
    target = 5000000
    assert two_sum(nums, target) == [1, 2]

def test_duplicate_values():
    """повторение чисел с разными индексами"""
    nums = [5, 5, 10]
    target = 10
    assert two_sum(nums, target) == [0, 1]

def test_target_zero():
    """сумма = 0"""
    nums = [1, -1, 2, -2]
    target = 0
    assert two_sum(nums, target) == [0, 1]

def test_order_does_not_matter():
    """разный порядок индексов"""
    nums = [1, 2, 3, 4]
    target = 5
    result = two_sum(nums, target)
    assert result in [[0, 3], [3, 0], [1, 2], [2, 1]]

def test_first_and_last():
    """начало и конец"""
    nums = [1, 100, 200, 300, 400, 500, 999]
    target = 1000
    assert two_sum(nums, target) == [0, 6]

def test_middle_elements():
    """середина"""
    nums = [10, 20, 30, 40, 50]
    target = 70
    assert two_sum(nums, target) == [2, 3]

def test_all_same_numbers():
    """одинаковый числа"""
    nums = [7, 7, 7, 7]
    target = 14
    assert two_sum(nums, target) == [0, 1]

def test_negative_target():
    """отрицательная сумма"""
    nums = [-5, -3, -2, -1]
    target = -5
    assert two_sum(nums, target) == [1, 2]
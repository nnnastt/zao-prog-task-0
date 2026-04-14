def two_sum(nums, target):

    seen = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in seen:
            return [seen[complement], i]

        seen[num] = i

    return None
if __name__ == '__main__':
    print('=' * 40)
    print("ПРОГРАММА 'СУММА ДВУХ ЧИСЕЛ'")
    print('=' * 40)

    input_nums = input('Введите числа через пробел: ')
    nums = [int(x) for x in input_nums.split()]

    target = int(input('Введите целевую сумму target: '))

    print('-' * 40)

    result = two_sum(nums, target)

    if result:
        print(f'РЕЗУЛЬТАТ: индексы {result}')
        print(f'{nums[result[0]]} + {nums[result[1]]} = {target}')
    else:
        print(f'Решение не найдено')
        print(f' Никакие два числа в массиве не дают сумму {target}')

    print('=' * 40)
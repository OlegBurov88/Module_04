"""
Пузырьковая сортировка
"""


def bubble_sort(ls):
    swapper = True
    while swapper:
        swapper = False
        for i in range(len(ls) - 1):
            if ls[i] > ls[i + 1]:
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swapper = True


if __name__ == '__main__':
    nums = [5, 6, 2, 1, 3, 4]
    bubble_sort(nums)
    print(nums)

"""
Cортировка выборки
"""


def selection_sort(ls):
    for i in range(len(ls)):
        lowest = i
        for j in range(i + 1, len(ls)):
            if ls[j] < ls[lowest]:
                lowest = j
        ls[i], ls[lowest] = ls[lowest], ls[i]


if __name__ == '__main__':
    nums = [5, 6, 2, 1, 3, 4]
    selection_sort(nums)
    print(nums)

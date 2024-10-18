from module_4.sortfunc_2 import insertion_sort, bubble_sort, selection_sort
import time

data_1 = [9, 7, 4, 5, 6, 7, 1, 2]
data_2 = [9, 7, 4, 5, 6, 7, 1, 2, 20, 10, 1]
data_3 = [9, 7, 4, 5, 6, 7, 1, 2, 321, 1, 5, 2, 3, 6, 9, 8, 7, 1, 2, 3, 6, 54, 8, 9, 7]


start = time.perf_counter()
print(insertion_sort(data_1), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')

start = time.perf_counter()
print(insertion_sort(data_2), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')

start = time.perf_counter()
print(insertion_sort(data_3), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')


start = time.perf_counter()
print(bubble_sort(data_1), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')

start = time.perf_counter()
print(bubble_sort(data_2), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')

start = time.perf_counter()
print(bubble_sort(data_3), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')


start = time.perf_counter()
print(selection_sort(data_1), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')

start = time.perf_counter()
print(selection_sort(data_2), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')

start = time.perf_counter()
print(selection_sort(data_3), end=' ')
end = time.perf_counter()
print(f'Затраченное время: {(end-start)*10**6} мкс')

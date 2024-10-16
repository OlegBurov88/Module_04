def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')

    inner_function()


test_function()
# inner_function()
"""
Вызов функции inner_function вызывает ошибку, так как данная функция находится
в области видимости функции test_function(является для нее локальной).
Её можно вызывать только в пределах видимости той зоны в которой она находится.
"""

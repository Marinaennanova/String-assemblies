"""Задача:Range - это просто"""
# Создайте пользовательский класс исключения StepValueError, который наследуется от ValueError.
# Наследования достаточно, класс оставьте пустым при помощи оператора pass
class StepValueError(ValueError):
    pass

# Создайте класс Iterator, который обладает следующими свойствами и атрибутами __init__(self, start, stop, step=1):
class Iterator:
    def __init__(self, start, stop, step=1):
# Атрибуты объекта:
# start - целое число с которого начинается итерация.
# stop - целое число на котором заканчивается итерация.
# step - шаг с которой совершается итерация.Step не может быть 0.
# pointer - указывает на текущее число в итерации pointer = start (изначально start)

        self.start = start
        self.stop = stop
        self.step = step
        self.pointer = start
        if step == 0:
# создание собственного исключения при помощи оператора raise
            raise StepValueError('Шаг не может быть равен 0')
#__iter__- метод, сбрасывающий значение pointer на start и возвращающий сам объект итератора.
    def   __iter__(self):
        self.pointer = self.start
        return self
# __next__ - метод, увеличивающий атрибут pointer на step. В зависимости от знака атрибута step итерация
# завершится либо когда pointer станет больше stop, либо меньше stop.

    def __next__(self):
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration
        result = self.pointer
        self.pointer += self.step # увеличили на step
        return result
# этот блок целиком я копирую из услобия задачи
try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError:
    print("Шаг не может быть равен 'O'")

# Вводимые значения
iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)

# Вывод результата
for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()


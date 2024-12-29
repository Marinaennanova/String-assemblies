""" Цель задания:

Освоить механизмы создания декораторов Python.

Практически применить знания, создав функцию декоратор и обернув ею другую функцию.  """


# Функция декоратор (is_prime), которая распечатывает "Простое",
# если результат 1ой функции будет простым числом и "Составное" в противном случае.
def is_prime(func):
# внутренняя функция wrapper в is_prime
    def wrapper(*args):
        result = func(*args)
        summ = sum(args)
        k = 0
        for i in range(2, summ // 2 + 1):
            if summ % i == 0:
                k = k +1
        if k <= 0:
            print('Простое')
        else:
            print('Составное')
        return result
    return wrapper

# @is_prime - декоратор для функции sum_three
@is_prime
# Функция, которая складывает 3 числа (sum_three)
def sum_three(*args):
    return sum(args)



result = sum_three(2, 3, 6)
print(result)

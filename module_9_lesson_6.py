#Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
# при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
from itertools import combinations
def all_variants(text):
    for x in text:
        yield x
    for r in combinations(text,2):
        print (r)
    print(text)

a = all_variants("луковка")
for i in a :
    print(i)



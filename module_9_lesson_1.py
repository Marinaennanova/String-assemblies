def apply_all_func(int_list, *functions):
    results={}
    for i in functions:
        results[i.__name__] = i(int_list) #запись в словарь results функции под ключом её названия,синтаксис my_dict[key]=value (i.__name__ функция с ее именем)
    return results 
       
print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
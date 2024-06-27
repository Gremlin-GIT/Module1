# совари
my_dict = {"Вася": 2002, "Света": 1995, "Никифор": 1979,}
print("Словарь my_dict:")
print(my_dict)
print("Значение по существующему ключу 'Вася':", my_dict.get("Вася"))
print("Значение по отсутствующему ключу 'Влад':", my_dict.get("Влад"))
my_dict["Алла"] = 2001
my_dict["Толик"] = 2003
print("Обновленный словарь my_dict:")
print(my_dict)
removed_value = my_dict.pop("Света")
print("Удалено значение из пары с ключом 'Света':", removed_value)
print("Обновленный словарь my_dict:")
print(my_dict)
# множества
my_set = {1, 2, 3, "кумкват", "фейхоа", "дуриан"}
print("Множество my_set:")
print(my_set)
my_set.add(4)
my_set.add("арбуз")
my_set.remove(3)
print("Измененное множество my_set:")
print(my_set)
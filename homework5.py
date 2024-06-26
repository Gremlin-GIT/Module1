# Переменные разных типов данных.
immutable_var = (1, 6.72, "pycharm", True)
print(immutable_var)

# Попытка изменить элементы кортежа immutable_var.
# Выводится ошибка, т.к. кортеж является неизменяемым типом данных.
# immutable_var[0] = 2
# print(immutable_var)

# Изменяемые структуры данных.
mutable_list = [1, 5.05, "PS One", False]
print(mutable_list)

# Изменение элементов списка mutable_list.
mutable_list[0] = 7
mutable_list[2] = "Python"
print(mutable_list)
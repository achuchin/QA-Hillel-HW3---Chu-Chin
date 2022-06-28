# 1 Зформуйте строку, яка містить певну інформацію про символ в відомому слові.
# Наприклад "The [номер символу] symbol in [тут слово] is '[символ з відповідним порядковим номером]'".
# Слово та номер отримайте за допомогою input() або скористайтеся константою.
# Наприклад (слово - "Python" а номер символу 3) - "The 3 symbol in "Python" is 't' ".

# если пользователь введет номер символа 0 - то результатом будет индекс -1, ввыедется последняя буква слова - не обработал эту ошибку
#  не обработал невалидные данные. Введите слово - работает только с str, Введите номер символа в слове - работает только с int.

word_request = str(input('Введите слово: '))
symbol_num = int(input('Введите номер символа в слове: '))

# перевожу введенное число в индекс символа
symbol_index = symbol_num - 1

# создаю переменную, кт обращается к индексу символа слова
symbol_result = (word_request[symbol_index])

print('The {number} symbol in {word} is {result}'.format(number = symbol_num, word = word_request, result = symbol_result))



# 2 Вести з консолі строку зі слів (або скористайтеся константою). Напишіть код, який визначить кількість кількість слів, в цих даних.

# вывожу количество уникальных слов

str_request = str(input())

print(len(set(str_request.split())))



# 3 Існує ліст з різними даними, наприклад lst1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum'].
# Напишіть механізм, який сформує новий list (наприклад lst2), який би містив всі числові змінні, які є в lst1.
# Майте на увазі, що данні в lst1 не є статичними можуть змінюватись від запуску до запуску.

list1 = ['1', '2', 3, True, 'False', 5, '6', 7, 8, 'Python', 9, 0, 'Lorem Ipsum', 9.0, 5.6]

list2 = []

# добавляю в list2 числа int и float
for i in list1:
    if type(i) is int:
        list2.append(i)
    elif type(i) is float:
        list2.append(i)

print(list1)
print(list2)


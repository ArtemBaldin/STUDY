import random
import json
from datetime import datetime

'''
1 Создать файл, в нем написать текст.
Считать данные с файла и вывести в консоль
Считать данные с этого же файла и записать в новый файл
Считать данные с этого же файла, преобразовать (любые операции)
и записать в этот же файл без
'''
print("\nTask 1\n")

questions_list = ["Name", "Surname", "City"]
with open("questions.txt", "wt") as f1:
    f1.write(str(questions_list))
# считаем, создал файл и написал текст в файле.

with open("questions.txt") as data:
    print(data.read())

with open("questions.txt", "rt") as date, \
        open("questions_list_todo.txt", "w+") as file:
    file.write(date.read())
# записал данные из старого файла в новый.

print("")

with open("questions_list_todo.txt", "r+") as data:
    list_q = data.read()
    
list_q = list_q.replace(" ", "")
list_q = list_q.replace("'", "")
list_q = list_q[1:-1].split(",")

with open("questions_list_todo.txt", "wt") as file:
    for i in range(len(list_q)):
        file.write(list_q[i] + ": \n")

with open("questions_list_todo.txt", "rt") as data:
    print(data.read())
# преобразовал данные и записал их в тот-же файл

'''
2 Написать программу, которая откроет файл \
questions.json и после
ответов на вопросы, запишет их назад в этот же файл. \
Файл тоже нужно закинуть будет
'''
print("\nTask 2\n")

with open("questions.json", "r") as file:
    data = json.load(file)

for value_1st in data.values():
    for value_2nd in value_1st:
        list_key_value2 = list(value_2nd.keys())
        print(value_2nd[list_key_value2[0]])
        value_2nd[list_key_value2[1]] = input(f"{list_key_value2[1]}: ")

with open("questions.json", "w+") as file:
    file.write(json.dumps(data))

'''
3 Угадай число
Рандомное число можно сделать через модуль random
Диапазон 1 - 50
Попыток 10 (можно менять)
Рандомите число из диапазона,
запрашиваете число у юзера, валидируя его,
сравниваете, если угадал - завершаеться программа,
ксли нет снова спрашиваете число.
Если юзер не вложился в количество попыток -
завершаеете ее с сообщением что попыток больше нет
'''
print("\nTask 3 & 4\n")


def attempts_save(num_rand, count):
    DATA = {
        'Number': num_rand,
        'Attemp': count,
        'Date': str(datetime.now())
    }
    with open("attempts.json", "w+") as file:
        json.dump(DATA, file)


# функция для 4го задания

range_min, range_max = 1, 50
attempts_all = 10
num = random.randint(range_min, range_max)
count_attempts = 1

print(f"Enter any digit in range from {range_min} to {range_max}.\n")

while count_attempts < attempts_all + 1:
    # check = str(random.randint(1,50))
    # print(f"Input digit: {check}")
    # оставил для быстрой проверки

    check = input("Enter digit: ")

    if not check.isdigit():
        print("Error: Input isn\'t digit.\nProgram interrupted.")
        break
    else:
        check = int(check)
    if check == num:
        print("You guess the number. Congratulations!!!")
        attempts_save(num, count_attempts)
        break
    else:
        if count_attempts == attempts_all:
            print("\nNo more attempts.\nGame over.\n")
            print(f"\nThe number was: {num}")
            break
        elif check > range_max:
            # можно допилить отрицательные числа.

            print("\nEntered digit is not in allowed range.\
            \nIt counts as an attempt.\nTry again.\n")
        else:
            print("Try again.\n")
    count_attempts += 1

'''
4 Сохраним последний успешный запуск
Нужно записать в json файл данные о последней \
удачной попытке угадать число из задачи 3.
В файле должны быть:
 - число
 - номер попытки
 - дата записи в файл (можно посмотреть такое в cw.py)
'''

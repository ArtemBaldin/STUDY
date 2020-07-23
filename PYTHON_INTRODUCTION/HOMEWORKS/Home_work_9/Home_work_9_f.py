"""
1
Input: Feb 12 2019 2:41PM
Output: 2019-02-12 14:41:00
Функция принимает строку (пример - Input) и возвращает строку (пример - Output)
"""
print ("Task_1\n")
import datetime

def date_transform_format (date_string):
    return datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print (date_transform_format("Feb 12 2019 2:41PM"))

"""
2
Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""
print("\nTask_2\n")
def is_prime (num):
    increment_num=3
    if num<2:
        return False
    while increment_num < num:
            if num%increment_num==0 or num%2==0:
                return False
            increment_num +=2
    return True
    
   
digit_to_check=1000000
for i in range (100):
    if is_prime(digit_to_check)==True:
        print (f"{i} - {digit_to_check} - {is_prime(digit_to_check)}")
    digit_to_check +=1


"""
3
Напишите функцию, которая принимает 1 аргумент (строка) и выполняет следующие действия на каждую из букв строки:
i - инкремент (+1)
d - дикремент (-1)
s - возведение в квадрат
o - добавить число в результативный список
остальные буквы игнорируются
Исходное число = 0
Результативный список = []
Вернуть результативный список
parse("iiisdoso")  ==>  [8, 64]
"""
print("\nTask_3\n")

def parse_str(str_symb):
    num=0
    res=[]
    for symb in str_symb:
        if symb=="i":
            num += 1
        elif symb=="d":
            num -=1
        elif symb=="s":
            num=num**2
        elif symb == "o":
            res.append(num)
        
    return res
    
to_do="iiisdoso"

print(parse_str(to_do))
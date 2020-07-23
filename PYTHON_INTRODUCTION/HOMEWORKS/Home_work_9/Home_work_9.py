import datetime
#from datetime import datetime

"""
1
Input: Feb 12 2019 2:41PM
Output: 2019-02-12 14:41:00
Функция принимает строку (пример - Input) и возвращает строку (пример - Output)
"""
# datatime.date (y, m, d)
# datetime.date.today()

# a = datetime.date(2012, 7, 21)
# print(a.year)
# print(a.month)
# print(a.day)

'''
a = datetime.time(12, 18, 35, 5867)
print(a)
print(type(a))

a = datetime.time(23, 5, 30)
b = datetime.time(7, 26)
c = datetime.time(21)
print(a)
print(b)
print(c)

print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)

c = datetime.datetime(2017, 7, 18, 4, 52, 33, 51204)
print(c)

a = datetime.datetime.today()
b = datetime.datetime.now()
print(a)
print(b)

a = datetime.datetime.today().strftime("%d.%m.%Y")
b = datetime.datetime.today().strftime("%H:%M:%S")
print(a)
print(b)

08.11.2018
11:41:04

Формат	Значение
%a	название дня недели в сокращенном виде
%A	название дня недели в полном виде
%w	номер дня недели в виде целого числа
%d	номер дня месяца в виде целого числа
%b	название месяца в сокращенном виде
%B	название месяца в полном виде
%m	номер месяца в числовом представлении
%y	номер года без столетия
%Y	номер года в полном представлении
%H	количество часов в 24-часовом формате
%I	количество часов в 12-часовом формате
%p	до полудня или после полудня в 12-часовом формате
%M	количество минут в виде целого числа
%S	количество секунд в виде целого числа
%f	количество микросекунд в виде целого числа
%z	часовой пояс в формате UTC
%Z	название часового пояса
%j	номер дня в году
%U	номер недели в году, если считать с воскресенья
%w	номер недели в году, если считать с понедельника
%c	местное представление даты и времени
%x	местное представление даты
%X	местное представление времени
%%	символ процента

a = datetime.datetime(2015, 3, 27, 8, 12, 24, 34574)
print(a.year)
print(a.month)
print(a.day)
print(a.hour)
print(a.minute)
print(a.second)
print(a.microsecond)

from datetime import datetime, date, time
a = date(2015, 3, 19)
b = time(2, 10, 43)
c = datetime.combine(a, b)
print(c)

'''

a=date_input = "Feb 12 2019 2:41PM"
#a=date_input = "Feb 12 2019"
# Output: 2019-02-12 14:41:00

#print(str(datetime.date(2020, 12, 10)))
print('datetime.date.today()')

#c=datetime.datetime.today().strftime("%d.%m.%Y")
#d=datetime.datetime(2019, 11, 10, 14, 41)
#d=d.strftime("%b %d %Y %I:%M%p")

#print (d)

aa= datetime.datetime.strptime(a, "%b %d %Y %I:%M%p")
d=aa.strftime("%Y-%m-%d %H:%M:%S")

print(aa)
print(d)

# strftime(%b %d %Y)

def date_transform_format (date_string):
    return datetime.datetime.strptime(date_string, "%b %d %Y %I:%M%p")

print (date_transform_format("Feb 12 2019 2:41PM"))


"""
2
Напишите функция is_prime, которая принимает 1 аргумент (число) и возвращает True, если число простое, иначе False
Простое число - это число, которое делится без остатка только на себя и на 1
"""
def is_prime(num):
    pass
 
def fff(n):  
    d = 2
    while d * d <= n and n % d != 0:
        d += 1
    return d * d > n   
    
check_num=2
print("t")
print(check_num%2)
print(check_num%3)
print("t")
print(is_prime(check_num))

print(fff(check_num))



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
    
x="iiisdoso"

print(parse_str(x))

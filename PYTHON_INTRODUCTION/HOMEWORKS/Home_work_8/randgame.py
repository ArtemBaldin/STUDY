import random
import json
from datetime import datetime

def attempts_save (num_rand, count):
	DATA= {
	   'Number': num_rand,
	   'Attemp': count,
       'Date': str(datetime.now())
	  }
	with open ("attempts.json", "w+") as file:
			json.dump (DATA, file)

range_min , range_max = 1, 50
attempts_all = 10
num = random.randint (range_min, range_max)
count_attempts = 1

print (f"Enter any digit in range from {range_min} to {range_max}.\n")

while count_attempts<attempts_all+1:
	check = str(random.randint(1,50))
	print(f"Input digit: {check}")
#	check= input ("Enter digit: ")

	if not check.isdigit():
		print ("Error: Input isn\'t digit.\nProgram interrupted.")
		break
	else:
		check = int(check)
	if check==num:
		print("You guess the number. Congratulations!!!")
		attempts_save(num, count_attempts)
		break
	else:
			if count_attempts==attempts_all:
				print("\nNo more attempts.\nGame over.\n")
				print(f"\nThe number was: {num}")
				break
			elif check>range_max:
				# можно допилить отрицательные числа.
				print("\nEntered digit is not in allowed range.\nIt counts as an attempt.\nTry again.\n")
				
			else:
				print("Try again.\n")
	count_attempts +=1






'''

3 Угадай число
Рандомное число можно сделать через модуль random
Диапазон 1 - 50
Попыток 10 (можно менять)
Рандомите число из диапазона, 
запрашиваете число у юзера, валидируя его, 
сравниваете, если угадал - завершаеться программа, 
ксли нет снова спрашиваете число.
Если юзер не вложился в количество попыток - завершаеете ее с сообщением что попыток больше нет
'''


'''
4 Сохраним последний успешный запуск
Нужно записать в json файл данные о последней удачной попытке угадать число из задачи 3.
В файле должны быть:
 - число
 - номер попытки
 - дата записи в файл (можно посмотреть такое в cw.py)
 '''
	
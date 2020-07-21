'''
1 Создать файл, в нем написать текст.
    Считать данные с файла и вывести в консоль
    Считать данные с этого же файла и записать в новый файл
    Считать данные с этого же файла, преобразовать (любые операции) и записать в этот же файл без
'''
print("--- 1.1")

questions_list=["Name", "Surname", "City"]
#f1 = open ("questions.txt", "wt" )
#f1.close()
#print(f1.closed)
with open ("questions.txt", "wt") as f1:
		f1.write(str(questions_list))
print (open("questions.txt").read()) # не знаю закрыт ли файл questions.txt
open("questions.txt").close

print("--- 1.2")

#print(str(questions_list))
#print("---")

#f1= open ("questions.txt", "rt" )
#print(f1.read())
#f1.close
#
with open("questions.txt", "rt") as date, open("questions_list_todo.txt", "w+") as file:
	file.write(date.read())
		
	
f2= open("questions_list_todo.txt", "rt")
print(f2.read())
f2.close
#
print("--- 1.3")

f2=open("questions_list_todo.txt", "r+")
list_q=f2.read()
#print(list_q[1:-1])
#list_q=list_q[1:-1].split(",")
list_q=list_q.replace(" ", "")
list_q=list_q.replace("'", "")
list_q=list_q[1:-1].split(",")
print(type(list_q))
print(list_q)

with open("questions_list_todo.txt", "wt") as file:
	for i in range(len(list_q)):
		file.write(list_q[i]+": \n")

f1=open("questions_list_todo.txt", "rt")
print(f1.read())
		

	




'''
2 Написать программу, которая откроет файл questions.json и после ответов на вопросы, запишет их назад в этот же файл. Файл тоже нужно закинуть будет
'''
import json
from datetime import datetime



print("--- 2")
dict_q={}
f1=open ("questions_list_todo.txt", "rt")
for i in f1:
	i=i.replace("\n", "")
	i=i.replace(" ","")
	i=(i[:-1])
	dict_q.setdefault(i, None)

print(dict_q)

print("---")

print ("read json")
f_js=open("questions1.json", "w+")
#f_js.write(json.dumps(dict_q))
json.dump(dict_q, f_js)
print(f_js.read())
print("off")
f_js=open("questions1.json", "r+")
#print(f_js.read())
#print(dict_q["Name"])
#print(f_js.items())
js_k=json.load(open("questions.json", "rt"))
#js_k=open("questions.json", "rt")
#print(js_k.keys())
print("---")
#print(js_k.values())
print("---")
#for i in js_k[i]:
#	print(i)
#	print("--")
#	js_k[i]=input(f"{i} : ")
#	print(js_k[i])
#	print(js_k[i])
#print(js_k)
#t1=js_k["questions"][1]

#pd_k=dict(js_k)
#print("pd_k")
#print(pd_k)
for z in js_k.values():
	#print(f"(z = {z}")
	for v in z:
		list_kk=list(v.keys())
	#	print(list_kk[])
		print(v[list_kk[0]])
		v[list_kk[1]]=input(f"{list_kk[1]}: ")

js_
	
		
		
		

#print (f)
		
	#	print(js_k[z][n]["q"])
#		print(f"v = {v}")
#	    	n+=1



#for i in js_k:
#	print(js_k[[i][c]][1]["q"])
#	c+=1
#	print(js_k[i][c])

#print(t1)
#print(type(t1))
#print(t1["q"])
#print(t1["answer"])



print("---2.2")
#f1=open ("questions_list_todo.txt", "rt")
#print (f1.readline())
#print (f1.readline())
#print (f1.readline())
	





#DATA= {
#     'name': 'Vitalii',
#     'age': 24,
#     'updated': str(datetime.now())
# }

#with open('test.json', 'w') as file:
#     json.dump(DATA, file, indent=4)
#
#with open('test.json', 'r') as file_to_read:
#     data = json.load(file_to_read)
#     print(data)

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
''''
1. Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12), и возвращающую время
года, которому этот месяц принадлежит (зима, весна, лето или осень).
'''
print ("--> 1")
def get_season(number):
   if int(number)==0:
   	season = ""
   else:
    	season_of_year = {"winter":(12,1,2),  "spring":(3,4,5), "summer":(6,7,8), "autumn":(9,10,11)}
    	for key in season_of_year.keys():
    		if number in season_of_year[key]:
    			season = key
   return season


print (get_season(3)) 
print ("")
# add more cases - What do U mean?
while mon:=str:
	mon=input("In which month do You want to take a vacation.\nType number of month: ")
	if mon.isdigit():
		mon=int(mon)
		break

print (f"\nYour vacation will be in {get_season(mon)}.\nGood choice." if get_season(mon)!="" else "\nNo vacation for You in this year. Ha-ha.\n")



"""
2. Реализовать функцию, которая принимает строку и расделитель и возвращает словарь {слово: количество повторений}
"""

print ("\n---> 2")
def converter(string, separator):
    value_dic={}
    for i in string.split(separator):
    	value_dic.setdefault (i, string.split(separator).count(i))
    return value_dic
    
my_str = input('String: ')
delimiter = input('delimiter: ')
if delimiter =="":
	print (f"--> delimiter by default = \"None\"")
	delimiter = None
	
print(converter(my_str, delimiter))


'''
3. Написать функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения: периметр квадрата, 
площадь квадрата и диагональ квадрата.
'''

print ("\n--> 3")

def get_rectangle_data(a):
    a = float(a)
    per = a*4
    square = a**2
    diag = (2*a)**0.5
    return per, square, diag
    
print ("Input the length of one side of square." )

while side:= str:
	side = input("Side: ")
	if side.replace(".","").isdigit():
		side = float(side)
		break
	print ("\nSide of square, it\'s a length.\nInput a digit, please.")

print ("")
print (get_rectangle_data(side))
print ("")

print (f"The perimeter of the square is: {get_rectangle_data(side)[0]}\nThe area of the square is: {get_rectangle_data(side)[1]}\nThe diagonal of the square is: {get_rectangle_data(side)[2]}")
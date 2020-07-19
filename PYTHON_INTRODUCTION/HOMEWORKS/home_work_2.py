print (" First way solution\n ")

x = input(" Enter 3 digits: ")
sum_x = int(x[0]) + int(x[1]) + int(x[2])
print (f" Сумма цифр числа {x} равняется {sum_x} ")

###
print (" \n\n Second way solution\n ")

x = int(input( " Enter 3 digits: "))
a = x%10 
b = x%100//10
c = x//100 
sum_x = a + b + c
print (f" Сумма цифр числа {x} равняется {sum_x} ")
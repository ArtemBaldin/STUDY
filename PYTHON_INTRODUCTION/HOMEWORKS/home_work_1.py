print ("First way solution")

count_of_students = 6
apples = 50
print (f"Яблок у студента: {int(apples/count_of_students)}, в корзине: {apples % count_of_students}")

###
print ("\n\n")
print ("Second way solution")

st=count_of_students
a=apples
# для удобства
x = int(a / st) # студентов с яблоком
y = int(a-st*x) # остаток яблок
print ("Яблок у студента: {}, в корзине: {}". format (x, y))
# Simple way
print ("Input two integer didgits: ")
a=first_d = int(input ("Enter first digit: "))
b=second_d = int(input("Enter second digit: "))
for i in range (first_d, second_d+1):
	if i%5 == 0:
		print (i)
	
# just for interest
print("")
print ("Input two integer didgits: ")
list_d = [ ]
try:
	a=first_d =input("Enter first digit: ")
	a=int(a)
	try:
		b=input("Enter second digit: ")
		b=int(b)
	except:
		print("Wrong input. Reenter second digit.")
		b=input("Enter second digit: ")
except:
	print("Wrong input. Reenter first digit.")
	a=first_d =input("Enter first digit: ")

list_d.extend([a, b])
list_d.sort()
for i in range(list_d[0], list_d[1]+1):
	if i%5 == 0:
		print(i)
#if possible, write me, please, compact version of the code in second way or maybe U recommend me another logic.Thanks.

def multiply(x, y):
	print(f"{x} * {y} равно {int(x) * int(y)}")
	
def add(x, y):
	print(f"{x} + {y} равно {int(x) + int(y)}")

def divide(x, y):
	try:
		print(f"{x} / {y} равно {int(x) / int(y)}")
	except:
		print ("Ups, it's Division by Zero.\nBig no-no in mathematics!")
	
def substraction(x, y):
	print(f"{x} - {y} равно {int(x) - int(y)}")




x=y=""
ch_exit=""
math_do="-1"

print("To finish calculation print 'exit' in any field\n")
while ch_exit!="exit":
	
	while not x.isdigit() and x!="exit":
		x=input("Input 1st operand: ")
	if x=="exit":
		break
	while "+-/*".find(math_do)==-1:
		math_do=input("Input math operation: ")
	if math_do=="exit":
		break	
	while not y.isdigit() and y!="exit":
		y=input("Input 2st operand: ")
	if y=="exit":
		break
	
	if math_do=="*":
		multiply(x,y)
	elif math_do=="+":
		add(x,y)
	elif math_do=="/":
		divide(x,y)
	elif math_do=="-":
		substraction (x,y)
	else:
		print("Something wrong")
	
	math_do="-1"
	x=y=""
	ch_exit=""
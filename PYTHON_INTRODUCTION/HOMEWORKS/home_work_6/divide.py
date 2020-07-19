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
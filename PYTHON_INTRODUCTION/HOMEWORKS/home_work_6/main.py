from multiply import *
from add import *
from divide import *
from substraction import *


if __name__ == "__main__":
	
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
			if math_do =="":
				math_do="-1"
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

		print ("")
		math_do="-1"
		x=y=""
		ch_exit=""
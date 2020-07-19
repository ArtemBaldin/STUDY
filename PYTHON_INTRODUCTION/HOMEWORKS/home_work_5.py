def check (var_a, var_b):
	try:
		var_a = int(var_a)
		var_b = int(var_b)
		if var_a==var_b:
			result = '"="'
		elif var_a>var_b:
			result = '">"'
		elif var_a<var_b:
			result = '"<"'
	except:
		if type (var_a)==str or type(var_b)==str:
			result = '"str"'
	return f"Result is: {result}"
	
a=input("First : " )
b=input("Second: ")	
print(check(a,b))

#
def func(var_a, var_b):
  if type(var_a) == str or type(var_b) == str:
    print('str')
  elif var_a > var_b:
    print('>')
  elif var_a == var_b:
    print('=')
  elif var_a < var_b:
    print('<')
print("-->")

func(5, 7)
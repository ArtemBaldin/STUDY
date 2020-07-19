# That was intresting)))
import sys
def if_ru_in_text (text_):
	ru_a="а, б, в, г, д, е, ё, ж, з, и, й, к, л, м, н, о, п, р, с, т, у, ф, х, ц, ч, ш, щ, ъ, ы, ь, э, ю, я"
	ru_a=ru_a.replace("," " ", "")
	ru_a=list(ru_a)
	ch_text=0
	for i in range(len(ru_a)):
		ch_text +=text_.count(ru_a[i])
	return ch_text


var_string = "hApPyHalLOweEn!"
print("Counting of vowels in string. Only in English.\n")
print("You can input your own string or use defaul option.")
print (f"\nDefault string is: {var_string}.\n")
print("Press: \n1- To input own string \n2- To use default string.")
try:
	x= int(input("Input: "))
	while x!=1 and x!=2:
		x=int(input("Input right number: "))
	if x==1:
		var_string=input ("Your string is: ")
		while if_ru_in_text (var_string)>0:
			print("\nВы ввели Русские буквы.					\nInput text in English.\n")
			var_string=input ("Your string is: ")	
except:
	print ("\nWrong symbol.")
	sys.exit("Program interrupted")
	


#print(f"\nnYour string is: {var_string}")


print("\nFirst way solution.\n-------------------")
#var_string = "hApPyHalLOweEn!"
#print(f"Your string: {var_string}")
var_string = var_string.lower()
vowels_list = "aeiou"
counting_vowels = 0
for i in vowels_list:
	for k in var_string:
		if i == k:
			counting_vowels += 1
print(f"Total vowels in the string = {counting_vowels}")
###


#Second variant
print("\n\nSecond way solution.\n--------------------")
#var_string = "hApPyHalLOweEn!"
var_string= var_string.lower()
vowels_list='a', 'e', 'i', 'o', 'u'
vowels_list=list(vowels_list)
counting_vowels=0
for i in range(len(vowels_list)):
	counting_vowels +=var_string.							count(vowels_list[i])
print(f"Total vowels in the string = {counting_vowels}")




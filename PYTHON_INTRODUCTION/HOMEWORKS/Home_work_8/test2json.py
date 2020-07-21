import json

file_q = json.load(open("questions.json", "rt"))
for value_1st in file_q.values():
	for value_2nd in value_1st:
		list_key_value2 = list (value_2nd.keys())
		print (value_2nd[list_key_value2[0]])
		value_2nd[list_key_value2[1]] = input (f"{list_key_value2[1]}: ")

with open ("questions.json", "w+") as file:
	file.write (json.dumps(file_q))
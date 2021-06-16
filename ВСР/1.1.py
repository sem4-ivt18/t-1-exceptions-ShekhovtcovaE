import json

def main():
	di = enter_dict()
	print('Enter the name of the file')
	new_file = input()
	file = open_file(new_file, di)

def  open_file(new_file, di):
	try:
		with open(new_file, "w+") as jFile:
			data = json.dump(di, jFile)
	except NameError as e:
		raise FileNotFoundError
	else:
		return data
	
	

def enter_dict():
	keyboard = 'Y'
	di = {}
	while keyboard == 'y' or keyboard == 'Y':
		print('Enter the key')
		key = input()
		print('Enter the value')
		value = input()
		print('Enter the type of the value str/int/float')
		type_of_value = input()
		types = ['int', 'str', 'float']

		if type_of_value == 'int':
			try:
				value = int(value)
			except:
				raise TypeError
		if type_of_value == 'float':
			try:
				value = float(value)
			except:
				raise TypeError
		
		assert(type_of_value in types), 'Wrong type'
		
		di.update({key: value})
		print('Do you want to continue? Y/N')
		keyboard = input()
	print(di)
	return di


main()

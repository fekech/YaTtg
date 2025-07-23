import os

# Проверка на существование файла
def FileCheck(filename,):
	try:
		if os.path.exists(filename):
			return False
		else:
			return True
	except:
		gui.AddObjectToWidget('file: {filename} is not found')

# Создание файла с меткой перезаписи
def FileCreate(filename='none.txt',data='none',):
	try:
		with open(filename,'w+') as file:
			file.write(data)
		gui.AddObjectToWidget('Create file {filename} succesfull ')
	except:
		gui.AddObjectToWidget('Create file {filename} have a ERROR')

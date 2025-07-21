import os

# Проверка на существование файла
def FileCheck(filename,lg):
	try:
		if os.path.exists(filename):
			return True
		else:
			return False
	except:
		lg.error('file: {filename} is not found')

# Создание файла с меткой перезаписи
def FileCreate(filename='none.txt',data='none',lg=None):
	try:
		with open(filename,'w+') as file:
			file.write(data)
		lg.info('Create file {filename} succesfull ')
	except:
		lg.error('Create file {filename} have a ERROR')

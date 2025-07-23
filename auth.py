import json, os
import init, gui

def UploadDb(ID,lg,pas):
	data = {"login":lg,"password":pas}
	if init.FileCheck(os.getcwd()+chr(92)+"data"+chr(92)+'users'+chr(92)+str(ID)+'.json'):
		with open(os.getcwd()+chr(92)+"data"+chr(92)+'users'+chr(92)+str(ID)+'.json',"w", encoding="utf-8") as js:
			json.dump(data,js,indent=4)
			print('work')
	else:
		gui.AddObjectToWidget('Users is already adding!')

def LoadDb(ID):
	with open(os.getcwd()+chr(92)+"data"+chr(92)+'users'+chr(92)+str(ID)+'.json', "r", encoding="utf-8") as file:
		data = json.load(file)
		return data
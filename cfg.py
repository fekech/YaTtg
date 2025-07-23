import configparser
import os
import gui

config = configparser.ConfigParser()

def CfgCreate():
	try:
		config.add_section('Settings')
		config.set('Settings', 'width', '480')
		config.set('Settings', 'height', '60')
		with open(os.getcwd()+chr(92)+'data'+chr(92)+'settings.ini', 'w') as config_file:
			config.write(config_file)
		gui.AddObjectToWidget('Create config succesfull ')
	except:
		gui.AddObjectToWidget('Create config have a ERROR')

def CfgRead(collection,key):
	try:
		return config.read(collection,key)
	except:
		gui.AddObjectToWidget('can not read config files')
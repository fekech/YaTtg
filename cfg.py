import configparser
import os

config = configparser.ConfigParser()

def CfgCreate(lg):
	try:
		config.add_section('Settings')
		config.set('Settings', 'width', '420')
		config.set('Settings', 'height', '630')
		with open(os.getcwd()+chr(92)+'data'+chr(92)+'settings.ini', 'w') as config_file:
			config.write(config_file)
		lg.info('Create config succesfull ')
	except:
		lg.error('Create config have a ERROR')

def CfgRead(collection,key,lg):
	try:
		return config.read(collection,key)
	except:
		lg.error('can not read config files')
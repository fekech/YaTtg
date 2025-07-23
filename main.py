import init, cfg, gui
import threading, os, time

cfg.CfgCreate()
gui_theard = threading.Thread(target=gui.LoadGui)
gui_theard.start()

while True:
	time.sleep(0.6)
	if gui_theard.is_alive():
		pass
	else:
		os._exit(0)
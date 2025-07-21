from init import *
from cfg import *
from gui import *
import logging

logging.basicConfig(level=logging.INFO, filename=os.getcwd()+chr(92)+'logs'+chr(92)+"yattg.log", filemode="w", format="%(asctime)s %(message)s")

CfgCreate(logging)

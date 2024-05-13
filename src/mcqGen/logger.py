import logging
from datetime import datetime
filename=f"{datetime.now().strftime('%m-%d-%Y-%H-%M-%S')}.log"
import os
dirs=os.path.join(os.getcwd(),"logs")
os.makedirs(dirs,exist_ok=True)
fpath=os.path.join(dirs,filename)
logging.basicConfig(level=logging.INFO,filename=fpath,format="[%(asctime)s] %(lineno)s %(name)s -%(levelname)s %(message)s")
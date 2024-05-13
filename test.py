# from src.mcqGen.logger import logging
#logging.info("this is the first log using logging")
from src.mcqGen.utils import read_file

f=open(r"C:\\Users\\krish\\Downloads\\file.pdf","r")
print(read_file(f))
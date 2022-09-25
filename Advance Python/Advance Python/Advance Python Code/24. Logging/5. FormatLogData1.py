from logging import *
basicConfig(filename="logfile.log", level=DEBUG, filemode='w', format='%(asctime)s -- %(message)s')
debug("This is Debug")
info("This is Info")
warning("This is Warning")
error("This is Error")
critical("This is Critical")
from logging import *
LOG_FORMAT = '%(asctime)s // %(message)s // %(lineno)d' 
basicConfig(filename="logfile.log", level=DEBUG, filemode='w', format=LOG_FORMAT)
debug("This is Debug")
info("This is Info")
warning("This is Warning")
error("This is Error")
critical("This is Critical")
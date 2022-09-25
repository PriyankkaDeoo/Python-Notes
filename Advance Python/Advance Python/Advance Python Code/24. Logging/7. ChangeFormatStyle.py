from logging import *
LOG_FORMAT = '{lineno} *** {name} *** {asctime} *** {message}' 
basicConfig(filename="logfile.log", level=DEBUG, filemode='w', style='{', format=LOG_FORMAT)
debug("This is Debug")
info("This is Info")
warning("This is Warning")
error("This is Error")
critical("This is Critical")
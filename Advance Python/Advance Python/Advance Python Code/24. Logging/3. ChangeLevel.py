from logging import *
basicConfig(filename="logfile.log", level=DEBUG)
debug("This is Debug")
info("This is Info")
warning("This is Warning")
error("This is Error")
critical("This is Critical")
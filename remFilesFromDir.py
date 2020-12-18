import os, sys
import datetime

from filefuncs import *

if __name__=="__main__":
    # command line: python directory.py [path] [days]
    argv = sys.argv
    src = argv[1]
    days = 999999999
    if len(argv)>2:
        days = int(argv[2])
    
    rem_files_from_dir (src, days)


# copies all files in directory Argv1 to directory Argv2 newer than [Argv3] days old (all files if Argv3 is not set)
# python copydir [src dir] [tgt dir] [days]

from shutil import *
import os, sys, datetime 

from filefuncs import *

if __name__ == "__main__":
    argv = sys.argv
    src = argv[1]
    tgt = argv[2]
    days = 999999999
    if len(argv)>3:
        days = int(argv[3])
    
    copy_dir (src, tgt, days)
    
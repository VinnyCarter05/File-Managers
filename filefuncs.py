from shutil import *
import os, sys, datetime 

def listdir_with_ext (path=".", ext = ""):
    filelist = []
    for file in os.listdir(path):
        if file.lower().endswith(ext):
            filelist.append([os.path.join(path,file), os.path.getmtime(os.path.join(path,file))])
    return sorted_list_by_col (filelist)

def sorted_list_by_col (lst, col=0, reverse = False):
    sorted_list = sorted(lst, key = lambda x: x[col], reverse = reverse)
    return (sorted_list)

def copy_dir (srcdir, tgtdir, days = 999999999):
    src_files = listdir_with_ext (path=srcdir)
    for file, mtime in src_files:
        if (datetime.datetime.now()-datetime.datetime.fromtimestamp(mtime))<datetime.timedelta(days = days):
            try:
                copy2(file, tgtdir)
            except:
                print ("error")

def rem_files_from_dir (srcdir, days = 9999999):
    # remove files from dir > [days] days old
    src_files = listdir_with_ext (path=srcdir)
    for file, mtime in src_files:
        if (datetime.datetime.now()-datetime.datetime.fromtimestamp(mtime))>datetime.timedelta(days = days):
            try:
                os.remove(file)
            except:
                print ("error")

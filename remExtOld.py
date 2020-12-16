import os, sys
import datetime


def listdir_with_ext (path=".", ext = ""):
    filelist = []
    for file in os.listdir(path):
        if file.lower().endswith(ext):
            filelist.append([file, os.path.getmtime(os.path.join(path,file))])
    return sorted_list_by_col (filelist)

def sorted_list_by_col (lst, col=0, reverse = False):
    sorted_list = sorted(lst, key = lambda x: x[col], reverse = reverse)
    return (sorted_list)

if __name__=="__main__":
    # command line: python directory.py [path] [ext] [#days]
    remlist = []
    path = "."
    ext = ""
    try:
        path = sys.argv[1]
    except:
        pass
    try:
        ext = sys.argv[2]
        if ext == "*":
            ext = ""
    except: 
        pass
    try:
        days = int(sys.argv[3])
    except:
        pass
    filelist = listdir_with_ext(path, ext)
    # 
    for file, date in filelist:
        if (datetime.datetime.now() - datetime.datetime.fromtimestamp(date))>datetime.timedelta(days=days):
            remlist.append (os.path.join(path, file))
    if len(remlist)>0:
        print ("Found the following files:\n", remlist)
        ans = input("Are you sure want to delete these files permanently? (Y/n)")
        if ans == "Y":
            for file in remlist:
                os.remove(file)
            input("Removed. Press ENTER to close")
    else:
        input ("No Files found.  Press ENTER to close")
            
import os, sys
import datetime



def listdir_with_ext (path=".", ext = ""):
    PDFlist = []
    for file in os.listdir(path):
        if file.lower().endswith(ext):
            PDFlist.append([file, os.path.getmtime(os.path.join(path,file))])
    return sorted_list_by_col (PDFlist)

def sorted_list_by_col (lst, col=0, reverse = False):
    sorted_list = sorted(lst, key = lambda x: x[col], reverse = reverse)
    return (sorted_list)

if __name__=="__main__":
    # command line: python directory.py [path] [ext]

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
    PDFlist = listdir_with_ext(path, ext)
    # 
    for file, date in PDFlist:
        print (os.path.join(path,file),datetime.datetime.fromtimestamp(date),(datetime.datetime.now() - datetime.datetime.fromtimestamp(date))>datetime.timedelta(days=days))
        
        # datetime.datetime.fromtimestamp(date))
    
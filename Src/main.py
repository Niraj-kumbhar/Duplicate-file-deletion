from genericpath import isfile
import hashlib
import os
from posixpath import join
import sys

def checkPath(upath):
    """ 
    check path and set path

    this function checks if path given by user exists or not
    and if user doesn't provided anything current working directory path will get selected 
    """
    if upath == '':   
                           
        upath = os.getcwd()
        print('As no path given, selected currect directory for scanning\n')

    if not os.path.exists(upath):
        print('\n****Path entered does not exists!!!!!****')
        exit()

    return upath
    
    
def readdata(file):
    """
    Read file in binary

    this function will read file in binary and will return file in binary and file full path 
    """
    #fullpath = os.path.join('/home/groot/my code/first/target',file)
    with open(file, 'rb') as f:
        fread = f.read()
        fname = f.name
    return fread, fname

def check_Duplicate():
    """
    Check duplicate files

    this function will convert file in hashed, will remove duplicate files and return the duplicate files list 

    """

    unique = [] #for storing unique files in Dir
    flist = [] #for storing duplicate files in Dir
    

    for file in files:
        
        fpath = os.path.join(u_path, file)
        fdata, fname= readdata(fpath)

        hashed = hashlib.md5(fdata)
        #print(hashed.hexdigest())
        if hashed.hexdigest() in unique:
            flist.append(fname)
            print('{} .....found!!'.format(fname))
            os.remove(file)
        else:
            unique.append(hashed.hexdigest())
    return flist


u_path = checkPath(input("Enter path: ")) #take folder path from user
files = [x for x in os.listdir(u_path) if isfile(join(u_path,x))] #we will store all files present in folder in list
print('Scanning started......\n')
duplicate = check_Duplicate()

print("\nScan Completed\n{} Duplicate files Removed!!".format(len(duplicate)))

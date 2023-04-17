import os
import dropbox
from dropbox.files import WriteMode 

class ShiftData:
    def __init__(self,access_token):
        self.access_token = access_token
    def uploadfiles(self,fromfile,tofile):
        dbx = dropbox.Dropbox(self.access_token)
        for root, directries, files in os.walk(fromfile):
            for filename in files:
                localpath = os.path.join(root,filename)
                rtpath = os.path.relpath(localpath,fromfile)
                dbxpath = os.path.join(tofile,rtpath)
                with open(localpath, 'rb') as f:
                    dbx.ulfiles(f.read(),dropbox_path,mode = WriteMode("Overwrite"))

def main():
    access_token = ''
    
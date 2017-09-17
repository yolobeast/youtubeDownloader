import subprocess
import tkinter as tk
from tkinter import filedialog
import os
import json

    
def converter():    
    root = tk.Tk()
    root.withdraw()
    try:
        file_path = filedialog.askopenfilename()
        path,filename = os.path.split(file_path)
        print("file name : ", filename)

        listof_id = []

        #try :
        with open('store.txt', 'r') as f:
            listof_id = f.read().splitlines();
        #except :
         #   print ("the file is not there")



        filena, ext = filename.split(".")
        idlsi = []
        title = []
        for id in listof_id:
            idlsi,title = id.split("=")
            print ("id asdfasdfasdf : "+idlsi + ' ' +filena)
            if filena == idlsi: 
               outputname = title;
              

        try:
            x = subprocess.call('mkdir Music')
            p = subprocess.call('ffmpeg.exe -i '+ 'video\\'+filename + ' ' + 'Music\\'+outputname + '.mp3')
        except:
            print("the file doesnt exist asfsfsadfsdf")
    except:
        print ("you didnt choose a file")

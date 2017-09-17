##from pytube import YouTube

##yt = YouTube("https://www.youtube.com/watch?v=ayBuBxmuTEo")

##print(yt.get_videos())

##print(yt.filename)

from __future__ import unicode_literals
import youtube_dl
import os
import json
import subprocess


class MyLogger(object):
    def debug(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)


def my_hook(d):
    if d['status'] == 'finished':
        print('Done downloading')


def download(link):        
    ydl_opts = {
        #'format' : 'video/',
        'outtmpl': '\\video\%(id)s',
        'logger': MyLogger(),
        'progress_hooks': [my_hook]}

    try :
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            meta = ydl.extract_info(
               link , download=False) 
            ydl.download([link])
            
        title = (meta['title'])
        idforvid = (meta['id'])
        ti = title.replace(" ",'')
        print ('title : ' ,ti+'.webm')
        print ('id : ', meta['id'])
        inputnam = (ti+'.webm')
        outputnam = (ti+'.mp3')

        with open('store.txt', 'a+') as f:
            f.write(idforvid + '=' + ti + '\n')

        print ('mv '+ 'video\\' +idforvid + ' ' + 'video\\'+idforvid + '.mp4')
        p = subprocess.call('mv '+ 'video\\' +idforvid + ' ' + 'video\\'+idforvid + '.mp4')
        return(1)    
    except :
        return(0)


    
    
   

    # with open('store.json', 'a+') as f:
        # try:
            # data = json.load(f)
        # # if the file is empty the ValueError will be thrown
        # except ValueError:
            # data = {}
            
    # with open('store.json', 'a+') as f:
        # data[idforvid] = ti
        # json.dump(data, f)
        
    


       
        #import ffmpeg
    #(ffmpeg
    #    .input(path + inputnam)
    #    .hflip()
    #    .output(outputnam)
    #    .run()
    #)



           
    #print ('title : %s' ,(meta['title']))
    
    

    



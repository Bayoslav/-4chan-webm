import requests 
import bs4 as bs 
import moviepy,wget
import imageio, subprocess
imageio.plugins.ffmpeg.download()
#f#rom moviepy.editor import VideoFileClip, concatenate_videoclips
import ffmpeg


f = open("1523214516999.webm","r")

fe = open("1523214045678.webm","a")


dd = str(f.read())
fe.write(dd)

f.close()

fe.close()
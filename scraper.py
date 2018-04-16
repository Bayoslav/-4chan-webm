import requests 
import bs4 as bs 
import moviepy,wget
import imageio, subprocess
imageio.plugins.ffmpeg.download()
#f#rom moviepy.editor import VideoFileClip, concatenate_videoclips
import ffmpeg
imageio.plugins.ffmpeg.download()
url = input("Enter the thread link: ")
r = requests.get(url)
#ffmpeg -i "concat:input1.ts|input2.ts|input3.ts" -c copy output.ts
stringic = ""

soup = bs.BeautifulSoup(r.text,'lxml')
#http://i.4cdn.org/wsg/1521166840714.webm
divs = soup.find_all('div',class_='fileText')
cliplist = []
i = 0
for i in range(0,len(divs)):
    href = divs[i].find('a')
    link = href.get('href')
    #print(link[2:])
    if(link[-4:]=='webm'):
        link = 'http:' + link
        #print(link)
        file = wget.download(link)
        emp4fiel = file[:-4] + "webm"
        print(file)
        print(emp4fiel)
        cmd = "ffmpeg -i " + file + " -c:v libvpx-vp9 -crf 30 -b:v " + emp4fiel
        subprocess.call(cmd) 
        #rint(file)
        pravoime = "file " + emp4fiel
        cliplist.append(pravoime)
            
#mp4box -add video1.mp4 -cat video2.mp4 -cat video3.mp4 output.mp4
f = open('names.txt','w') 
for item in cliplist:
      f.write("%s\n" % item)
#f.write(stringic)
name = input("What do you want to name your file?")

#print(stringic)
dd = " " + name + ".webm"
final_clip = "ffmpeg -f concat -i names.txt  -c:v libvpx-vp9 -crf 30 -b:v copy " + dd
print(final_clip)
f.close()
subprocess.call(final_clip)

#final_clip.write_videofile(name + '.webm')
    #if(link[-4:])
#print(r.text)

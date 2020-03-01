import playsound
import os
def list():
    for i in range(0,c):
        print(str(i) +  "." + b[i])

if "__name__"== "__main__":
    b = os.listdir(r"C:\Users\khaja\Music")
    c = len(b)
    print("Welcome to the music player")
    print("Songs list")
    list()


'''
def displayIntro():
    while(True):
        playsound.playsound(r"C:\khaja\Music\Believer.mp3",True)
displayIntro()
'''
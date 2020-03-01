import playsound
import os
import time
def intro():
    b = os.listdir(r"C:\Users\khaja\Music")
    c = len(b)
    for i in range(0,c):
        print(str(i) +  "." + b[i])
    select(b)
def introall():
    b = os.listdir(r"C:\Users\khaja\Music")
    c = len(b)
    for i in range(0,c):
        print(str(i) +  "." + b[i])
    print("Playing all....")
    time.sleep(5)
    too(c, b)
def too(c, b):
    for i in range(0, c):
        try:
            str2 = ''.join(r"C:\Users\khaja\Music\"")
            sn = str2.strip('"')
            print(sn)
            path1 = sn + b[i]
            print(path1)
            playsound.playsound(path1, True)
        except Exception as k:
            print("Can't play" + b[i] + "song")
            print("Playing the next song")
            print(k)
        finally:
            pass
        continue
def select(b):
    while ( True ):
        try:
            num = int(input("Which song do want to play:"))
            str1 = ''.join(r"C:\Users\khaja\Music\"")
            sn = str1.strip('"')
            print(sn)
            path1 = sn + b[num]
            print(path1)
            playsound.playsound(path1, True)
        except Exception as k:
            print("Can't play" + b[num] + "song")
            print(k)
            select(b)
take = int(input("Press 1 to play all and press 2 to go for normal"))
print("Welcome to the music player")
print("Songs list")
if take == 2:
    intro()
elif take == 1:
    introall()

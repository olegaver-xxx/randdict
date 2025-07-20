import os
import pathlib
from itertools import count
from dicts import vid, snd, pic, txt
# userpath = input("Укажи путь к директории")
userpath = "/home/melkor/Documents/"
folder = pathlib.Path(userpath)
objects = folder.iterdir()



def collect(self):
    objects_count = len(list(objects))
    print(objects_count)
    for obj in objects:
        ext = os.path.splitext(obj.name)[1]
        print(ext)
        if ext == self:
            print ("i find")


collect('.mp4')













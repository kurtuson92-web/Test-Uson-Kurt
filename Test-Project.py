import os
import shutil

dire = input("Enter folder Path ")

if os.path.exists(dire):
    files = os.listdir()
    img = 0
    vid = 0
    doc = 0
    oth = 0

else:
    print ("unknown directory")



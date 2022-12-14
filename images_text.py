import os

from function import *

path = 'E:\\Progress\\anicharts\\static\\images'
for file_name in os.listdir(path):
    name = dbf.find_one({'mid': int(file_name.split('.')[0])})['name']
    with open('E:\\Progress\\VideoHandle\\images.txt', 'a') as f:
        f.write(f"ani.recourse.loadImage(web+'images/{file_name.split('.')[0]}', '{name}');")

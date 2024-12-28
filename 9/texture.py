# 1 создадим модуль, который будет управлять всеми изображениями
from tkinter import PhotoImage

_frames = {}
def load(name, file_name):    # вызывать эту фукцию будем в модуле main

    image = PhotoImage(file=file_name)
    _frames[name] = image

def get(name):
    return _frames[name]
# def load_textures():
#     texture.load('WATER', '../img/water.png')
#     texture.load('BRICK', '../img/brick.png')
#     texture.load('CONCRETE', '../img/wall.png')
#

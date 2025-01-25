from units import Missle
import units
_missles = []
_canvas = None
def initialize(canvas):
    global _canvas
    _canvas = canvas
def fire(owner):
    m = Missle(_canvas,owner)
    _missles.append(m)
def update():
    start = len(_missles)-1
    for i in range(start,-1,-1):
        if _missles[i].is_destroyed():
            del _missles[i]
        else:
            _missles[i].update()



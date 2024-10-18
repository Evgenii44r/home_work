from hitbox import Hitbox
hb1 = Hitbox(0,100,100,100)
hb2 = Hitbox(90,100,100,100)
hb3 = Hitbox(190,100,100,100)
print(f'верхняя hb1: {hb1.top},'
      f'верхняя hb2: {hb2.top},'
      f'верхняя hb3: {hb3.top},')
print(f'нижния hb1: {hb1.bottom},'
      f'нижния hb2: {hb2.bottom},'
      f'нижния hb3: {hb3.bottom},')
print(f'лево hb1: {hb1.left},'
      f'лево hb2: {hb2.left},'
      f'лево hb3: {hb3.left},')
print(f'право hb1: {hb1.right},'
      f'право hb2: {hb2.right},'
      f'право hb3: {hb3.right},')
intersects= hb1.intersects(hb2)
intersects_3= hb2.intersects(hb3)
intersects_2= hb1.intersects(hb3)
print(intersects)
print(intersects_2)
print(intersects_3)

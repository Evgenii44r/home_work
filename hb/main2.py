from hitbox import Hitbox
hb1 = Hitbox(0,100,100,100)
hb2 = Hitbox(110,100,100,100)
hb3 = Hitbox(220,100,100,100)
print(f'верхняя hb1: {hb1.top},'
      f'верхняя hb2: {hb2.top},'
      f'верхняя hb3: {hb3.top},')
print(f'нижния hb1: {hb1.bottom},'
      f'нижния hb2: {hb2.bottom},'
      f'нижния hb3: {hb3.bottom},')
print(f'левая hb1: {hb1.left},'
      f'левая hb2: {hb2.left},'
      f'левая hb3: {hb3.left},')
print(f'правая hb1: {hb1.right},'
      f'правая hb2: {hb2.right},'
      f'правая hb3: {hb3.right},')
intersects = hb1.intersects(hb2)
intersects_2 = hb2.intersects(hb3)
print(intersects)
print(intersects_2)
*

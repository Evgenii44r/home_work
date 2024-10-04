from random import choice
student = input('Представьтесь')
try:
    level = int(input("Выберите уровень сложности 1 - 3:"))
except:
    level = 1
    print('Установлен уровень 1')
if level < 1 or level > 3:
    level = 1
    print('Установлен уровень 1')
print(f"Хорошо, {student}. Тебе викторнина по истории!")


questions = {
    1: [('В каком году началась великая отечественная война?''1941'),
        ("Кто был первым президентом США?""Джордж Вашнгтон")]

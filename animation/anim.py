import tkinter as tk
import random


# Базовый класс для объектов, которые могут падать
class FallingObject:
    def __init__(self, canvas, x, y, size, color, speed=2):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.speed = speed
        self.color = color
        self.id = self.canvas.create_oval(x - size // 2, y - size // 2, x + size // 2, y + size // 2,
                                          fill=self.color, outline="")

    # Метод для перемещения объекта вниз
    def fall(self):
        self.canvas.move(self.id, 0, self.speed)

    # Проверка, упал ли объект за пределы окна
    def is_out_of_bounds(self, height):
        bbox = self.canvas.bbox(self.id)
        return bbox[3] > height


# Класс для яблока, наследуемый от FallingObject
class Apple(FallingObject):
    def __init__(self, canvas, x, y, size=20, color="red", speed=2):
        super().__init__(canvas, x, y, size, color, speed)


# Класс для листа, также наследуемый от FallingObject
class Leaf(FallingObject):
    def __init__(self, canvas, x, y, size=15, color="green", speed=1):
        super().__init__(canvas, x, y, size, color, speed)


# Класс для дерева
class Tree(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()

        # Создание холста для отображения яблонь
        self.canvas = tk.Canvas(self, width=500, height=400, bg="white")
        self.canvas.pack()

        # Координаты дерева
        self.tree_x = 250
        self.tree_y = 100

        # Отображение дерева
        self.draw_tree()

        # Генерация случайных объектов (яблок и листьев)
        self.objects = []
        for _ in range(10):
            obj_type = random.choice([Apple, Leaf])
            obj = obj_type(self.canvas, self.tree_x + random.randint(-50, 50), self.tree_y, size=random.randint(15, 25))
            self.objects.append(obj)

        # Запуск цикла анимации
        self.animate()

    # Рисование дерева
    def draw_tree(self):
        self.canvas.create_rectangle(self.tree_x - 30, self.tree_y + 60, self.tree_x + 30, self.tree_y + 200,
                                     fill="brown")  # Ствол
        self.canvas.create_polygon(
            [self.tree_x - 80, self.tree_y + 40, self.tree_x + 80, self.tree_y + 40, self.tree_x, self.tree_y - 70],
            fill="green")  # Крона

    # Анимационный метод
    def animate(self):
        for obj in self.objects:
            obj.fall()  # Перемещение объекта вниз
            if obj.is_out_of_bounds(self.canvas.winfo_height()):
                self.canvas.delete(obj.id)  # Удаление объекта, когда он падает за пределы экрана
                self.objects.remove(obj)

        self.after(50, self.animate)  # Повторный вызов метода через 50 мс


if __name__ == "__main__":
    root = tk.Tk()
    app = Tree(master=root)
    app.mainloop()
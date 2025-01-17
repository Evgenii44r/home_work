import tkinter as tk


# Создаем класс для окна приложения
class App(tk.Tk):
    def __init__(self):
        super().__init__()

        # Настраиваем окно
        self.title("Пример анимации")
        self.geometry("500x300")

        # Создаем холст для рисования
        self.canvas = tk.Canvas(self, width=500, height=300)
        self.canvas.pack()

        # Создаем объект шарика
        self.ball = Ball(self.canvas)

        # Запускаем анимацию
        self.animate()

    def animate(self):
        # Перемещаем шарик
        self.ball.move()

        # Повторяем анимацию через 20 миллисекунд
        self.after(20, self.animate)


# Класс для шарика, наследуем от класса Canvas
class Ball(tk.Canvas):
    def __init__(self, canvas):
        self.canvas = canvas
        self.x = 250  # Начальная координата X
        self.y = 150  # Начальная координата Y
        self.r = 30  # Радиус шарика
        self.dx = 2  # Скорость перемещения по оси X
        self.dy = 2  # Скорость перемещения по оси Y

        # Рисуем шарик
        self.id = self.canvas.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill="blue",
            outline="black")

    def move(self):
        # Проверка границ окна
        if self.x + self.r >= 500 or self.x - self.r <= 0:
            self.dx *= -1
        if self.y + self.r >= 300 or self.y - self.r <= 0:
            self.dy *= -1

        # Обновляем координаты шарика
        self.x += self.dx
        self.y += self.dy

        # Перемещаем шарик на холсте
        self.canvas.move(self.id, self.dx, self.dy)


if __name__ == "__main__":
    app = App()
    app.mainloop()
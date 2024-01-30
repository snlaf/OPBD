import tkinter as tk

class AnimationApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Анимация")
        self.geometry("400x510")

        self.speed = 10

        self.canvas = tk.Canvas(self, width=400, height=400)
        self.canvas.pack()

        self.circle = self.canvas.create_oval(180, 180, 220, 220, fill="blue")

        self.up_button = tk.Button(self, text="Вверх", command=lambda: self.move_circle(0, -self.speed))
        self.up_button.pack(side=tk.TOP)

        self.down_button = tk.Button(self, text="Вниз", command=lambda: self.move_circle(0, self.speed))
        self.down_button.pack(side=tk.BOTTOM)

        self.left_button = tk.Button(self, text="Влево", command=lambda: self.move_circle(-self.speed, 0))
        self.left_button.pack(side=tk.LEFT)

        self.right_button = tk.Button(self, text="Вправо", command=lambda: self.move_circle(self.speed, 0))
        self.right_button.pack(side=tk.RIGHT)

        self.speed_scale = tk.Scale(self, from_=1, to=20, orient=tk.HORIZONTAL, command=self.update_speed)
        self.speed_scale.set(self.speed)
        self.speed_scale.pack(side=tk.BOTTOM, fill=tk.X)

    def move_circle(self, dx, dy):
        self.canvas.move(self.circle, dx, dy)
        self.after(100, lambda: self.move_circle(dx, dy))

    def update_speed(self, value):
        self.speed = int(value)

if __name__ == "__main__":
    app = AnimationApp()
    app.mainloop()
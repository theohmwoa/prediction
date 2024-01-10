import tkinter as tk
from tkinter import Button
from PIL import Image, ImageDraw


class ImageDrawApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Drawing App")

        self.canvas_width = 400
        self.canvas_height = 400
        self.background_color = 'black'
        self.pen_color = 'white'
        self.pen_size = 2

        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg=self.background_color)
        self.canvas.pack()

        self.image = Image.new("RGB", (self.canvas_width, self.canvas_height), self.background_color)
        self.draw = ImageDraw.Draw(self.image)

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

        save_button = Button(self.root, text='Save Image', command=self.save_img)
        save_button.pack()

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line((self.old_x, self.old_y, event.x, event.y),
                                    width=self.pen_size, fill=self.pen_color, capstyle=tk.ROUND, smooth=tk.TRUE)

            self.draw.line((self.old_x, self.old_y, event.x, event.y),
                           fill=self.pen_color, width=self.pen_size)

        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x = None
        self.old_y = None

    def save_img(self):
        file_path = 'drawing.png'
        self.image.save(file_path)
        print(f"Image saved as {file_path}")


root = tk.Tk()
app = ImageDrawApp(root)

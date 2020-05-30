from tkinter import *
from tkinter.colorchooser import askcolor


class Paint(object):

    DEFAULT_PEN_SIZE = 8.0
    DEFAULT_COLOR = 'black'

    def __init__(self):
        self.root = Tk()

        self.pen_button = Button(self.root, text='Pen', command=self.use_pen, bd = 6, bg = 'cyan')
        self.pen_button.grid(row=0, column=0)

        self.brush_button = Button(self.root, text='Brush', command=self.use_brush, bd = 6, bg = 'cyan')
        self.brush_button.grid(row=0, column=1)

        self.color_button = Button(self.root, text='Color', command=self.choose_color, bd = 6, bg = 'cyan')
        self.color_button.grid(row=0, column=2)

        self.eraser_button = Button(self.root, text='Eraser', command=self.use_eraser, bd = 6, bg = 'cyan')
        self.eraser_button.grid(row=0, column=3)

        self.c = Canvas(self.root, bg='white', width=500, height=800)
        self.c.grid(row=1, columnspan=4)

        self.b = Button(self.root, text="Draw oval", command=self.draw_oval, bd = 6, bg = 'cyan')
        self.b.grid(row=0, column=4)

        self.b1 = Button(self.root, text="Draw line", command=self.draw_line, bd=6, bg='cyan')
        self.b1.grid(row=0, column=5)

        self.b2 = Button(self.root, text="Draw Rect", command=self.draw_rect, bd=6, bg='cyan')
        self.b2.grid(row=0, column=6)

        self.choose_size_button = Scale(self.root, from_=1, to=10, orient=VERTICAL, bg='cyan')
        self.choose_size_button.grid(row=1, column=5)

        self.setup()

        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.line_width = self.choose_size_button.get()
        self.color = self.DEFAULT_COLOR
        self.eraser_on = False
        self.active_button = self.pen_button
        self.c.bind('<B1-Motion>', self.paint)
        self.c.bind('<ButtonRelease-1>', self.reset)
        #self.b.pack()
        #self.c.pack()
    def use_pen(self):
        self.activate_button(self.pen_button)

    def use_brush(self):
        self.activate_button(self.brush_button)

    def choose_color(self):
        self.eraser_on = False
        self.color = askcolor(color=self.color)[1]

    def draw_oval(self):
        self.c.create_oval(10, 10, 200, 200)

    def draw_line(self):
        self.c.create_line(300, 25, 70, 70)

    def draw_rect(self):
        self.c.create_rectangle(300, 25, 100, 100)

    def use_eraser(self):
        self.activate_button(self.eraser_button, eraser_mode=True)

    def activate_button(self, some_button, eraser_mode=False):
        self.active_button.config(relief=RAISED)
        some_button.config(relief=SUNKEN)
        self.active_button = some_button
        self.eraser_on = eraser_mode

    def paint(self, event):
        self.line_width = self.choose_size_button.get()
        paint_color = 'white' if self.eraser_on else self.color
        if self.old_x and self.old_y:
            self.c.create_line(self.old_x, self.old_y, event.x, event.y,
                               width=self.line_width, fill=paint_color,
                               capstyle=ROUND, smooth=TRUE, splinesteps=36)
        self.old_x = event.x
        self.old_y = event.y

    def reset(self, event):
        self.old_x, self.old_y = None, None


if __name__ == '__main__':
    Paint()

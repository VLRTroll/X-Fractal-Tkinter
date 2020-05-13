from tkinter import *

### Custom Constants
IMAGE_SIZE = 600
RECURSIVE_LEVELS = 6

BACKGROUND_COLOR = '#00ff00'
LINE_COLOR = 'brown'
LINE_SCALE = 1

### Recursive function
def XFractal(n, tam, x, y):
    if n > 0:
        x0 = x - tam/2
        x1 = x + tam/2

        y0 = y - tam/2
        y1 = y + tam/2

        line1 = canvas.create_line(x0, y0, x1, y1, fill = LINE_COLOR, width = LINE_SCALE*n)
        line2 = canvas.create_line(x0, y1, x1, y0, fill = LINE_COLOR, width = LINE_SCALE*n)

        XFractal(n-1, tam/2, x0, y0)
        XFractal(n-1, tam/2, x0, y1)
        XFractal(n-1, tam/2, x1, y0)
        XFractal(n-1, tam/2, x1, y1)

if __name__ == "__main__":
    frame = Tk()
    frame.title(f"Fractal de X de {RECURSIVE_LEVELS} niveis")

    side = IMAGE_SIZE
    canvas = Canvas(frame, bg = BACKGROUND_COLOR, height = side, width = side)
    canvas.pack()

    XFractal(RECURSIVE_LEVELS,side/2,side/2,side/2)

    frame.mainloop()

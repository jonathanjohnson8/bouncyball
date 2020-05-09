"""
Here is a Blue, Bouncing Ball.
First, it creates a canvas, then it creates a ball - "based on an oval of an arbitrary dimension"
It is setup to be able to recognize when it touches an edge of the canvas,based on its awareness of the 4 boundaries.
"""

import tkinter
import time


SQUARE_SIZE = 70
CANVAS_HEIGHT = 600
CANVAS_WIDTH = 600
CHANGE_X_START = 10
CHANGE_Y_START = 7
BALL_SIZE = 70

def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, 'Move BALL')
    ball = canvas.create_oval(0, 0, BALL_SIZE, BALL_SIZE, fill='blue', outline='blue')
    change_x = CHANGE_X_START
    change_y = CHANGE_Y_START
    while True:
        canvas.move(ball, change_x, change_y)
        if hit_left_wall(canvas, ball) or hit_right_wall(canvas, ball):
            change_x *= -1
        if hit_top_wall(canvas, ball) or hit_bottom_wall(canvas, ball):
            change_y *= -1
        canvas.update()
        time.sleep(1/50,)
    canvas.mainloop()


def hit_left_wall(canvas, object):
    return get_left_x(canvas, object) <= 0

def hit_top_wall(canvas, object):
    return get_top_y(canvas, object) <= 0

def hit_right_wall(canvas, object):
    return get_right_x(canvas, object) >= CANVAS_WIDTH

def hit_bottom_wall(canvas, object):
    return get_bottom_y(canvas, object) >= CANVAS_HEIGHT

def get_left_x(canvas, object):
    return canvas.coords(object)[0]

def get_top_y(canvas,object):
    return canvas.coords(object)[1]
def get_right_x(canvas, object):
    return canvas.coords(object)[2]
def get_bottom_y(canvas, object):
    return canvas.coords(object)[3]


def make_canvas(width, height, title):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    reachange_y for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas

if __name__ == "__main__":
    main()
from turtle import color
from graphics import *
import math


DIS_LEN = 800
LEN = DIS_LEN // 2
PADDING = 60
BACKGROUND_COLOR = color_rgb(245, 245, 245)
GREY = color_rgb(220, 220, 220)
BLACK = color_rgb(0, 0 , 0)
expr = 'x+2'
entry = Entry(Point(DIS_LEN / 2 + 2.5 * PADDING, DIS_LEN + 1.5 * PADDING), 40)
entered = False
display = GraphWin('Graphing Calculator', DIS_LEN + 2 * PADDING, DIS_LEN + 2 * PADDING)

#   real value to graphics.py value X
def convx(value: int) -> int:
    return value + LEN + PADDING

#   real value to graphics.py value Y
def convy(value: int) -> int:
    return (LEN - value) + PADDING

#   graphics.py value to real value X
def inv_convx(value: int) -> int:
    return value - LEN - PADDING

#   graphics.py value to real value Y
def inv_convy(value: int) -> int:
    return LEN - value - PADDING

def draw_origin() -> None:
    origin = Circle(Point(convx(0), convx(0)), 1)
    origin.setOutline(color_rgb(250, 0, 0))
    origin.setWidth(2)
    origin.draw(display)

def draw_borders() -> None:
    d = LEN
    draw_line(Point(-d, d), Point(d, d), GREY)
    draw_line(Point(d, -d), Point(d, d), GREY)
    draw_line(Point(d, -d), Point(-d, -d), GREY)
    draw_line(Point(-d, d), Point(-d, -d), GREY)

def draw_axis() -> None:
    d = LEN
    draw_line(Point(d, 0), Point(-d, 0), GREY)
    draw_line(Point(0, d), Point(0, -d), GREY)

def draw_point(x: int, y: int) -> None:
    p = Circle(Point(convx(x), convy(y)), 1)
    p.setWidth(0.5)
    p.draw(display)

def draw_line(p1: Point, p2: Point, color: color) -> None:
    p1.x = convx(p1.x)
    p1.y = convy(p1.y)
    p2.x = convx(p2.x)
    p2.y = convy(p2.y)

    line = Line(p1, p2)
    line.setFill(color)
    line.setWidth(1.5)
    line.draw(display)

def main_text(s: str) -> None:
    text = Text(Point(DIS_LEN / 2 - 3 * PADDING, DIS_LEN + 1.5 * PADDING), s)
    text.setFace('courier')
    text.setSize(12)
    text.draw(display)

def instruc_text(s: str) -> None:
    text = Text(Point(DIS_LEN / 2 + 260, DIS_LEN + 70), s)
    text.setFace('courier')
    text.setSize(8)
    text.draw(display)

def entry_text() -> None:
    entry.setFace('courier')
    entry.setSize(12)
    entry.setFill(GREY)
    entry.draw(display)

def clear_plot() -> None:
    rect = Rectangle(Point(convx(-LEN), convy(LEN)), Point(convx(LEN), convy(-LEN)))
    rect.setFill(BACKGROUND_COLOR)
    rect.draw(display)

def draw_root(x) -> None:
    words = "(" + str(round(x, 2)) + ", 0)"
    text = Text(Point(convx(x) + 10, convy(0) - 10), words)
    text.setFace('helvetica')
    text.setSize(8)

    point = Circle(Point(convx(x), convy(0)), 2)
    point.setFill(color_rgb(150, 30, 150))

    point.draw(display)
    text.draw(display)



# ---------------------- f(x) ----------------------- #

def f(x: int) -> float:
    try:
        return eval(expr)
    except:
        return 0.123456789
    
# ---------------------- f(x) ----------------------- #
        
def main():

    display.setBackground(BACKGROUND_COLOR)
    draw_borders()
    draw_axis()
    draw_origin()
    main_text("Enter expr here:")
    instruc_text("(Type EXIT to exit program)")
    entry_text()

    
    while True:
        xr = iter(range(-(LEN), LEN))
        k = ''
        while(k != 'Return'):
            k = display.getKey()
        
        global expr
        expr = entry.getText().strip()
        if expr == 'EXIT':
            quit()

        #reset
        clear_plot()
        draw_borders()
        draw_axis()
        draw_origin()
        
        for x in xr:
            y1 = f(x)
            y2 = f(x + 1)

            # fine x intercepts by seeing if f(x) and f(x+1) are of opposite sign
            if y1 == 0:
                draw_root(x)
            elif y1 * y2 < 0:
                draw_root(x + 0.5)
            
            if(abs(y1) < LEN and abs(y2) < LEN):
                draw_line(Point(x, y1), Point(x + 1, y2), BLACK)

            elif(abs(y1) > LEN and abs(y2) < LEN):
                if(y1 < 0):
                     closer = -LEN
                else:
                     closer = LEN
                draw_line(Point(x, closer), Point(x + 1, y2), BLACK)

            elif(abs(y1) < LEN and abs(y2) > LEN):
                #draw line to whichever is closer: y = LEN or y = -LEN
                if(y2 < 0):
                    closer = -LEN
                else:
                    closer = LEN
                draw_line(Point(x, y1), Point(x + 1, closer), BLACK)

    

main()

import turtle           #paint
import tkinter          #gui
import pyautogui as pag #gui
#import os              #os库


def initWindow():
    turtle.setup(800,600,0,0)
    turtle.up()
    turtle.goto(0,0)
    return

def getMouseXY_pag():
    return pag.position()

class sMetroWay:
    '直线way 宽,颜色,初始x,初始y,结束x,结束y'
    def __init__(self,width,color,stx,sty,endx,endy):
        self.width = width
        self.color = color
        self.stx = stx
        self.sty = sty
        self.endx = endx 
        self.endy = endy
        self.width = width


    def showWay(self):
        turtle.color(self.color)
        turtle.pensize(self.width)
        turtle.goto(self.stx, self.sty)
        turtle.down()
        turtle.goto(self.endx, self.endy)
        turtle.up()



#MainLoop
mouse_XY = getMouseXY_pag()
way1 = sMetroWay(50,"red",10,10,10,20)
way1.showWay()
turtle.done()
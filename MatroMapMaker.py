import turtle            #paint
import time              #time库
import tkinter           #gui
#import os               #os库

#####################################################

def initWindow():                               ##初始化
    turtle.hideturtle()                         #隐藏乌龟
    turtle.setup(800,600)                       #init窗口
    turtle.up()                                 #抬笔
    turtle.goto(0,0)                            #初始乌龟位置
    turtle.setheading(0)                        #设初始角度
    turtle.speed(0)                             #没有绘制过程
    return

class sMetroWay:                                #直线way
    '直线way 宽,颜色,初始x,初始y,结束x,结束y'
    def __init__(self,width,color,stx,sty,endx,endy):
        self.width = width
        self.color = color
        self.stx = stx
        self.sty = sty
        self.endx = endx 
        self.endy = endy
        self.width = width


    def s_showWay(self):                                #输出图形
        turtle.color(self.color)
        turtle.pensize(self.width)
        turtle.goto(self.stx, self.sty)
        turtle.down()
        turtle.goto(self.endx, self.endy)
        turtle.up()
    
    def sWayUndo(self):                                 #返回撤销操作次数
        for i in range(3):#??? unknown range!!!
            turtle.undo()
#####################################################

class cMetroWay:
    '曲线转角way 宽,颜色,半径,初始角度,结束角度,X,Y'
    def __init__(self,width,color,r,stangle,endangle,stx,sty):
        self.width = width
        self.color = color
        self.r = r
        self.stangle = stangle
        self.endangle = endangle
        self.stx = stx
        self.sty = sty
        if (self.stangle - self.endangle < 0):
            self.angle = self.endangle - self.stangle
        else:
            self.angle = self.stangle - self.endangle
            self.r = -1 * self.r
        #if(self.angle > 180):
        #   self.angle = self.angle - 180

    def c_showWay(self):
        turtle.color(self.color)
        turtle.pensize(self.width)
        turtle.goto(self.stx, self.sty)
        turtle.down()
        turtle.setheading(self.stangle)
        turtle.circle(self.r,self.angle)
        turtle.up()

    def cWayUndo(self):                                 #返回撤销操作次数
        for i in range(4):
            turtle.undo()

#MainLoop
zoom = 0.1 #画面缩放
initWindow()
#turtle.onclick((10,10),1,None)
way1 = sMetroWay(10 * zoom,"blue",10 * zoom,10 * zoom,10 * zoom,200 * zoom)
way1.s_showWay()
for r in range(3):
    way2 = cMetroWay((10 + 5 * r) * zoom,"red",100 * zoom,180,270,r * 30 * zoom,0 * zoom)
    way2.c_showWay()
    way2.cWayUndo()

for r in range(5):
    way2 = sMetroWay(10 * zoom,"blue",10 * zoom,10 * zoom,r * 20 * zoom,50 + 20 * r * zoom)
    way2.s_showWay()
    way2.sWayUndo()
    
for r in range(100):#缩放测试
    turtle.clear()
    zoom = zoom + 0.05
    way2 = cMetroWay((10 + 5) * zoom,"red",100 * zoom,180,270,30 * zoom,0 * zoom)
    way2.c_showWay()
    way2 = sMetroWay(10 * zoom,"blue",10 * zoom,10 * zoom,20 * zoom,50 + 20 * zoom)
    way2.s_showWay()
    

turtle.done()
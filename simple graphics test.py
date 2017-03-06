"""
Design Prolog 
Author:Karthik Nayak
Section 15
Email:karthiknayak@uky.edu
Date: 24th Sept 2015
Lab 4 individual 
Purpose:To Create a Halloween Party Invite Card with the users Name

"""

#Importing graphics library
from graphics import *


def main():
    #getting users name
    name = input("Enter name of recipient:")
    
    #creating graphics window
    win = GraphWin("Party Invite",600,600)
    win.setBackground('black')
    
    #Displays all greeting with user name     
    text1 = Text(Point(300,35), "Halloween Bash!")
    text1.setSize(30)
    text1.setOutline('green1')
    text1.draw(win)
    
    text2 = Text(Point(300,95), "Trick or Treat?")
    text2.setSize(30)
    text2.setOutline('green2')
    text2.draw(win)
    
    text3 = Text(Point(300,185), name)
    text3.setSize(30)
    text3.setOutline('cyan')
    text3.draw(win)
    
    text4 = Text(Point(300,245), "Lets have a SPOOKtacular time")
    text4.setSize(30)
    text4.setOutline('purple')
    text4.draw(win)
    
    text5 = Text(Point(300,550), "Be Scary!!")
    text5.setSize(30)
    text5.setOutline('white')
    text5.draw(win)
    
    text6 = Text(Point(300,515), "click to close window")
    text6.setSize(15)
    text6.setOutline('red')
    text6.draw(win)    
    
    #Drawing halloween pumkin with different objects 
    face = Oval(Point(200,310), Point(400,470))
    face.draw(win)
    face.setFill('orange2')
    face.setOutline('yellow')
    
    nose = Circle(Point(300,400),15)
    nose.draw(win)
    nose.setWidth(3)
    nose.setFill('yellow')
    
    eye1 = Polygon(Point(240,340),Point(280,360),Point(240,380))
    eye1.setWidth(3)
    eye1.setFill('yellow')    
    eye1.draw(win)
    
    eye2 = Polygon(Point(350,340),Point(300,360),Point(340,380))
    eye2.setWidth(3)
    eye2.setFill('yellow')    
    eye2.draw(win)    
    
    mouth = Rectangle(Point(260,425),Point(340,440))
    mouth.setWidth(3)
    mouth.setFill('yellow')    
    mouth.draw(win)    
    
    line = Line(Point(300,280),Point(300,310))
    line.setWidth(10)
    line.setFill('green4')    
    line.draw(win)  
    
    #waiting for user to click and then closing the window 
    win.getMouse()
    win.close()
    
main()

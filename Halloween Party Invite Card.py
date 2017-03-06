#Name: Nayak
#CS 115 Lab 4 Feedback Fall 2015
#Section 15
#Score   100 / 100 possible
#Late: No.
#Grading comments: Looks good. 
#
#Individual   42/42 pts
#  input name          6/6 pts
#  name as Text        6/6 pts
#  5 different classes 6/6 pts
#  3 different colors  6/6 pts
#  prolog              6/6 pts
#  documentation       6/6 pts
#  getMouse/close      6/6 pts
#Team          58/58 pts
#  get the Points      8 pts
#  get x's and y's     9 pts
#  draw one line, 
#     with circles    12 pts 
#  draw the other line, 
#     with circles    12 pts 
#  draw intersection point   5 pts
#  getMouse/close     6 pts
#  Text information   6 pts

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

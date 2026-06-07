from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self):
        super().__init__()
        
        self.shape("circle")
        self.color("red")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5) 
        self.speed("fastest")
        
    def refresh(self):
        rand_x = random.randint(-285,285)
        rand_y = random.randint(-285,285)
        self.goto(rand_x,rand_y)
               
import math
import random
import pygame
import tkinter as tk
from tkinter import massagebox

# the grid layout class
class square(obj):
    rows = 0
    width = 0

    def __init__(self,start,dirnx=1,dirny=0,color=(255,0,0)):
        ...

    def move(self,dirnx,dirny):
        ...

    def draw(self,surface, eyes = False):
        ...


# creating the snakes body
class snake(obj):
    def __init__(self,color,pos):
        ...

    def move(self):
        ...

    def reset(self,pos):
        ...

    def addBody(self):
        ...

    def draw(self,surface):



def drawGrid(w, rows, surface):
    ...

def redraw(surface):
    ...

def randomFood(rows, item):
    ...

def alertBox(subject,content):
    ...

def main():
    width = 500
    height = 500
    rows = 20
    win = pygame.display.set_mode((width,height))
    snake_ = snake((255,0,0), (10,10))
    flag = True
    
    clock = pygame.time.Clock()

    while flag:
        pygame.time.delay(50)
        clock.tick(10)



    

    ...


rows =
w =

cube.rows = rows
cube.w = w

main()

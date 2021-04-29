from turtle import Screen
from turtle import Turtle
import pygame
import tkinter

class Game:

    def __init__(self):
        screen = Screen()
        turtle = Turtle()
        root = tkinter.Tk()
        pygame.init()
        pygame.display.set_caption('Car Simulator 2077')
        image = pygame.image.load(r'C:\Users\Csaby\Documents\GitHub\kancsiazIsten\LOL.png')     
        screen.mainloop()

Game()
import pygame
import win32api
import win32con
import win32gui
import time
import numpy as np
import pyttsx3

from pygame.locals import *
from tkinter import *
from trainee import *

root = Tk()
pygame.init()

# For borderless, use pygame.NOFRAME
screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN) 
clock = pygame.time.Clock()

# Transparency color
transparency = (255, 0, 128)  
pygame.display.set_caption("Assistant")
font = pygame.font.Font("font\coders_crux.ttf", 40)
fullscreen = True
run = 1

#neccessary for transparant screen, add layer
hwnd = pygame.display.get_wm_info()["window"]
win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)
win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*transparency), 0, win32con.LWA_COLORKEY)

scr_w = root.winfo_screenwidth()
scr_h = root.winfo_screenheight()
tolx = scr_w/3*2
toly = scr_h/3*2

while run:
    check=0
    screen.fill(transparency)
    
    input = ""

    thought, run = mind(input)
    print(thought) 

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0
        if event.type == KEYDOWN:
            if event.key == K_F11:
                if fullscreen and not check:
                    scr_w = 1600
                    scr_h = 900
                    screen = pygame.display.set_mode((scr_w, scr_h))
                    fullscreen = False
                    check = 1
                    time.sleep(0.1)
                if not fullscreen and not check:
                    scr_w = root.winfo_screenwidth()
                    scr_h = root.winfo_screenheight()
                    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
                    fullscreen = True
                    time.sleep(0.1)
                    check = 1
    
    pygame.display.update()
    clock.tick(60)
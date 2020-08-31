import pygame as py
import random as rd
import math
py.init()
#colors
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
black=(0,0,0)
#creating window
window=py.display.set_mode((900,500),0,32)
py.display.set_caption("Ball Balancing")
bgimg=py.image.load('wedge2.jpg').convert()
py.display.update()
#variable
quit_game=False
game_over=False
b_x=450
b_y=180
fps=60
angle=0
clock=py.time.Clock()
while not quit_game:
    v_x=0
    v_y=0
    gravity=10
    if b_y>=400:
        gravity=0
        v_y=0
        v_x=0
    for event in py.event.get():
        if event.type==py.QUIT:
            quit_game=True
        if event.type==py.KEYDOWN:
            if event.key==py.K_ESCAPE:
                quit_game=True
            elif event.key==py.K_RIGHT:
                v_x+=30
            elif event.key==py.K_LEFT:
                v_x=-30
            elif event.key==py.K_SPACE:
                v_x=10
                v_y=-80
    angle+=1
    window.fill(white)
    #rotating image
    bgimg2=py.transform.rotate(bgimg,angle)
    mx,my=py.mouse.get_pos()
    window.blit(bgimg2,(400-int(bgimg2.get_width()/2),250-int(bgimg2.get_height()/2)))
    #drawing rectangle on surface
    bgimg_rect=py.Rect(400-int(bgimg2.get_width()/2),250-int(bgimg2.get_height()/2),int(bgimg2.get_width()),int(bgimg2.get_height()))
    #draw a ball
    ball=py.draw.circle(window,green,[b_x,b_y],30)
    #draw a rectangle around a ball 
    ball_rect=py.Rect(ball)
    if ball_rect.colliderect(bgimg_rect):
        if v_y>=0:
            ball_rect.bottom=bgimg_rect.top
            gravity=0
    
    v_y=v_y+(gravity)
    b_y+=v_y
    b_x+=v_x 
    # py.draw.rect(window,red,ball_rect) 
    clock.tick(fps)
    py.display.update()

py.quit()
quit()
    
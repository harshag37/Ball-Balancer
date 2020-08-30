import pygame,sys


def rotate(surface,angle):
   rotated_surface=pygame.transform.rotozoom(surface,-angle,1)
   rotated_rect=rotated_surface.get_rect(center=(250,400))
   return rotated_surface,rotated_rect    
      


pygame.init()
screen=pygame.display.set_mode((500,800))
clock=pygame.time.Clock()

bg_surface=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/background1.png').convert()
#bg_surface=pygame.transform.scale2x(bg_surface)
wedge_surface=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/base.png').convert_alpha()
wedge_rect=wedge_surface.get_rect(center=(250,400))
angle=0
SWANPIPE=pygame.USEREVENT
pygame.time.set_timer(SWANPIPE,1000)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
       
       # if event.type == SWANPIPE:
             
   
    angle+=1
    screen.blit(bg_surface,(0,0))
    wedge_rotated,wedge_rotated_rect = rotate(wedge_surface,angle)
    
    screen.blit(wedge_rotated,wedge_rotated_rect)
  
    pygame.display.update() 
    clock.tick(120)
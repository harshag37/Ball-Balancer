import pygame,sys



def rotatedxy(surface,angle):
   
   rotated_surface=pygame.transform.rotozoom(surface,-angle,1)
   rotated_rect=rotated_surface.get_rect(center=(250,400)) 

   #adding colour to rectangle
   #pygame.draw.rect(screen, [255, 0, 0], [250 - rotated_surface.get_width()//2, 400 - rotated_surface.get_height()//2, rotated_surface.get_width(), rotated_surface.get_height()], 0)
  # ox,oy=rotatedxy(surface, angle)
   mx,my=pygame.mouse.get_pos()


   # setting offset from center of ledge, it should be from its top left corner. corrected that here.
   offset=(mx-(250 - rotated_surface.get_width()//2),my-(400 - rotated_surface.get_height()//2))
   rotated_surface_mask = pygame.mask.from_surface(rotated_surface)




   result = rotated_surface_mask.overlap(circle_mask,offset)
   result2 = rotated_surface_mask.overlap(circle2_mask,offset)

   if result or result2:
        colour=circle2
   else:
        colour=circle
    
    
   screen.blit(colour,(mx,my))
    
   screen.blit(rotated_surface,rotated_rect)
  
   


pygame.init()
screen=pygame.display.set_mode((500,800))
clock=pygame.time.Clock()

bg_surface=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/background1.png').convert()
#bg_surface=pygame.transform.scale2x(bg_surface)
ledge_surface=pygame.image.load('C:/Users/DRAVI/Pictures/Screenshots/base.png').convert_alpha()
ledge_rect=ledge_surface.get_rect(center=(100,400))
ledge_mask=pygame.mask.from_surface(ledge_surface)
angle=0
#ox=wedge_rect.centerx
#oy=wedge_rect.centery

circle=pygame.image.load('C:/Users/DRAVI/Pictures/ci.png').convert_alpha()
circle_mask = pygame.mask.from_surface(circle)

circle2 = pygame.image.load('C:/Users/DRAVI/Pictures/ci2.png').convert_alpha()
circle2_mask = pygame.mask.from_surface(circle)


colour = circle



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                  pygame.quit()
                  sys.exit()
       
    angle+=1
   
        
   
    screen.fill((0, 0, 128))
    rotatedxy(ledge_surface, angle)
  
    pygame.display.update() 
    clock.tick(120)
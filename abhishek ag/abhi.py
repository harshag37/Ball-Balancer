import pygame,random,sys
pygame.init()

screen=pygame.display.set_mode((1500,750))

bg_surface=pygame.image.load(r'G:\background.png').convert()
bg_surface=pygame.transform.scale2x(bg_surface)
bg_surface=pygame.transform.scale2x(bg_surface)
bg_surface=pygame.transform.scale2x(bg_surface)
bg_surface=pygame.transform.scale2x(bg_surface)
bg_surface=pygame.transform.scale2x(bg_surface)

pl_surface=pygame.image.load(r'G:\plank2.png').convert_alpha()
pl_surface=pygame.transform.scale2x(pl_surface)

pl_rect=pl_surface.get_rect(center=(750,450))
ball_surface=pygame.image.load(r'G:\ball.png').convert_alpha()
angle=0
p=0
while True:	
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	screen.blit(bg_surface,(0,0))
	if p!=30:
		angle+=0.5
		p+=0.5
		new_surface=pygame.transform.rotozoom(pl_surface,angle,1)
		
		new_rect=new_surface.get_rect(center=(750,450))
	
	if p==30:
		angle-=0.5
		new_surface=pygame.transform.rotozoom(pl_surface,angle,1)
		new_rect=new_surface.get_rect(center=(750,450))
		if angle==-30:
			p=-30


    
	screen.blit(new_surface,new_rect)		      
	pygame.display.update()		



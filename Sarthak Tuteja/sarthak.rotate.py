import pygame,sys

def rotate(surface,angle):
	rotated_surface = pygame.transform.rotozoom(surface,-angle,1)
	rotated_rect = rotated_surface.get_rect(center = (288,510))
	return rotated_surface,rotated_rect
pygame.init()
screen = pygame.display.set_mode((576,1024))
clock=pygame.time.Clock()

background = pygame.image.load('assets/background.jpeg').convert()
background = pygame.transform.scale(background,(576,1024))
plank = pygame.image.load('assets/plank.png').convert_alpha()
plank = pygame.transform.scale(plank,(500,20))
plank_rect = plank.get_rect(center = (288,510))
angle = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
	
	angle += 1
	screen.blit(background,(0,0))
	plank_rotated,plank_rotated_rect = rotate(plank,angle)
	
	screen.blit(plank_rotated,plank_rotated_rect)
	pygame.display.update()
	clock.tick(120)		
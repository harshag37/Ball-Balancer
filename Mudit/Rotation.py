import pygame, sys

def rotate(surface,angle):
	rotated_surface = pygame.transform.rotozoom(surface,angle,1)
	rotated_rect = rotated_surface.get_rect(center = (450,350))
	return rotated_surface,rotated_rect
pygame.init()
clock = pygame.time.Clock()

#screen
screen = pygame.display.set_mode((900,700))


#ledge
ledge = pygame.image.load('E:/Drishti/Mini_project_aug_2020_ball_balancer/Rotation/Ledge.png').convert_alpha()
ledge_rect = ledge.get_rect(center = (450,350))
angle = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

	
	screen.fill((122,255,200))
	angle += 01
	#if angle >=180:
	#	angle = 0
	rotated_ledge, rotated_ledge_rect = rotate(ledge,angle)
				
	screen.blit(rotated_ledge,rotated_ledge_rect)		
	pygame.display.flip()
	clock.tick(200)		 
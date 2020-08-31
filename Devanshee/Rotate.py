import pygame, sys

pygame.init()
screen = pygame.display.set_mode((400,700))
clock = pygame.time.Clock()

slide = pygame.image.load('C:/Users/Dell/Desktop/slide.png').convert_alpha() 
slide_rect = slide.get_rect(center = (200,350))
angle = 0

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit

	screen.fill((0,0,235))
	angle += 1
	slide_r = pygame.transform.rotate(slide,angle)
	slide_rect = slide.get_rect(center = (200,350))
	screen.blit(slide_r,slide_rect)	

	pygame.display.update()
	clock.tick(120)
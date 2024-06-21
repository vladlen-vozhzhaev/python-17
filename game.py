import sys
import pygame

pygame.init()

screen = pygame.display.set_mode((1000, 700))
img = pygame.image.load('img/palne.png')
img = pygame.transform.scale(img, (200, 75))
img_x = 0
img_y = 20
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    img_x += 1
    screen.fill((0,0,0))
    screen.blit(img, (img_x, img_y))
    pygame.display.flip()
    clock.tick(60)
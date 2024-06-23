import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_SIZE = 40
PLAYER_SPEED = 5
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
WHITE = (255,255,255)
BLACK = (0,0,0)
clock = pygame.time.Clock()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (20, 20)
    def update(self, dx, dy):
        new_x = self.rect.x + dx
        new_y = self.rect.y + dy
        # Проверка на выход за границы экрана
        if new_x < 0:
            new_x = self.rect.x
        elif new_x > SCREEN_WIDTH - PLAYER_SIZE:
            new_x = self.rect.x
        elif new_y < 0:
            new_y = self.rect.y
        elif new_y > SCREEN_HEIGHT - PLAYER_SIZE:
            new_y = self.rect.y
        self.rect.x = new_x
        self.rect.y = new_y


player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    dx, dy = 0, 0
    if keys[pygame.K_LEFT]:
        dx = -PLAYER_SPEED
    if keys[pygame.K_RIGHT]:
        dx = PLAYER_SPEED
    if keys[pygame.K_UP]:
        dy = -PLAYER_SPEED
    if keys[pygame.K_DOWN]:
        dy = PLAYER_SPEED
    player.update(dx, dy)
    screen.fill(BLACK)
    all_sprites.draw(screen)
    pygame.display.flip()
    clock.tick(60)
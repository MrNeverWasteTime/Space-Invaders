import pygame
import random

# Inicialitzar pygame
pygame.init()

# Configuració de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Galactic Defense")

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Carregar imatges
try:
    background = pygame.transform.scale(pygame.image.load("backgroundd.jpg"), (WIDTH, HEIGHT))
    player_img = pygame.transform.scale(pygame.image.load("AVION.png"), (50, 50))
    enemy_img = pygame.transform.scale(pygame.image.load("Space-Invaders-Alien-PNG-Image.png"), (40, 40))
    bullet_img = pygame.transform.scale(pygame.image.load("bullet.png"), (10, 20))
except pygame.error as e:
    print(f"Error carregant imatges: {e}")
    exit()

# Fonts
font = pygame.font.Font(None, 36)

# Classes
class Player:
    def __init__(self):
        self.image = player_img
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.speed = 5
        self.lives = 3  # Vidas del jugador

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 50:
            self.x += self.speed

    def collide(self, enemy):
        return enemy.x < self.x + 50 and enemy.x + 40 > self.x and enemy.y < self.y + 50 and enemy.y + 40 > self.y

    def lose_life(self):
        self.lives -= 1

class Enemy:
    def __init__(self):
        self.image = enemy_img
        self.x = random.randint(0, WIDTH - 40)
        self.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.respawn()

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def respawn(self):
        self.x = random.randint(0, WIDTH - 40)
        self.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)

class Bullet:
    def __init__(self, x, y):
        self.image = bullet_img
        self.x = x
        self.y = y
        self.speed = 7

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def collide(self, enemy):
        return enemy.x < self.x < enemy.x + 40 and enemy.y < self.y < enemy.y + 40

# Crear jugador i enemics
player = Player()
enemies = [Enemy() for _ in range(5)]
bullets = []

running = True
clock = pygame.time.Clock()

def draw_lives():
    lives_text = font.render(f"Vidas: {player.lives}", True, WHITE)
    screen.blit(lives_text, (10, 10))

def game_over():
    screen.fill((0, 0, 0))
    game_over_text = font.render("GAME OVER", True, RED)
    screen.blit(game_over_text, (WIDTH // 2 - 80, HEIGHT // 2))
    pygame.display.update()
    pygame.time.delay(3000)
    pygame.quit()
    exit()

while running:
    screen.blit(background, (0, 0))  # Dibuixa el fons

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullets.append(Bullet(player.x + 20, player.y))

    # Mou el jugador
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move("left")
    if keys[pygame.K_RIGHT]:
        player.move("right")

    # Dibuixa el jugador i les vides
    player.draw()
    draw_lives()

    # Mou i dibuixa els enemics
    for enemy in enemies:
        enemy.move()
        enemy.draw()
        if player.collide(enemy):
            player.lose_life()
            enemy.respawn()
            if player.lives <= 0:
                game_over()

    # Mou i dibuixa les bales
    for bullet in bullets[:]:
        bullet.move()
        bullet.draw()

        # Comprova col·lisions
        for enemy in enemies:
            if bullet.collide(enemy):
                enemy.respawn()
                bullets.remove(bullet)
                break

        if bullet.y < 0:
            bullets.remove(bullet)

    pygame.display.update()
    clock.tick(60)  # Limita a 60 FPS

pygame.quit()

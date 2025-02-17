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
RED = (200, 0, 0)
GREEN = (0, 255, 0)

# Carregar imatges
bg = pygame.image.load("https://www.google.com/imgres?q=dank%20memer&imgurl=https%3A%2F%2Fi1.sndcdn.com%2Favatars-000218991771-8s9gta-t240x240.jpg&imgrefurl=https%3A%2F%2Fsoundcloud.com%2Fsilly-stix&docid=srYO46chhBiebM&tbnid=6iq7RjM85l-FDM&vet=12ahUKEwjT_9qNuL6LAxVf1gIHHRAoLYUQM3oECGcQAA..i&w=240&h=240&hcb=2&ved=2ahUKEwjT_9qNuL6LAxVf1gIHHRAoLYUQM3oECGcQAA")  # Has d'afegir una imatge de fons personalitzada
player_img = pygame.image.load("player.png")
enemy_img = pygame.image.load("enemy.png")
bullet_img = pygame.image.load("bullet.png")

# Classes
class Player:
    def __init__(self):
        self.image = pygame.transform.scale(player_img, (50, 50))
        self.x = WIDTH // 2
        self.y = HEIGHT - 80
        self.speed = 5
        self.lives = 3

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

    def move(self, direction):
        if direction == "left" and self.x > 0:
            self.x -= self.speed
        if direction == "right" and self.x < WIDTH - 50:
            self.x += self.speed

class Enemy:
    def __init__(self):
        self.image = pygame.transform.scale(enemy_img, (40, 40))
        self.x = random.randint(0, WIDTH - 40)
        self.y = random.randint(-100, -40)
        self.speed = random.randint(2, 4)

    def move(self):
        self.y += self.speed
        if self.y > HEIGHT:
            self.y = random.randint(-100, -40)
            self.x = random.randint(0, WIDTH - 40)

    def draw(self):
        screen.blit(self.image, (self.x, self.y))

class Bullet:
    def __init__(self, x, y):
        self.image = pygame.transform.scale(bullet_img, (10, 20))
        self.x = x
        self.y = y
        self.speed = 7

    def move(self):
        self.y -= self.speed

    def draw(self):
        screen.blit(self.image, (self.x, self.y))


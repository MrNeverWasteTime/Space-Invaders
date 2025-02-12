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

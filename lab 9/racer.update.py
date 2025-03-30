# Импортируем библиотеки
import pygame, sys
from pygame.locals import *
import random, time

# Инициализация Pygame
pygame.init()

# Частота обновления экрана (FPS)
FPS = 60
FramePerSec = pygame.time.Clock()

# Определяем цвета
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Определяем параметры экрана и скорости
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0

# Шрифты и текст
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

# Загружаем фон
background = pygame.image.load(r"C:\Users\bajge\OneDrive\PP2\lab 9\AnimatedStreet.png")

# Создаём экран
DISPLAYSURF = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Game")

# Класс игрока
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\bajge\OneDrive\PP2\lab 9\Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0 and pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH and pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)
        if self.rect.top > 0 and pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if self.rect.bottom < SCREEN_HEIGHT and pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)

# Класс врага
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load(r"C:\Users\bajge\OneDrive\PP2\lab 9\Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.bottom > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Класс монет с разным весом (1, 3, 5 очков)
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"C:\Users\bajge\OneDrive\PP2\lab 9\BuffCoin.png")
        self.image = pygame.transform.scale(self.image, (60, 60))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.value = random.choice([1, 3, 5])  # cost  1, 3 или 5 очков

    def move(self):
        self.rect.move_ip(0, 4)  # fall down moneta 
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def collect(self):
        global SCORE
        SCORE += self.value
        self.rect.top = 0  # Убираем монету после сбора
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Функция увеличения скорости врагов каждые 20 очков
def increase_enemy_speed():
    global SPEED
    if SCORE % 20 == 0 and SCORE != 0:  # Увеличиваем скорость при кратном 20 количестве очков
        SPEED += 1

# Создаём объекты
P1 = Player()
E1 = Enemy()

# Группы спрайтов
enemies = pygame.sprite.Group()
enemies.add(E1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1) # добавляем 
all_sprites.add(E1)

coins = pygame.sprite.Group()
for _ in range(1):  # Создаём три монеты
    coin = Coin()
    coins.add(coin)
    all_sprites.add(coin)

# Ивент для увеличения скорости
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Главный игровой цикл
while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5      
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # риусссууем  фон
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))

    # Обновление всех спиритов 
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # чекаем   собрал ли игрок монету
    collected_coins = pygame.sprite.spritecollide(P1, coins, dokill=True)  # dokill=True удаляет монету
    for coin in collected_coins:
        SCORE += coin.value  # Добавляем очки только если монета реально была собрана
        increase_enemy_speed()

    # Создаём новую монету, чтобы поддерживать их количество
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)


    # Проверяем столкновение игрока с врагами
    if pygame.sprite.spritecollideany(P1, enemies):
        time.sleep(1)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)

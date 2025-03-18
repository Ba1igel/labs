import pygame
import datetime

pygame.init()
width, height = 800, 800
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("MICKEY_WATCH")

clock_beti = pygame.image.load(r"C:\Users\bajge\OneDrive\skils\clock.png")
min_r_hand = pygame.image.load(r"C:\Users\bajge\OneDrive\skils\rightarm.png")
sec_l_hand = pygame.image.load(r"C:\Users\bajge\OneDrive\skils\leftarm.png")

orta = (width // 2, height // 2)

running = True
while running:
    screen.fill((0, 0, 0))  

    now = datetime.datetime.now()
    min_angle = -6 * now.minute
    sec_angle = -6 * now.second

    povernut_minute = pygame.transform.rotate(min_r_hand, min_angle)
    povernut_second = pygame.transform.rotate(sec_l_hand, sec_angle)

    screen.blit(clock_beti, clock_beti.get_rect(center=orta))
    screen.blit(povernut_minute, povernut_minute.get_rect(center=orta)) 
    screen.blit(povernut_second, povernut_second.get_rect(center=orta))

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()

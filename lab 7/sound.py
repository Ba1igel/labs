import pygame
import os

pygame.init()
pygame.mixer.init()

music_folder = r"C:\Users\bajge\OneDrive\music"  
songs = [os.path.join(music_folder, track) for track in os.listdir(music_folder) if track.endswith(".mp3")]

if not songs:
    print("Нет музыки в указанной папке!")
    pygame.quit()
    exit()

current_song = 0
paused = False

def play_music():
    pygame.mixer.music.load(songs[current_song]) # upload the songs but now play it
    pygame.mixer.music.play()

play_music()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Music Player")

running = True  
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    paused = True
                elif paused:
                    pygame.mixer.music.unpause()
                    paused = False
                else:
                    play_music()

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

            elif event.key == pygame.K_d:
                current_song = (current_song + 1) % len(songs)
                play_music()
            elif event.key == pygame.K_a:
                current_song = (current_song - 1) % len(songs)
                play_music()

pygame.quit()

import pygame
import os

pygame.init()

MUSIC_FOLDER = r"C:\Users\Глазков Артем\PycharmProjects\PythonProject2\.venv\share\music"

if not os.path.exists(MUSIC_FOLDER):  
    print(f"Папка {MUSIC_FOLDER} не найдена!")
    exit()

playlist = [os.path.join(MUSIC_FOLDER, f) for f in os.listdir(MUSIC_FOLDER) if f.endswith(".mp3")]
if not playlist:
    print("Нет MP3 файлов в папке!")
    exit()

current_track = 0
pygame.mixer.music.load(playlist[current_track])
pygame.mixer.music.play()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("MP3 Player")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

            elif event.key == pygame.K_RIGHT:
                current_track = (current_track + 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()

            elif event.key == pygame.K_LEFT:
                current_track = (current_track - 1) % len(playlist)
                pygame.mixer.music.load(playlist[current_track])
                pygame.mixer.music.play()

            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()

pygame.quit()

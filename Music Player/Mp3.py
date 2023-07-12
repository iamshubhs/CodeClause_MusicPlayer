from cgitb import enable
import collections
from gc import collect
from http import cookies
import pygame
import os

pygame.init()
pygame.mixer.init()

playlist = r"C:\Users\91958\Desktop\Shubhs\Projects\Music Player\Playlist.txt"

# Window size
window_width = 500
window_height = 250
window = pygame.display.set_mode((window_width, window_height))

window.fill((255, 255, 255))
font = pygame.font.Font(None, 40)
text_surface = font.render("Music by @iamshubhs", True, (10, 0, 10))
text_surface1 = font.render("Press Spacebar to start the Playlist", True, (10, 0, 10))

text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2))
text_rect1 = text_surface1.get_rect(center=(window_width // 2, window_height // 2+50))
window.blit(text_surface, text_rect)
window.blit(text_surface1, text_rect1)


# Update the window
pygame.display.flip()
pygame.display.set_caption("Music Player")

playlist1 = []

try:
    with open(playlist, 'r') as file:
        playlist1 = [line.strip() for line in file]
except FileNotFoundError:
    print("Playlist file not found. Please check the file path.")

if enable:
    enable()

current_song_index = 0

def play_song(song):
    if os.path.exists(song):
        pygame.mixer.music.load(song)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.event.poll()  # Allow event handling during playback
    else:
        print(f"Song not found: {song}")

def play_playlist():
    global current_song_index
    song = playlist1[current_song_index]
    play_song(song)

def play_next_song():
    global current_song_index
    current_song_index = (current_song_index + 1) % len(playlist1)
    play_playlist()

def play_previous_song():
    global current_song_index
    current_song_index = (current_song_index - 1) % len(playlist1)
    play_playlist()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()  # Quit pygame before exiting
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                play_playlist()
            elif event.key == pygame.K_RIGHT:
                play_next_song()
            elif event.key == pygame.K_LEFT:
                play_previous_song()

pygame.quit()

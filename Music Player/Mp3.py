import pygame

pygame.init()

#window size
window_width = 500
window_height = 350
window = pygame.display.set_mode((window_width, window_height))

window.fill((255, 255, 255))
font = pygame.font.Font(None, 36)
text_surface = font.render("Music by @iamshubhs", True, (10, 0, 10))
text_rect = text_surface.get_rect(center=(window_width // 2, window_height // 2))
window.blit(text_surface, text_rect)

    # Update the window
pygame.display.flip()
pygame.display.set_caption("Music Player")
pygame.mixer.music.load(r"C:\Users\91958\Desktop\Shubhs\Projects\Music Player\Attention - Charlie Puth(WellMp3.In).mp3")
pygame.mixer.music.play()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
pygame.quit()

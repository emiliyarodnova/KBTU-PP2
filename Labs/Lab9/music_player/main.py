import pygame
from player import load_music, play_music, pause_music, unpause_music, stop_music

pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((600, 350))
pygame.display.set_caption("Music Player")

font = pygame.font.SysFont(None, 36)
small_font = pygame.font.SysFont(None, 28)

playlist = [
    "./music_player/music/1.mp3",
    "./music_player/music/2.mp3"
]

current_track = 0
is_paused = False
running = True

load_music(playlist[current_track])


def get_song_name(path):
    return path.split("/")[-1]


while running:
    screen.fill((30, 30, 30))

    title_text = font.render("Simple Music Player", True, (255, 255, 255))
    song_text = small_font.render(
        "Now playing: " + get_song_name(playlist[current_track]),
        True,
        (200, 200, 200)
    )
    play_text = small_font.render("P - Play", True, (200, 200, 200))
    pause_text = small_font.render("Space - Pause / Resume", True, (200, 200, 200))
    stop_text = small_font.render("S - Stop", True, (200, 200, 200))
    next_text = small_font.render("Right Arrow - Next song", True, (200, 200, 200))
    prev_text = small_font.render("Left Arrow - Previous song", True, (200, 200, 200))
    exit_text = small_font.render("Esc - Exit", True, (200, 200, 200))

    screen.blit(title_text, (160, 30))
    screen.blit(song_text, (120, 80))
    screen.blit(play_text, (220, 130))
    screen.blit(pause_text, (140, 170))
    screen.blit(stop_text, (220, 210))
    screen.blit(next_text, (150, 250))
    screen.blit(prev_text, (135, 290))
    screen.blit(exit_text, (220, 330))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                play_music()
                is_paused = False

            elif event.key == pygame.K_SPACE:
                if is_paused:
                    unpause_music()
                    is_paused = False
                else:
                    pause_music()
                    is_paused = True

            elif event.key == pygame.K_s:
                stop_music()
                is_paused = False

            elif event.key == pygame.K_RIGHT:
                current_track += 1
                if current_track >= len(playlist):
                    current_track = 0
                load_music(playlist[current_track])
                play_music()
                is_paused = False

            elif event.key == pygame.K_LEFT:
                current_track -= 1
                if current_track < 0:
                    current_track = len(playlist) - 1
                load_music(playlist[current_track])
                play_music()
                is_paused = False

            elif event.key == pygame.K_ESCAPE:
                running = False

    pygame.display.update()

pygame.quit()

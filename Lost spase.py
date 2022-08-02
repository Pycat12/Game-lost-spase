import pygame
import Controls
from gun import Gun
from pygame.sprite import Group
from stats import Stats
from scores import Scores

def run():
    pygame.init()
    screen = pygame.display.set_mode((700, 700))
    pygame.display.set_caption("Lost spase")
    bg_color = (0, 0, 0)
    gun = Gun(screen)
    bullets = Group()
    inos = Group()
    Controls.create_army(screen, inos)
    stats = Stats()
    sc = Scores(screen, stats)

    while True:
        Controls.events(screen, gun, bullets)
        if stats.run_game:
            gun.update_gun()
            bullets.update()
            Controls.update(bg_color, screen, stats, sc, gun, inos, bullets)
            Controls.update_bullets(screen, stats, sc, inos, bullets)
            Controls.udate_inos(stats, screen, sc, gun, inos, bullets)
run()
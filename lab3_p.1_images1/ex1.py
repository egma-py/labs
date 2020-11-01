import pygame as pg
import pygame.draw as pgd

pg.init()

FPS = 30
screen = pg.display.set_mode((400, 400))
screen.fill((211, 211, 211))

#drawing body
pgd.circle(screen, (255, 255, 0), (200, 200), 100)
pgd.circle(screen, (0, 0, 0), (200, 200), 101, 1)

#right eye
pgd.circle(screen, (255, 0, 0), (245, 180), 16)
pgd.circle(screen, (0, 0, 0), (245, 180), 8)
pgd.circle(screen, (0, 0, 0), (245, 180), 17, 1)

#left eye
pgd.circle(screen, (255, 0, 0), (155, 180), 20)
pgd.circle(screen, (0, 0, 0), (155, 180), 10)
pgd.circle(screen, (0, 0, 0), (155, 180), 21, 1)

#mouth
pgd.line(screen, (0, 0, 0), (155, 260), (245, 260), 20)

#left eyebrow
pgd.polygon(screen, (0, 0, 0), [[99, 120], [105, 110], [185, 163], [179, 172]])

#right eyebrow
pgd.polygon(screen, (0, 0, 0), [[280, 146], [283, 153], [212, 177], [210, 168]])

pg.display.update()
clock = pg.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finished = True

pg.quit()


import pygame as pg
from sys import exit

#game variables
game_width = 1280
game_height = 800

#images
background_images = pg.image.load("assets/Background_grassy.png")

pg.init()#Initialize the window
windows = pg.display.set_mode((game_width, game_height))
pg.display.set_caption("Game")
clock = pg.time.Clock()#Frame rate asset

#x, y, width, height
player = pg.Rect(150, 150, 130, 50)

def Draw():
    windows.fill("black")
    windows.blit(background_images, (0,0))
    pg.draw.rect(windows, (2, 239, 238), player)

while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()
            #Pressed down and released
        # if event.type == pg.KEYDOWN:
            # if event.key in (pg.K_UP, pg.K_w):
            #     player.y -= 5
            # if event.key in (pg.K_DOWN, pg.K_s):
            #     player.y += 5
            # if event.key in (pg.K_LEFT, pg.K_a):
            #     player.x -= 5
            # if event.key in (pg.K_RIGHT, pg.K_d):
            #     player.x += 5
    keys = pg.key.get_pressed()
    if keys[pg.K_UP] or keys[pg.K_w]:
        player.y -= 5
    if keys[pg.K_DOWN] or keys[pg.K_s]:
        player.y += 5
    if keys[pg.K_LEFT] or keys[pg.K_a]:
        player.x -= 5
    if keys[pg.K_RIGHT] or keys[pg.K_d]:
        player.x += 5
    Draw()

    pg.display.update()
    clock.tick(60)
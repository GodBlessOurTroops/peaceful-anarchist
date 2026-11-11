import pygame as pg
from sys import exit

#game variables
game_width = 1280
game_height = 800
player_x = game_width/2
player_y = game_height/2
player_width = 42
player_height = 48

#images
background_images = pg.image.load("assets/Background_grassy.png")
character = pg.image.load("assets/character_crack.png")

#Initialize the window
pg.init()
windows = pg.display.set_mode((game_width, game_height))
pg.display.set_caption("Game")
clock = pg.time.Clock()#Frame rate asset

class Player (pg.Rect):
 def __init__(self):
    pg.Rect.__init__(self, player_x, player_y, player_width, player_height)
    self.image = character

#x, y, width, height
player = Player()

def Draw():
    windows.fill("black")
    windows.blit(background_images, (0,0))
    windows.blit(player.image, player)
while True:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit()
            exit()

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
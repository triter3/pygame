import pygame as pg
import player
import game_map
import colisions
import vec2 as v

class World():
    def __init__(self):
        self.restart()

    def restart(self):
        self.player = player.Player(0.2)
        self.map = game_map.Map(0.2);
        self.camera = Camera()
        self.camera.follow(self.player)
        self.resize(pg.display.Info().current_w)

    def update(self, time):
        #crida de updates
        self.player.update(time)
        #comprovacio de colisions
        while((colisions.colision_map(self.player,self.map))): pass

    def resize(self, ref):
        self.camera.resize(ref)
        self.player.resize(ref)
        self.map.resize(ref)

    def draw(self, screen):
        self.camera.update()
        self.map.draw_map(screen, self.camera)
        self.player.draw(screen, self.camera)

class Camera():
    def __init__(self):
        self.ini_pos = v.Vec2(0,0)
        self.offset = v.Vec2(0,0)
        self.entity = None

    def resize(self, ref):
        self.ini_pos.x = pg.display.Info().current_w/2
        self.ini_pos.y = pg.display.Info().current_h/2

    def follow(self, entity):
        self.entity = entity

    def fix(self):
        self.entity = None

    def move(self, x, y):
        self.offset.x += x
        self.offset.y += y

    def set_pos(self, x, y):
        self.offset.x = x
        self.offset.y = y

    def update(self):
        if self.entity != None:
            self.offset.x = self.entity.rect.x + self.entity.rect.width/2
            self.offset.y = self.entity.rect.y + self.entity.rect.height/2

    def get_pos(self):
        pos = v.Vec2(0,0)
        pos.x = self.ini_pos.x - self.offset.x
        pos.y = self.ini_pos.y - self.offset.y
        return pos

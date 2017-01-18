import pygame as pg
import player
import game_map
import colisions
import vec2 as v
import json

class World():
    def __init__(self):
        self.restart()

    def restart(self):
        pro = self.load_pro("game_properties.json")
        self.player = player.Player(pro["players"]["player1"])
        self.map = game_map.Map(pro["map"]);
        self.camera = Camera()
        # self.camera.follow(self.player)
        self.resize()

    def update(self, time):
        #crida de updates
        self.player.update(time)
        #comprovacio de colisions
        while((colisions.colision_map(self.player,self.map))): pass

    def resize(self):
        self.camera.resize()
        self.player.resize(self.camera)
        self.map.resize(self.camera)

    def draw(self, screen):
        self.map.draw_map(screen, self.camera)
        self.player.draw(screen, self.camera)

    def load_pro(self, name):
        f = open(name, "r")
        return json.load(f)



class Camera():
    def __init__(self):
        self.ini_pos = v.Vec2(0,0)
        self.offset = v.Vec2(0,0)
        self.size = v.Vec2(200,200)
        self.entity = None

    def resize(self):
        self.size.x = pg.display.Info().current_w
        self.size.y = 200
        if(pg.display.Info().current_h/self.size.y <= 2):
            self.size.y = pg.display.Info().current_h
        self.ini_pos.x = int(self.size.x/2)
        self.ini_pos.y = int(self.size.y/2)
        self.ref = int(pg.display.Info().current_h/self.size.y)

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

    def get_pos(self):
        pos = v.Vec2(0,0)
        pos.x = int(self.ini_pos.x/self.ref - self.offset.x)
        pos.y = int(self.ini_pos.y - self.offset.y)
        if self.entity != None:
            pos.x -= self.entity.rect.x + int(self.entity.rect.width/2)
            pos.y -= self.entity.rect.y + int(self.entity.rect.height/2)
        return pos

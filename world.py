import player
import pygame as pg
import game_map
import colisions

class World():
    def __init__(self):
        self.restart()

    def restart(self):
        self.player = player.Player(0.3)
        self.map = game_map.Map(0.2);
        self.resize(pg.display.Info().current_w)

    def update(self, time):
        #crida de updates
        self.player.update(time, self.map)
        #comprovacio de colisions
        if colisions.colision_map(self.player,self.map): print("colision")


    def resize(self, ref):
        self.player.resize(ref)
        self.map.resize(ref)

    def draw(self, screen):
        self.map.draw_map(screen)
        self.player.draw(screen)

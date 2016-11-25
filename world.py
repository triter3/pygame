import player
import game_map

class World():
    def __init__(self):
        self.restart()

    def restart(self):
        self.player = player.Player(0.2)
        self.map = game_map.Map(0.2);

    def update(self, time):
        self.player.update(time)

    #def resize(w,h):
        #self.player.resize(w,h)
        #self.map.resize(w,h)

    def draw(self, screen):
        self.map.draw_map(screen)
        self.player.draw(screen)

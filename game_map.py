import pygame as pg

class Map:
	def __init__(self, tile_dim):
		self.restart()
		self.tile_dim = tile_dim
		self.tile = Tile()

	def restart(self):
		self.buffer_map = [[1,1,1,1,1,0,0,0,1],[0,0,0,0,0,0,0,0,1],[0,0,1,0,0,0,0,0,1],[0,0,0,0,0,0,0,0,1],[1,0,0,0,1,0,0,0,1], [1,0,0,0,1,0,0,0,1], [1,0,0,0,1,0,0,0,1], [1,0,0,0,1,0,0,0,1]]
		self.offset_x = 0
		self.offset_y = 0

	def resize(self, ref):
		self.tile.set_size(ref, self.tile_dim)
		d = (len(self.buffer_map[0])*self.tile.get_size())/2
		self.map_shift_x = (pg.display.Info().current_w/2) - d
		d = (len(self.buffer_map)*self.tile.get_size())/2
		self.map_shift_y = (pg.display.Info().current_h/2) - d

	def move_map(self, x, y):
		self.offset_x += x
		self.offset_y += y

	def draw_map(self, screen):
		for j in range(0, len(self.buffer_map)):
			for i in range(0, len(self.buffer_map[j])):
				if self.buffer_map[j][i] == 1:
					self.tile.draw(screen, i*self.tile.get_size() + self.map_shift_x + self.offset_x,
						j*self.tile.get_size() + self.map_shift_y + self.offset_y)



class Tile():
	def __init__(self):
		self.color = [140,2,140]

	def draw(self, screen, x ,y):
		self.rect.x = x
		self.rect.y = y
		screen.blit(self.image, self.rect)

	def get_size(self):
		return self.rect.width

	def set_size(self, ref, dimensions):
		self.image = pg.Surface([dimensions*ref, dimensions*ref])
		self.image.fill(self.color)
		self.rect = self.image.get_rect()

import pygame as pg

class Map:
	def __init__(self, dimensions):
		self.restart()
		self.tile = Tile(dimensions)

	def restart(self):
		self.buffer_map = [[1,1,1,1,1],[0,0,0,0,0],[0,0,1,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,1,1]]
		self.offset_x = 0
		self.offset_y = 0
		d = (len(self.buffer_map[0])*self.tile.get_size())/2
		self.map_shift_x = (pg.display.Info().current_w/2) - d - self.tile.get_size()/2
		d = (len(self.buffer_map)*self.tile.get_size())/2
		self.map_shift_y = (pg.display.Info().current_h/2) - d - self.tile.get_size()/2

	def resize(ref):
		self.tile.set_size(ref)

	def draw_map(self, screen):
		for j in range(0, len(self.buffer_map)):
			for i in range(0, len(self.buffer_map[j])):
				if self.buffer_map[j][i] == 1:
					self.tile.draw(screen, i*self.tile.get_size(),
						j*self.tile.get_size())



class Tile(pg.sprite.Sprite):
	def __init__(self, dimensions):
		pg.sprite.Sprite.__init__(self)
		self.dimensions = dimensions
		self.image = pg.Surface([64,64])
		self.image.fill([140, 2, 140])
		self.rect = self.image.get_rect()
		ref = pg.display.Info().current_w
		self.rect.width = self.dimensions*ref
		self.rect.height = self.dimensions*ref

	def draw(self, screen, x ,y):
		self.rect.x = x - self.rect.width
		self.rect.y = y - self.rect.height
		screen.blit(self.image, self.rect)

	def get_size(self):
		return self.rect.width

	def set_size(ref):
		self.rect.width = self.dimensions*ref
		self.rect.height = self.dimensions*ref

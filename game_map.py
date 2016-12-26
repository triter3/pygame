import pygame as pg
import vec2 as v

class Map:
	def __init__(self, tile_dim):
		self.tile_dim = tile_dim
		self.shift = v.Vec2(0,0)
		self.tile = Tile()
		#temporal
		self.buffer_map = [1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1], [1,0,0,0,0,1,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1]
		# self.buffer_map = [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]

	def resize(self, ref):
		self.tile.set_size(ref, self.tile_dim)
		self.shift.x = -((len(self.buffer_map[0]))*self.tile.get_size())/2
		self.shift.y = -((len(self.buffer_map))*self.tile.get_size())/2

	def draw_map(self, screen, camera):
		for j in range(0, len(self.buffer_map)):
			for i in range(0, len(self.buffer_map[j])):
				if self.buffer_map[j][i] == 1:
					self.tile.draw(screen, camera,
						i*self.tile.get_size() + self.shift.x,
						j*self.tile.get_size() + self.shift.y )


class Tile():
	def __init__(self):
		self.color = [150,2,140] #temporal

	def draw(self, screen, camera, x ,y):
		self.rect.x = x + camera.get_pos().x
		self.rect.y = y + camera.get_pos().y
		screen.blit(self.image, self.rect)

	def get_size(self):
		return self.rect.width

	def set_size(self, ref, dimensions):
		self.image = pg.Surface([dimensions*ref, dimensions*ref])
		self.image.fill(self.color)
		self.rect = self.image.get_rect()

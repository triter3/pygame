import pygame as pg
import vec2 as v
import os

class Map:
	def __init__(self, tile_dim):
		self.tile_dim = tile_dim
		self.shift = v.Vec2(0,0)
		self.tile = Tile()
		#temporal
		self.buffer_map = [1,1,1,1,1,1,1,1,1],[1,0,0,0,0,0,0,0,0],[1,0,0,0,0,0,0,0,1],[1,0,0,0,0,0,0,0,1], [1,0,0,0,0,1,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1], [1,0,0,0,0,0,0,0,1],[1,1,1,1,1,1,1,1,1]
		# self.buffer_map = [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0], [0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0]

	def resize(self, camera):
		self.tile.set_size(self.tile_dim*camera.ref)
		self.shift.x = -len(self.buffer_map[0])*self.tile_dim/2
		self.shift.y = -len(self.buffer_map)*self.tile_dim/2

	def draw_map(self, screen, camera):
		for j in range(0, len(self.buffer_map)):
			for i in range(0, len(self.buffer_map[j])):
				if self.buffer_map[j][i] == 1:
					self.tile.draw(screen, camera,
						i*self.tile_dim + self.shift.x,
						j*self.tile_dim + self.shift.y )


class Tile():
	def __init__(self):
		self.color = [150,2,140] #temporal
		self.or_image = pg.image.load(os.path.join("tile1.png")).convert()

	def draw(self, screen, camera, x ,y):
		self.rect.x = x + camera.get_pos().x
		self.rect.y = y + camera.get_pos().y
		self.rect.x = int(self.rect.x*camera.ref)
		self.rect.y = int(self.rect.y*camera.ref)
		screen.blit(self.image, self.rect)

	def set_size(self, size):
		self.image = pg.transform.scale(self.or_image, [size, size])
		self.rect = self.image.get_rect()

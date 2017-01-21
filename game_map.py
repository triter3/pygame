import pygame as pg
import vec2 as v
import os
import csv

class Map:
	def __init__(self, pro):
		self.tile_dim = pro["tile_size"]*2
		self.open_map(pro["dir"])
		self.load_tiles(pro["tiles"])
		self.shift = v.Vec2(0,0)

	def resize(self, camera):
		for i in self.tiles_list:
			i.set_size(self.tile_dim*camera.ref)
		self.shift.x = -len(self.buffer_map[0])*self.tile_dim/2
		self.shift.y = -len(self.buffer_map)*self.tile_dim/2

	def draw_map(self, screen, camera):
		for j in range(0, len(self.buffer_map)):
			for i in range(0, len(self.buffer_map[j])):
				if self.buffer_map[j][i] != "0":
					self.tiles_list[int(self.buffer_map[j][i]) - 1].draw(screen, camera,
						i*self.tile_dim + self.shift.x,
						j*self.tile_dim + self.shift.y )

	def open_map(self, map_file):
		self.buffer_map = []
		with open(map_file, "r") as csvfile:
			f = csv.reader(csvfile, delimiter = ',')
			for row in f:
				self.buffer_map.append(row)

	def load_tiles(self, pro):
		self.tiles_list = []
		for i in range(1, pro["num"] + 1):
			self.tiles_list.append(Tile(pro[str(i)]))

class Tile():
	def __init__(self, img_file):
		self.or_image = pg.image.load(os.path.join(img_file)).convert()

	def draw(self, screen, camera, x ,y):
		self.rect.x = x + camera.get_pos().x
		self.rect.y = y + camera.get_pos().y
		self.rect.x = int(self.rect.x*camera.ref)
		self.rect.y = int(self.rect.y*camera.ref)
		screen.blit(self.image, self.rect)

	def set_size(self, size):
		self.image = pg.transform.scale(self.or_image, [size, size])
		self.rect = self.image.get_rect()

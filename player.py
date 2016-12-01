import pygame as pg

class Player():
	def __init__(self, dimensions):
		self.dimensions = dimensions
		self.color = [140, 2, 2]
		self.rect = pg.Rect(0,0,0,0)
		self.restart()

	def restart(self):
		self.velocity = 0.1
		#situa al personatge al centre de la pantalla
		self.rect.x = (pg.display.Info().current_w - self.rect.width)/2
		self.rect.y = (pg.display.Info().current_h - self.rect.height)/2

	def update(self,time,map):
		key = pg.key.get_pressed()
		direction = [0,0]
		if key[pg.K_a]: direction[0] = -1
		if key[pg.K_d]: direction[0] = 1
		if key[pg.K_w]: direction[1] = -1
		if key[pg.K_s]: direction[1] = 1

		#self.rect = self.rect.move(self.velocity*direction[0]*time,
			#self.velocity*direction[1]*time)
		map.move_map(-self.velocity*direction[0]*time,
			-self.velocity*direction[1]*time)

	def resize(self, ref):
		self.image = pg.Surface([self.dimensions*ref, self.dimensions*ref])
		rect = self.image.get_rect()
		self.rect.x += (-rect.width + self.rect.width)/2
		self.rect.y += (-rect.height + self.rect.width)/2
		self.rect.width = rect.width
		self.rect.height = rect.height
		self.image.fill(self.color)

	def draw(self, screen):
		 screen.blit(self.image, self.rect)

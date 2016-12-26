import pygame as pg
import vec2 as v

class Player():
	def __init__(self, dimensions):
		self.dimensions = dimensions
		self.color = [140, 2, 2] #temporal
		self.velocity = 0.2
		self.rect = pg.Rect(0,0,0,0)
		self.last_pos = v.Vec2(0,0)

	def update(self, time):
		key = pg.key.get_pressed()
		direction = v.Vec2(0,0)
		if key[pg.K_a]: direction.x = -1
		if key[pg.K_d]: direction.x = 1
		if key[pg.K_w]: direction.y = -1
		if key[pg.K_s]: direction.y = 1

		if not key[pg.K_LSHIFT]:
			direction.x *= self.velocity*time
			direction.y *= self.velocity*time
		self.move(direction)

	def resize(self, ref):
		#modifica la imatge
		self.image = pg.Surface([self.dimensions*ref, self.dimensions*ref])
		#modifica la posició respecte la mida
		pos = v.Vec2()
		pos.x = self.rect.x + self.rect.width/2
		pos.y = self.rect.x + self.rect.height/2
		self.rect = self.image.get_rect()
		self.rect.x = pos.x - self.rect.width/2
		self.rect.y = pos.y - self.rect.height/2
		self.image.fill(self.color)

	def move(self, vec, update = True):
		if update:
			self.last_pos.x = self.rect.x
			self.last_pos.y = self.rect.y
		self.rect.x += vec.x
		self.rect.y += vec.y

	def set_pos(self, vec):
		self.last_pos.x = self.rect.x
		self.last_pos.y = self.rect.y
		self.rect.x = vec.x
		self.rect.y = vec.y

	def get_offset(self):
		a = v.Vec2()
		a.x = self.rect.x - self.last_pos.x
		a.y = self.rect.y - self.last_pos.y
		return a

	def draw(self, screen, camera):
		rect = pg.Rect(self.rect)
		rect.x += camera.get_pos().x
		rect.y += camera.get_pos().y
		screen.blit(self.image, rect)

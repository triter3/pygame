import pygame as pg
import vec2 as v
import os

class Player():
	def __init__(self, dim):
		self.dim = dim
		self.color = [140, 2, 2] #temporal
		self.velocity = 0.2
		self.rect = pg.Rect(-dim/2,-dim/2,dim,dim)
		self.last_pos = v.Vec2(0,0)
		self.or_image = pg.image.load(os.path.join("player.png")).convert()

	def update(self, time):
		key = pg.key.get_pressed()
		direction = v.Vec2(0,0)
		if key[pg.K_a]: direction.x = -1
		if key[pg.K_d]: direction.x = 1
		if key[pg.K_w]: direction.y = -1
		if key[pg.K_s]: direction.y = 1
		if not key[pg.K_LSHIFT]:
			direction.x *= int(self.velocity*time)
			direction.y *= int(self.velocity*time)
		self.move(direction)

	def resize(self, camera):
		#modifica la imatge
		self.image = pg.transform.scale(self.or_image, [self.dim*camera.ref, self.dim*camera.ref])

	def move(self, vec, update = True):
		if update:
			self.last_pos.x = self.rect.x
			self.last_pos.y = self.rect.y
		self.rect.x += vec.x
		self.rect.y += vec.y

	def set_pos(self, vec, update = True):
		if update:
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
		v.zoom_rect(rect, camera.ref)
		screen.blit(self.image, rect)

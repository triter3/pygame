import pygame as pg
import vec2 as v
import os

class Player():
	def __init__(self, pro, gravity):
		dim = v.Vec2(pro["width"]*2, pro["height"]*2)
		self.velocity = pro["velocity"]
		self.controls = pro["controls"]
		self.rect = pg.Rect(-dim.x/2,-dim.y/2,dim.x,dim.y)
		self.last_pos = v.Vec2(0,0)
		self.or_image = pg.image.load(os.path.join(pro["skin"])).convert()
		self.jump = Jump(pro["jump_force"])
		self.jump.gravity = gravity

	def update(self, time):
		key = pg.key.get_pressed()
		direction = v.Vec2(0,1) #gravity on 'y'= 1 // 'y' = 0
		if key[ord(self.controls["left"])]: direction.x = -1
		if key[ord(self.controls["right"])]: direction.x = 1
		if key[ord(self.controls["jump"])]: self.jump.jump() #gravity on
		# if key[pg.K_w]: direction.y = -1 #gravity off
		# if key[pg.K_s]: direction.y = 1 #gravity off
		direction.x *= int(self.velocity*time)
		# direction.y *= int(self.velocity*time) #gravity off
		direction.y *= self.jump.get_movement(time) #gravity on
		self.move(direction)

	def resize(self, camera):
		#modifica la imatge
		self.image = pg.transform.scale(self.or_image, [self.rect.width*camera.ref, self.rect.height*camera.ref])

	def move(self, vec, update = True):
		if update:
			self.last_pos.x = self.rect.x
			self.last_pos.y = self.rect.y
		self.rect.x += vec.x
		self.rect.y += vec.y

	def colision(self, side):
		if side == "down":
			self.jump.floor()

		if side == "up":
			self.jump.velocity = 0

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

class Jump():
	def __init__(self, jump_f):
		self.gravity = 0
		self.jump_f = jump_f
		self.in_jump = False
		self.velocity = 0

	def jump(self):
		if(not self.in_jump):
			self.velocity = -self.jump_f
			self.in_jump = True

	def get_movement(self, time):
		x = int(self.velocity*time)
		if self.velocity < 25:
			self.velocity = self.velocity + self.gravity*time
		return x

	def floor(self):
		self.velocity = 0
		self.in_jump = False

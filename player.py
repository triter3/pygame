import pygame as pg

class Player(pg.sprite.Sprite):
	def __init__(self, dimensions):
		pg.sprite.Sprite.__init__(self)
		self.image = pg.Surface([dimensions*pg.display.Info().current_w,
			dimensions*pg.display.Info().current_h])
		self.image.fill([140, 2, 2])
		self.restart()

	def restart(self):
		self.rect = self.image.get_rect()
		self.velocity = 0.1
		self.rect.x = (pg.display.Info().current_w - self.rect.width)/2
		self.rect.y = (pg.display.Info().current_h - self.rect.height)/2

	def update(self,time):
		key = pg.key.get_pressed()
		direction = [0,0]
		if key[pg.K_a]: direction[0] = -1
		if key[pg.K_d]: direction[0] = 1
		if key[pg.K_w]: direction[1] = -1
		if key[pg.K_s]: direction[1] = 1
		if key[pg.K_r]:
			self.width = 500
			self.height = 500
			self.image = pg.transform.rotozoom(self.image, 20)
			self.rect = self.image.get_rect(center=self.rect.center)

		self.rect = self.rect.move(self.velocity*direction[0]*time, self.velocity*direction[1]*time)
		#print(self.rect.x , ",", self.rect.y)

	#def resize(w,h):

	def draw(self, screen):
		 screen.blit(self.image, self.rect)

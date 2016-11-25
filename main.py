import pygame as pg
import world
import sys

def main():
	pg.init()
	screen = pg.display.set_mode([500,500])
	pg.display.set_caption("prova")
	clock = pg.time.Clock()
	g_world = world.World()
	#inici del bucle principal
	while True:
		clock.tick(30)
		for event in pg.event.get():
			if event.type == pg.QUIT: sys.exit()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE: sys.exit()
		screen.fill([0,0,0])
		g_world.update(clock.get_time())
		g_world.draw(screen)
		pg.display.flip()

if __name__ == "__main__":
	main()

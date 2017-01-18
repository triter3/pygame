import pygame as pg
import world
import sys

def main():
	pg.init()
	screen = pg.display.set_mode([200,200], pg.RESIZABLE)
	pg.display.set_caption("pygame")
	clock = pg.time.Clock()
	g_world = world.World()
	#inici del bucle principal
	while True:
		clock.tick(30)
		for event in pg.event.get():
			if event.type == pg.QUIT: sys.exit()
			if event.type == pg.VIDEORESIZE:
				last = pg.display.Info().current_h
				screen = pg.display.set_mode(event.dict['size'], pg.RESIZABLE)
				g_world.resize()
			elif event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE: sys.exit()
		screen.fill([0,0,0])
		g_world.update(clock.get_time())
		g_world.draw(screen)
		pg.display.flip()

if __name__ == "__main__":
	main()

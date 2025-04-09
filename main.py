import pygame
import sys
from constants import *
from player import Player
from asteroid_class import Asteroid
from shot import Shot
from asteroidfield import AsteroidField

def main():
	pygame.init()
	clock = pygame.time.Clock()
	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))	
	print("Starting Asteroids!")
	print(f"Screen width: {SCREEN_WIDTH}")
	print(f"Screen height: {SCREEN_HEIGHT}")
	drawable = pygame.sprite.Group()
	updateable = pygame.sprite.Group()
	rocks = pygame.sprite.Group()
	shots_group = pygame.sprite.Group()
	Player.containers = (drawable, updateable)
	Asteroid.containers = (rocks, drawable, updateable)
	AsteroidField.containers = (updateable)
	Shot.containers = (shots_group, drawable, updateable)
	player = Player(shots_group, SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
	asteroid_field = AsteroidField()
	dt = 0
	while True:
		for event in pygame.event.get():
   			if event.type == pygame.QUIT:
        			return
		for obj in updateable:
			obj.update(dt)

		for obj in rocks:
			if player.is_colliding(obj):
				print("Game over!")
				sys.exit()
	
		for obj in rocks:
			for bullet in shots_group:
				if obj.is_colliding(bullet):
					new_asteroids = obj.split()
					for asteroid in new_asteroids:
						rocks.add(asteroid)
						drawable.add(asteroid)
						updateable.add(asteroid)
					obj.kill()
					bullet.kill()
		screen.fill("black")
		for obj in drawable:
			obj.draw(screen)

		pygame.display.flip()
		dt = clock.tick(60) / 1000

if __name__ == "__main__":
	main()


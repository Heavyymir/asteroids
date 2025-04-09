import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

class Asteroid(CircleShape):
	def __init__(self, x, y, radius):
		super().__init__(x, y, radius)

	def draw(self, screen):
		pygame.draw.circle(screen, "white", (self.position.x, self.position.y), self.radius,  2)

	def update(self, dt):
                self.position += (self.velocity * dt) 
	
	def split(self):
		self.kill()
		if self.radius <= ASTEROID_MIN_RADIUS:
			return[]
		else:
			random_angle = random.uniform(20, 50)
			rotated_vector1 = self.velocity.rotate(random_angle)
			rotated_vector2 = self.velocity.rotate(-random_angle)
			new_radius = self.radius - ASTEROID_MIN_RADIUS
			asteroid1 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid2 = Asteroid(self.position.x, self.position.y, new_radius)
			asteroid1.velocity = rotated_vector1 * 1.2
			asteroid2.velocity = rotated_vector2 * 1.2
			return [asteroid1, asteroid2]


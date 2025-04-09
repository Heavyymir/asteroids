from constants import *
from circleshape import CircleShape
from shot import Shot
import pygame

class Player(CircleShape):
	def __init__(self, shots_group, x, y):
		super().__init__(x, y, PLAYER_RADIUS)
		self.rotation = 0
		self.shots_group = shots_group
		timer = 0
		self.timer = timer

	def triangle(self):
    		forward = pygame.Vector2(0, 1).rotate(self.rotation)
    		right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
    		a = self.position + forward * self.radius
    		b = self.position - forward * self.radius - right
    		c = self.position - forward * self.radius + right
    		return [a, b, c]

	def draw(self, screen):
		pygame.draw.polygon(screen, "white", self.triangle(), 2)
		
	def rotate(self, dt):
		self.rotation += (PLAYER_TURN_SPEED * dt) 
	
	def move(self, dt):
		forward = pygame.Vector2(0, 1).rotate(self.rotation)
		self.position += forward * PLAYER_SPEED * dt

	def update(self, dt):
		if self.timer > 0:
			self.timer -= dt
		keys = pygame.key.get_pressed()
		if keys[pygame.K_a]:
			self.rotate(-dt)
		if keys[pygame.K_d]:
			self.rotate(dt)
		if keys[pygame.K_s]:
			self.move(-dt)
		if keys[pygame.K_w]:
			self.move(dt)
		if keys[pygame.K_SPACE]:
			self.shoot()
		
	def shoot(self):
		if self.timer > 0:
			return False
		offset = pygame.Vector2(0, self.radius)
		offset = offset.rotate(self.rotation)
		new_shot = Shot(self.position.x + offset.x, self.position.y + offset.y)
		velocity = pygame.Vector2(0, 1)
		velocity = velocity.rotate(self.rotation)
		velocity = velocity * PLAYER_SHOOT_SPEED
		new_shot.velocity = velocity
		self.shots_group.add(new_shot)
		self.timer = PLAYER_SHOOT_COOLDOWN
		return True

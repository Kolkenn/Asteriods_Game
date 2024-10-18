import pygame
from circleshape import CircleShape
from shot import Shot
from constants import *

class Player(CircleShape):
    
    def __init__(self, x, y):
        super().__init__(x, y,PLAYER_RADIUS)
        self.rotation = 0
        self.shoot_limit = 0
    
    def draw(self, screen):
        pygame.draw.polygon(screen,'white',self.triangle(),2)

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def rotate(self,delta_time):
        self.rotation += PLAYER_TURN_SPEED * delta_time

    def update(self, delta_time):
        self.shoot_limit -= delta_time
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            # Rotate to the left
            self.rotate(-delta_time)
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            # Rotate to the right
            self.rotate(delta_time)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            # Move Forward
            self.move(delta_time)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            # Move Forward
            self.move(-delta_time)
        if keys[pygame.K_SPACE] and self.shoot_limit <= 0:
            # Shoot
            self.shoot()
            self.shoot_limit = PLAYER_SHOOT_COOLDOWN

    def move(self,delta_time):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * delta_time

    def shoot(self):
        shot = Shot(self.position.x,self.position.y)
        shot.velocity = pygame.Vector2(0,1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
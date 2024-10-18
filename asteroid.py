import pygame, random
from circleshape import CircleShape
from constants import *

class Asteroid(CircleShape):
    def __int__(self,x,y,radius):
        super().__init__(x,y,radius)
    
    def draw(self,screen):
        pygame.draw.circle(screen,'white',self.position,self.radius,2)
    
    def update(self,delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            # Small Asteroid is just destroyed
            return
        else:
            angle = random.uniform(20,50)
            new_radius = self.radius - ASTEROID_MIN_RADIUS

            new_asteriod = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteriod.velocity = self.velocity.rotate(angle) * ASTEROID_SPLIT_SPEED

            new_asteriod = Asteroid(self.position.x,self.position.y,new_radius)
            new_asteriod.velocity = self.velocity.rotate(-angle) * ASTEROID_SPLIT_SPEED
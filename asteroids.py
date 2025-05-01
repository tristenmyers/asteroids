import pygame
import random
from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)
    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)
    def update(self, dt):
        self.position += (self.velocity * dt)
    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        random_angle = random.uniform(20, 50)
        first_asteroid_vector = pygame.math.Vector2.rotate(self.velocity, random_angle)
        second_asteroid_vector = pygame.math.Vector2.rotate(self.velocity, -random_angle)
        new_radius = self.radius - ASTEROID_MIN_RADIUS
        first_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        second_new_asteroid = Asteroid(self.position[0], self.position[1], new_radius)
        first_new_asteroid.velocity = first_asteroid_vector * 1.2
        second_new_asteroid.velocity = second_asteroid_vector * 1.2
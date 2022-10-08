import pygame
import math


class Pendulum:
    G = 9.81

    def __init__(self, length):
        self.origin = pygame.math.Vector2(400, 0)
        self.length = length
        self.mass = 8
        self.pos = pygame.math.Vector2(400, self.origin.y + self.length)

        self.angle = 0
        self.a_vel = 0
        self.a_acc = 0

    def draw(self, screen):
        pygame.draw.line(screen, (255, 255, 255), self.origin, self.pos, 2)
        pygame.draw.circle(screen, (255, 255, 255), self.pos, 10)

    def update(self, delta_time):

        self.pos.x = self.length * math.sin(self.angle) + self.origin.x
        self.pos.y = self.length * math.cos(self.angle) + self.origin.y

        self.a_acc = -self.G * math.sin(self.angle) * self.mass / self.length

        self.angle += self.a_vel * delta_time
        self.a_vel += self.a_acc

        self.a_vel *= 0.99

    def handle_events(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.angle = 0
                self.angle = math.atan2(pygame.mouse.get_pos()[0] - self.origin.x, pygame.mouse.get_pos()[1] - self.origin.y)
                #print(self.angle)


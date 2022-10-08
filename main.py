import pygame
import sys
from pendulum import Pendulum
from random import randint


class Application:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Pendulum")
        self.clock = pygame.time.Clock()

        #self.pendulum = Pendulum()

        self.lengths = [i for i in range(100, 300, 20)]
        print(len(self.lengths))

        self.pendulums = [Pendulum(length) for i, length in enumerate(self.lengths)]
        print(self.pendulums)

        self.running = True

    def run(self):
        while self.running:

            delta_time = self.clock.tick(144) / 1000

            self.events()
            self.update(delta_time)
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            for pendulum in self.pendulums:
                pendulum.handle_events(event)

    def update(self, delta_time):
        for pendulum in self.pendulums:
            pendulum.update(delta_time)

    def draw(self):
        self.screen.fill((0, 0, 0))
        for pendulum in self.pendulums:
            pendulum.draw(self.screen)

        pygame.display.update()


if __name__ == '__main__':
    app = Application()
    app.run()




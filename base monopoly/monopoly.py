# Créé par Valentin, le 05/02/2023 en Python 3.7
import pygame


class Game:
    def __init__(self, screen):
        self.screen = screen
        self.running = True
        self.clock = pygame.time.Clock()

    def handling_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        pass

    def display(self):
        screen.blit(plateau,(300,125))
        pygame.display.flip()


    def run(self):
        while self.running:
            self.handling_events()
            self.update()
            self.display()
            self.clock.tick(120)


pygame.init()
screen=pygame.display.set_mode((1080,720))
plateau=pygame.image.load("monopoly.jpg").convert()
game=Game(screen)
game.run()
pygame.quit()

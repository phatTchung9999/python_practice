import pygame
import random
from pygame.sprite import Sprite


from settings import Settings



class Ethereum(Sprite):

    def __init__(self, ai_game):
        super().__init__()
        self.settings = Settings()

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('./images/eth.bmp')
        self.image = pygame.transform.scale(
            self.image, (self.settings.eth_width, self.settings.eth_height)
        )
        self.rect = self.image.get_rect()

        self.x_position = random.randrange(
            int(self.settings.eth_width/2), int(self.screen_rect.right - self.settings.eth_width/2 ), 
            self.settings.eth_width)

        self.rect.centerx = self.x_position


        self.y = float(self.rect.y)
    



    def update(self):
        self.y += self.settings.eth_drop_speed

        self.rect.y = self.y






    

     




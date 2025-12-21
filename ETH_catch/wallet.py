import pygame

from settings import Settings

class Wallet:

    def __init__(self, ai_game):
        self.settings = Settings()

        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        self.image = pygame.image.load('./images/wallet.bmp')
        self.image = pygame.transform.scale(
            self.image, (self.settings.wallet_width, self.settings.wallet_height)
        )

        self.rect = self.image.get_rect()

        self.rect.midbottom = self.screen_rect.midbottom

        self.moving_right = False
        
        self.moving_left = False

        self.x = float(self.rect.x)
    
    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        if self.moving_right:
            self.x += self.settings.wallet_speed
        elif self.moving_left:
            self.x -= self.settings.wallet_speed
        
        self.rect.x = self.x

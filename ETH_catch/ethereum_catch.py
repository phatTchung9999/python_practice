import pygame
import sys
from time import sleep
import random


from settings import Settings
from ethereum import Ethereum
from wallet import Wallet


class EthereumCatch:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("ETH Catch")
        self.game_running = True
        self.wallet = Wallet(self)
        self.ethereums = pygame.sprite.Group()
        


    def create_eth(self):
        new_ethereum = Ethereum(self)
        self.ethereums.add(new_ethereum)
    
    def check_edge_eth(self):
        for eth in self.ethereums.copy():
            if eth.rect.top >= self.settings.screen_height:
                self.ethereums.remove(eth)

    def update_eth(self):
        self.ethereums.update()
        self.check_edge_eth()

        if random.randint(0,45) == 0:
            self.create_eth()


    def update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.ethereums.draw(self.screen)
        self.wallet.blitme()

        self.clock.tick(60)
        pygame.display.flip()
    
    def update_wallet(self):
        self.wallet.update()
    
    def check_collision(self):
        for eth in self.ethereums.copy():
            if eth.rect.colliderect(self.wallet.rect):
                self.ethereums.remove(eth)



    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.wallet.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.wallet.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.wallet.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.wallet.moving_left = False

    def run_game(self):
        while self.game_running:
            self.check_events()
            self.update_eth()
            self.update_wallet()
            self.check_collision()
            self.update_screen()


if __name__ == '__main__':
    ai_game = EthereumCatch()
    ai_game.run_game()
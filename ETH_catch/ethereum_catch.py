import pygame
import sys
from time import sleep
import random
import pymsgbox


from settings import Settings
from ethereum import Ethereum
from wallet import Wallet
from button import Button
from game_stats import GameStats
from scoreboard import ScoreBoard



class EthereumCatch:
    
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.stats = GameStats(self)

        

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )

        pygame.display.set_caption("ETH Catch")
        self.stats.fund = int(pymsgbox.prompt("How much is your budget?"))
        self.game_running = False
        self.wallet = Wallet(self)
        self.ethereums = pygame.sprite.Group()
        self.play_button = Button(self, "Play")
        self.board = ScoreBoard(self)

        
        


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
        
        if not self.game_running:
            self.play_button.draw_button()
        
        self.wallet.blitme()
        self.ethereums.draw(self.screen) 
        self.board.show_fund()
        self.board.show_eth_price()


        self.clock.tick(120)
        pygame.display.flip()
    
    def update_wallet(self):
        self.wallet.update()
    
    def check_collision(self):
        for eth in self.ethereums.copy():
            if eth.rect.colliderect(self.wallet.rect):
                self.stats.fund -= self.settings.eth_price
                self.board.prep_fund()
                self.ethereums.remove(eth)
    
    def check_play_button(self, mouse_pos):
        if self.play_button.rect.collidepoint(mouse_pos):
            self.game_running = True
    
    def restart(self):
        self.ethereums.empty()
        self.game_running = False


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.wallet.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.wallet.moving_left = True
                elif event.key == pygame.K_p:
                    self.restart()
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.wallet.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.wallet.moving_left = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self.check_play_button(mouse_pos)


    def run_game(self):
        while True:
            self.check_events()

            if self.game_running:
                self.update_eth()
                self.update_wallet()
                self.check_collision()
            self.update_screen()
            self.clock.tick(60)


if __name__ == '__main__':
    ai_game = EthereumCatch()
    ai_game.run_game()




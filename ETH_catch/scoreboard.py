import pygame.font 

class ScoreBoard:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.stats = ai_game.stats
        
        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_fund()
        self.prep_eth_price()

    def prep_fund(self):
        fund_str = str(self.stats.fund)
        self.fund_image = self.font.render(
            fund_str, True, self.text_color, self.settings.bg_color
        )
    
        self.fund_rect = self.fund_image.get_rect()
        self.fund_rect.right = self.screen_rect.right - 20
        self.fund_rect.top = 20
    
    def prep_eth_price(self):
        price_str = str(self.settings.eth_price)
        self.price_image = self.font.render(
            price_str, True, self.text_color, self.settings.bg_color
        )
        self.price_rect = self.price_image.get_rect()
        self.price_rect.left = self.screen_rect.left + 20
        self.price_rect.top = 20
    
    def show_fund(self):
        self.screen.blit(self.fund_image, self.fund_rect)
    
    def show_eth_price(self):
        self.screen.blit(self.price_image, self.price_rect)

    


    
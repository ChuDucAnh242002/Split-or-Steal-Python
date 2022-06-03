import pygame

class Button:
    def __init__(self, x, y, image):
        
        self.image = image
        self.width = self.image.get_width()
        self.height = self.image.get_height()
        self.rect = pygame.Rect(x, y, self.width, self.height)

    def draw(self, win):
        win.blit(self.image, (self.rect.x, self.rect.y))

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[0]
        if self.rect.collidepoint(x1, y1):
            return True
        else: return False
import pygame
import sys
import os
from network import Network
from button import Button

pygame.init()
pygame.font.init()

WIDTH, HEIGHT = 700, 700

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Client")

CLOCK = pygame.time.Clock()
FPS = 60

# Color 
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Size
IMAGE_WIDTH, IMAGE_HEIGHT = 200, 200

# Image 
SPLIT_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'split.png')), (IMAGE_WIDTH, IMAGE_HEIGHT))
STEAL_IMAGE = pygame.transform.scale(pygame.image.load(os.path.join('asset', 'steal.png')), (IMAGE_WIDTH, IMAGE_HEIGHT))

def drawwin(win, game, player):
    win.fill(WHITE)

    if not(game.connected()):
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render("Waiting for Player...", 1, RED, True)
        win.blit(text, (WIDTH // 2 - text.get_width() / 2, HEIGHT // 2 - text.get_height() / 2 ))

    else:
        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [Button(50, 500, SPLIT_IMAGE), Button(WIDTH - IMAGE_WIDTH - 50, 500, STEAL_IMAGE)]
def main():
    run = True
    n = Network()

    player = int(n.getP())
    print("You are player", player)

    while run:

        CLOCK.tick(FPS)

        try: 
            game = n.send("get")
        except:
            run = False
            print("Couldn't get game")
            break

        if game.bothWent():
            drawwin(WIN, game, player)
            pygame.time.delay(500)
            try:
                game = n.send("reset")
            except:
                run = False
                print("Couldn't get game while reseting")
                break


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
        drawwin(WIN, game, player)

def menu_screen():
    run = True
    
    while run:
        CLOCK.tick(FPS)
        WIN.fill(WHITE)
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, RED)

        WIN.blit(text, (WIDTH // 2 - text.get_width() /2 , HEIGHT // 2 - text.get_height()/2))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


if __name__ == "__main__":
    while True:
        menu_screen()
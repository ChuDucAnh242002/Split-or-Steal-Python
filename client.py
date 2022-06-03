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

FONT = pygame.font.SysFont("comicsans", 40)
FONT2 = pygame.font.SysFont("comicsans", 60)
FONT3 = pygame.font.SysFont("comicsans", 90)

def drawwin(win, game, p):
    win.fill(WHITE)

    
    if not(game.connected()):
        text = FONT.render("Waiting for Player...", 1, RED, True)
        win.blit(text, (WIDTH // 2 - text.get_width() / 2, HEIGHT // 2 - text.get_height() / 2 ))

    else:
        if game.result():
            if p == 0:
                text = str(game.get_cashp1()) + " dollar"
            else:
                text = str(game.get_cashp2()) + " dollar"

        else:
            text = str(game.get_cash()) + " dollar"
        cash_text = FONT2.render(text, 1, BLUE)
        win.blit(cash_text, (WIDTH // 2 - cash_text.get_width() / 2, 100 ))

        text = FONT2.render("Your move", 1, (0, 255, 255))
        win.blit(text, (80, 200))

        text = FONT2.render("Opponents", 1, (0, 255, 255))
        win.blit(text, (380, 200))

        move1 = game.get_player_move(0)
        move2 = game.get_player_move(1)
        if game.bothWent():
            text1 = FONT2.render(move1, 1, (0, 0, 0))
            text2 = FONT2.render(move2, 1, (0, 0, 0))

        else:
            if game.p1Went and p == 0:
                text1 = FONT2.render(move1, 1, (0,0,0))
            elif game.p1Went:
                text1 = FONT2.render("Locked In", 1, (0, 0, 0))
            else:
                text1 = FONT2.render("Waiting...", 1, (0, 0, 0))

            if game.p2Went and p == 1:
                text2 = FONT2.render(move2, 1, (0,0,0))
            elif game.p2Went:
                text2 = FONT2.render("Locked In", 1, (0, 0, 0))
            else:
                text2 = FONT2.render("Waiting...", 1, (0, 0, 0))

        if p == 1:
            win.blit(text2, (100, 350))
            win.blit(text1, (400, 350))
        else:
            win.blit(text1, (100, 350))
            win.blit(text2, (400, 350))


        for btn in btns:
            btn.draw(win)

    pygame.display.update()


btns = [Button("SPLIT", 50, 500, SPLIT_IMAGE),
        Button("STEAL", WIDTH - IMAGE_WIDTH - 50, 500, STEAL_IMAGE)]

def main():
    run = True
    n = Network()

    player = int(n.getP())
    # print("You are player", player)

    while run:

        CLOCK.tick(FPS)

        try: 
            game = n.send("get")
        except:
            run = False
            # print("Couldn't get game")
            break

        if game.bothWent():
            drawwin(WIN, game, player)
            pygame.time.delay(2000)
            try:
                game = n.send("reset")
            except:
                run = False
                # print("Couldn't get game while reseting")
                break

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                for btn in btns:
                    if btn.click(pos) and game.connected():
                        
                        if player == 0:
                            if not game.p1Went:
                                n.send(btn.text)  
                        else:
                            if not game.p2Went:
                                n.send(btn.text)

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
import pygame
import sys
from pygame.locals import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN
#Need : food
pygame.init()
SURFACE = pygame.display.set_mode((500,500))
FPSCLOCK = pygame.time.Clock()
class Player:
    p1 = 1 #(1 ~ 40)
    p2 = 1 #(1 ~ 40)
    d = 4
    alive = 1
    def draw():
        pygame.draw.rect(SURFACE,(255,255,0),((Player.p1 - 1 )* 10 + 50,(Player.p2 - 1) * 10 + 25,10,10))
        pygame.draw.rect(SURFACE,(0,0,0),((Player.p1  - 1) * 10 + 50,(Player.p2 - 1) * 10 + 25,10,10),1)
        if Player.alive == 0:
            pygame.draw.rect(SURFACE,(255,0,0),((Player.p1 - 1 )* 10 + 50,(Player.p2 - 1) * 10 + 25,10,10))
    def move():
        if Player.d == 1:
            Player.p2 -= 1
        elif Player.d == 2:
            Player.p2 += 1
        elif Player.d == 3:
            Player.p1 -= 1
        elif Player.d == 4:
            Player.p1 += 1
        elif Player.alive == 0:
            Player.d = 0

class Frame:
    def __init__(self,a,b,c,d):
        pygame.draw.rect(SURFACE,(220,220,220),(a,b,c,d))

def gameover():
    font1 = pygame.font.Font(None,60)
    text1 = font1.render("GAME OVER",True,(255,0,0))
    SURFACE.blit(text1,(120,200))
def main():
    
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_UP:
                    Player.d = 1
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_DOWN:
                    Player.d = 2
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_LEFT:
                    Player.d = 3
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_RIGHT:
                    Player.d = 4
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))
        f1 = Frame(0,0,50,500)
        f2 = Frame(450,0,50,500)
        f3 = Frame(0,0,500,25)
        f4 = Frame(0,425,500,75)
        Player.draw()
        Player.move()

        if Player.p1 < 1 or Player.p1 > 40 or Player.p2 < 1 or Player.p2 > 40:
            Player.alive = 0
            Player.d = 0
            gameover()
        FPSCLOCK.tick(10)
            
        pygame.display.update()


if __name__ == '__main__':
    main()

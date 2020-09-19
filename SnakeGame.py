import pygame
import random
import sys
from pygame.locals import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN
#Need : food
pygame.init()
SURFACE = pygame.display.set_mode((500,500))
FPSCLOCK = pygame.time.Clock()
class Player:
    p = [[20,20]]   # snake bodies' position
    d = 4   # moving direction
    alive = 1   # 1 = alive, 0 = dead
    tp = [0,0]  # turning point
    def draw():
        for i in range(len(Player.p)):
            pygame.draw.rect(SURFACE,(255,255,0),((Player.p[i][0] - 1 )* 10 + 50,\
            (Player.p[i][1] - 1) * 10 + 25,10,10))
        for i in range(len(Player.p)):
            pygame.draw.rect(SURFACE,(0,0,0),((Player.p[i][0]  - 1) * 10 + 50,\
            (Player.p[i][1] - 1) * 10 + 25,10,10),1)
        if Player.alive == 0:   # turning red when died
            pygame.draw.rect(SURFACE,(255,0,0),((Player.p[0][0] - 1 )* 10 + 50,\
        (Player.p[0][1] - 1) * 10 + 25,10,10))
    def move():
        if Player.d == 1:
            for i in range(len(Player.p)):
                Player.p[i][1] -= 1
        elif Player.d == 2:
            for i in range(len(Player.p)):
                Player.p[i][1] += 1
        elif Player.d == 3:
            for i in range(len(Player.p)):
                Player.p[i][0] -= 1
        elif Player.d == 4:
            for i in range(len(Player.p)):
                Player.p[i][0] += 1
        elif Player.alive == 0:
            Player.d = 0
    def foodcheck():
        if Player.p[0][0] == Food.p[0] and Player.p[0][1] == Food.p[1]:
            Food.setpos()
            if Player.d == 1:
                Player.p.append([Player.p[0][0], Player.p[0][1] - len(Player.p)])
            elif Player.d == 2:
                Player.p.append([Player.p[0][0], Player.p[0][1] + len(Player.p)])
            elif Player.d == 3:
                Player.p.append([Player.p[0][0] + len(Player.p), Player.p[0][1]])
            elif Player.d == 4:
                Player.p.append([Player.p[0][0] - len(Player.p), Player.p[0][1]])

class Food:
    p = [0,0]
    def setpos():
        Food.p[0] = random.randint(1,40)
        Food.p[1] = random.randint(1,40)
    def draw():
        pygame.draw.rect(SURFACE,(0,0,255),((Food.p[0] - 1) * 10 + 50,\
        (Food.p[1] - 1)  * 10 + 25,10,10))
        pygame.draw.rect(SURFACE,(0,0,0),((Food.p[0] - 1) * 10 + 50,\
        (Food.p[1] - 1) * 10 + 25,10,10),1)

class Frame: # frames of the game
    def __init__(self,a,b,c,d):
        pygame.draw.rect(SURFACE,(220,220,220),(a,b,c,d))

def gameover(): # printing game over letter
    font1 = pygame.font.Font(None,60)
    text1 = font1.render("GAME OVER",True,(255,0,0))
    SURFACE.blit(text1,(120,200))
def restart():  # reset or restart. press R
    Player.p[0] = [20,20]
    Player.alive = 1
    Player.d = 4
def main():
    Food.setpos()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:   # key bindings
                if event.key == K_UP:
                    Player.tp = [Player.p[0][0], Player.p[0][1]]
                    Player.d = 1
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_DOWN:
                    Player.tp = [Player.p[0][0], Player.p[0][1]]
                    Player.d = 2
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_LEFT:
                    Player.tp = [Player.p[0][0], Player.p[0][1]]
                    Player.d = 3
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_RIGHT:
                    Player.tp = [Player.p[0][0], Player.p[0][1]]
                    Player.d = 4
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_r:
                    restart()
            elif event.type == QUIT:
                pygame.quit()
                sys.exit()

        SURFACE.fill((255,255,255))
        f1 = Frame(0,0,50,500)
        f2 = Frame(450,0,50,500)
        f3 = Frame(0,0,500,25)
        f4 = Frame(0,425,500,75)
        Food.draw()
        Player.draw()
        Player.move()
        Player.foodcheck()
        if Player.p[0][0] < 1 or Player.p[0][0] > 40 or Player.p[0][1] < 1 or Player.p[0][1] > 40:
            Player.alive = 0
            Player.d = 0
            gameover()
        FPSCLOCK.tick(10)
            
        pygame.display.update()


if __name__ == '__main__':
    main()

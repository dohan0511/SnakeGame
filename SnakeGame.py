import pygame
import random
import sys
from pygame.locals import QUIT, K_UP, K_DOWN, K_LEFT, K_RIGHT, KEYDOWN
pygame.init()
SURFACE = pygame.display.set_mode((500,500))
FPSCLOCK = pygame.time.Clock()
class Player:
    p = [[20,20],[19,20],[18,20]]   # snake bodies' position
    d = 4   # moving direction
    alive = 1   # 1 = alive, 0 = dead
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
            Player.p.insert(0, [Player.p[0][0], Player.p[0][1] - 1])
            Player.p.pop()
        elif Player.d == 2:
            Player.p.insert(0, [Player.p[0][0], Player.p[0][1] + 1])
            Player.p.pop()
        elif Player.d == 3:
            Player.p.insert(0, [Player.p[0][0] - 1, Player.p[0][1]])
            Player.p.pop()
        elif Player.d == 4:
            Player.p.insert(0, [Player.p[0][0] + 1, Player.p[0][1]])
            Player.p.pop()
        elif Player.alive == 0:
            Player.d = 0
    def FoodCheck():
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
    def EnemyCheck():
        for i in Enemy.p:
            if Player.p[0][0] == i[0] and Player.p[0][1] == i[1]:
                Player.alive = -1
                Player.d = 0
                gameover('defeated')
                
                
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

class Scoreboard:
    def draw():
        font1 = pygame.font.Font(None,40)
        text1 = font1.render("SCORE : "+str(len(Player.p)),True,(0,0,0))
        SURFACE.blit(text1,(20,450))

class Enemy:
    p = [[0,0],[0,0],[0,0]]   # snake bodies' position
    d = 0  # moving direction
    alive = 1   # 1 = alive, 0 = dead
    count = 0
    WCcount = 0
    def draw():
        if Enemy.alive == 1 and Enemy.p[0] != [0,0]:
            for i in range(len(Enemy.p)):
                pygame.draw.rect(SURFACE,(10,10,10),((Enemy.p[i][0] - 1 )* 10 + 50,\
                (Enemy.p[i][1] - 1) * 10 + 25,10,10))
            for i in range(len(Enemy.p)):
                pygame.draw.rect(SURFACE,(0,0,0),((Enemy.p[i][0]  - 1) * 10 + 50,\
                (Enemy.p[i][1] - 1) * 10 + 25,10,10))
    def SetStartPos():
        if Enemy.p[0] == [0,0]:
            Enemy.p[0][0] = random.randint(10,30)
            Enemy.p[0][1] = random.randint(10,30)
    def SetDirection():
        data = random.randint(1,4)
        i = 0
        while i == 0:
            if Enemy.d == 1:
                if data == 2:
                    data = random.randint(1,4)
                else:
                    i += 1
            elif Enemy.d == 2:
                if data == 1:
                    data = random.randint(1,4)
                else:
                    i += 1
            elif Enemy.d == 3:
                if data == 4:
                    data = random.randint(1,4)
                else:
                    i += 1
            elif Enemy.d == 4:
                if data == 3:
                    data = random.randint(1,4)
                else:
                    i += 1
            else:
                i += 1
        Enemy.d = data
    def move():
        if Enemy.d == 1:
            Enemy.p.insert(0, [Enemy.p[0][0], Enemy.p[0][1] - 1])
            Enemy.p.pop()
        elif Enemy.d == 2:
            Enemy.p.insert(0, [Enemy.p[0][0], Enemy.p[0][1] + 1])
            Enemy.p.pop()
        elif Enemy.d == 3:
            Enemy.p.insert(0, [Enemy.p[0][0] - 1, Enemy.p[0][1]])
            Enemy.p.pop()
        elif Enemy.d == 4:
            Enemy.p.insert(0, [Enemy.p[0][0] + 1, Enemy.p[0][1]])
            Enemy.p.pop()
        elif Enemy.alive == 0:
            Enemy.d = 0
    def WallCheck():
        if Enemy.p[0][0] <= 2 and Enemy.p[0][1] <= 2 and Enemy.WCcount == 0:
            pass
        if Enemy.p[0][0] <= 2 and Enemy.WCcount == 0:
            Enemy.d = random.randint(1,2)
            Enemy.count = 0
            Enemy.WCcount += 1
        elif Enemy.p[0][0] >= 39 and Enemy.WCcount == 0:
            Enemy.d = random.randint(1,2)
            Enemy.count = 0
            Enemy.WCcount += 1
        elif Enemy.p[0][1] <= 2 and Enemy.WCcount == 0:
            Enemy.d = random.randint(3,4)
            Enemy.count = 0
            Enemy.WCcount += 1
        elif Enemy.p[0][1] >= 39 and Enemy.WCcount == 0:
            Enemy.d = random.randint(3,4)
            Enemy.count = 0
            Enemy.WCcount += 1
        elif Enemy.p[0][0] <= 2 or Enemy.p[0][0] >= 39 or Enemy.p[0][1] <= 2 or Enemy.p[0][1] >= 39:
            Enemy.WCcount += 1
            Enemy.count = 0
        if Enemy.WCcount == 10:
            if Enemy.p[0][0] <= 2:
                Enemy.d = 4
            elif Enemy.p[0][0] >= 39:
                Enemy.d = 3
            elif Enemy.p[0][1] <= 2:
                Enemy.d = 2
            elif Enemy.p[0][1] >= 39:
                Enemy.d = 1
            Enemy.WCcount = 0
def gameover(reason): # printing game over letter
    font1 = pygame.font.Font(None,60)
    font2 = pygame.font.Font(None,30)
    text1 = font1.render("GAME OVER",True,(255,0,0))
    if reason == 'wall':
        text2 = font2.render("Your snake hit the wall hard.",True,(222,23,56))
    elif reason == 'twisted':
        text2 = font2.render("Your snake twisted itself.",True,(222,23,56))
    elif reason == 'defeated':
        text2 = font2.render("Your snake was defeated by the enemy snake.",True,(222,23,56))
    SURFACE.blit(text1,(120,200))
    SURFACE.blit(text2,(30,270))
def restart():  # reset or restart. press R
    Player.p[0] = [20,20]
    Player.alive = 1
    Player.d = 4
    j = 0
    for i in range(len(Player.p) - 3):
        del Player.p[1]
    Enemy.p[0] = [0,0]
def main():
    Food.setpos()
    while True:
        for event in pygame.event.get():
            if event.type == KEYDOWN:   # key bindings
                if event.key == K_UP:
                    if Player.d != 2:
                        Player.d = 1
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_DOWN:
                    if Player.d != 1:
                        Player.d = 2
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_LEFT:
                    if Player.d != 4:
                        Player.d = 3
                    if Player.alive == 0:
                        Player.d = 0
                elif event.key == K_RIGHT:
                    if Player.d != 3:
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
        if len(Player.p) >= 6:
            Enemy.SetStartPos()
            Enemy.draw()
            Enemy.WallCheck()
            Enemy.move()
            Enemy.count += 1
            if Enemy.count == 10:
                Enemy.count = 0
                Enemy.SetDirection()
        Scoreboard.draw()
        Player.move()
        Player.EnemyCheck()
        Player.FoodCheck()
        if Player.p[0][0] < 1 or Player.p[0][0] > 40 or Player.p[0][1] < 1 or Player.p[0][1] > 40:
            # death by going out of the ground
            Player.alive = 0
            Player.d = 0
            gameover('wall')
        j = 0
        for i in Player.p: # death by twisting
            if j != 0:
                if Player.p[0] == i:
                    Player.alive = 0
                    Player.d = 0
                    gameover('twisted')
            j += 1
        if Player.alive == -1:
            gameover('defeated')
        FPSCLOCK.tick(10)
            
        pygame.display.update()


if __name__ == '__main__':
    main()

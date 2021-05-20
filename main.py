import math
import pygame
from pygame import mixer

import random

# pygame.init()
# #tao kich thuoc nen
# screen = pygame.display.set_mode((640,800))
#
# #tieu de va bieu tuong
# pygame.display.set_caption("Ban ga")
# icon = pygame.image.load('1/images/chicken.png')
# pygame.display.set_icon(icon)
#
# #nguoichoi
# playerh = pygame.image.load('1/images/space-ship1.png')
# playerx = 300
# playery = 700
# playerx_change = 0
#
# #conga
# hinhga = []
# gax = []
# gay = []
# gax_change = []
# gay_change = []
# soluong = 6
# for i in range(soluong):
#     hinhga.append(pygame.image.load('1/images/ga.png'))
#     gax.append(random.randint(0,590))
#     gay.append(random.randint(10,60))
#     gax_change.append(0.3)
#     gay_change.append(10)
#
# #dan
# dan = pygame.image.load('1/images/bullet.png')
# danx = 0
# dany = 700
# danx_change = 0
# dany_change = 2
# dan_trangthai = "ready"
#
# #diem
# score_vl = 0
# font = pygame.font.Font('freesansbold.ttf', 32)
# textx=10
# texty=10
#
# #hinhnen
# bg = pygame.image.load('1/images/65d32c0b80b35558e265a8d007c98ce3.jpg')
#
# #vị trí xuất hiện con gà
# def ga(x,y,i):
#     screen.blit(hinhga[i], (x,y))
#
# #vị trí người chơi
# def player(x,y):
#     screen.blit(playerh, (x,y))
#
# #bắn đạn
# def fire_d(x,y):
#     global dan_trangthai
#     dan_trangthai = "fire"
#     screen.blit(dan, (x+16, y+10))
#
# #
# def banga (gax, gay, danx, dany):
#     khoangcach = math.sqrt((math.pow(gax - danx,2)) + (math.pow(gay - dany,2)))
#     if khoangcach <27:
#         return True
#     else:
#         return  False
#
# #bang diem
# def show_score(x,y):
#     score = font.render("Score : " + str(score_vl),True, (255,255,255))
#     screen.blit(score,(x,y))
# #chạy game
# running = True
# while running:
#
#     #chỉnh màu nền
#     screen.fill((0, 0, 0))
#     screen.blit(bg, (0,0))
#
#     #tạo nút thoát game
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#         #điểu khiển người chơi
#         if event.type == pygame.KEYDOWN:
#             #dieu khien tau di trai phai
#             if event.key == pygame.K_LEFT:
#                 playerx_change = -0.5
#             if event.key == pygame.K_RIGHT:
#                 playerx_change = 0.5
#
#             #nút cách để bắn đạn
#             if event.key == pygame.K_SPACE:
#                 danx=playerx
#                 fire_d(danx, dany)
#
#         if event.type == pygame.KEYUP:
#             if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
#                 playerx_change = 0
#
#     playerx += playerx_change
#
#     #tạo giới hạn di chuyển cho tàu
#     if playerx <=0:
#         playerx=0
#     elif playerx >=570:
#         playerx = 570
#
#     #tạo chuyển động cho gà
#     for i in range(soluong):
#         gax[i] += gax_change[i]
#         if gax[i] <= 0:
#             gax_change[i] = 0.3
#             gay[i] += gay_change[i]
#         elif gax[i] >= 570:
#             gax_change[i] = -0.3
#             gay[i] += gay_change[i]
#
#         ban = banga(gax[i], gay[i], danx, dany)
#         if ban:
#             dany = 480
#             dan_trangthai = "ready"
#             score_vl += 1
#             gax[i] = random.randint(0, 590)
#             gay[i] = random.randint(10, 80)
#
#         ga(gax[i], gay[i], i)
#
#     #tạo đạn khi bắn
#     if dany <=0:
#         dany = 700
#         dan_trangthai = "ready"
#     if dan_trangthai == "fire":
#         fire_d(danx,dany)
#         dany -= dany_change
#
#
#
#     show_score(textx,texty)
#     player(playerx,playery)
#     pygame.display.update()

class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.image = pygame.image.load("media/images/space_ship.png")
        self.imageWith = 100
        self.imageHeight = 93

        self.health = 5
        self.speed = 2


class Game:
    def __init__(self):
        # khoi tao pygame
        pygame.init()

        # trang thai cua game
        self.__gameState = "intro"

        # kich co man hinh
        self.__screenWidth = 1280
        self.__screenHeight = 800

        # tao cua so game
        self.__screen = pygame.display.set_mode((self.__screenWidth, self.__screenHeight))
        icon = pygame.image.load("media/images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Chicken Invaders")

        # tao va set player o vi tri (x, y) (o giua + phia duoi man hinh)
        self.player = Player(self.__screenWidth/2 - 100/2, self.__screenHeight/2 - 93/2 + 330)


    def playIntro(self):
        # load nhac nen intro
        mixer.music.load("Media/Sounds/welcome_background_music.wav")
        mixer.music.play(-1)

        # load intro background image
        backgroundImage = pygame.image.load("media/images/galaxy_background_pixel_1280x800.jpg")
        introText = pygame.image.load("media/images/intro_text.png")
        introTitle = pygame.image.load("media/images/intro_title.png")
        introAuthor = pygame.image.load("media/images/intro_author.png")

        # hien thi thong tin o man hinh intro
        self.__screen.blit(backgroundImage, (0, 0))
        self.__screen.blit(introText, (((self.__screenWidth/2) - 750/2), (self.__screenHeight/2) - 31/2 + 350))
        self.__screen.blit(introTitle, (((self.__screenWidth/2) - 914/2), (self.__screenHeight/2) - 80/2 - 100))
        self.__screen.blit(introAuthor, (((self.__screenWidth/2) - 750/2 + 80), (self.__screenHeight / 2) - 31/2 + 200))
        pygame.display.update()

        gameIsBeingOpened = True
        while (gameIsBeingOpened):

            # su kien tat cua so
            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingOpened = False
                    pygame.quit()

            # lang nghe
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RETURN]:
                # thay doi state cua game
                self.__gameState = "play"
                gameIsBeingOpened = False


    def playGame(self):
        # load nhac nen gameplay
        mixer.music.load("Media/Sounds/game_play_background_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.image.load("media/images/play_background.jpg")
        self.__screen.blit(backgroundImage, (0, 0))

        # load player's spaceship image
        spaceship = pygame.image.load("media/images/space_ship.png")


        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            # Vong lap game: Su kien thay doi -> cap nhat va xu li thong tin -> ve lai game -> Su kien thay doi ...

            # su kien tat cua so window
            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()

            ### lien tuc lang nghe su kien va thay doi:
            # di chuyen player
            keys = pygame.key.get_pressed()
            if (keys[pygame.K_LEFT] and (self.player.x > 0)):
                self.player.x -= self.player.speed
            if (keys[pygame.K_RIGHT] and (self.player.x < (self.__screenWidth - 100))):
                self.player.x += self.player.speed

            #### lien tuc ve lai game
            self.__screen.blit(backgroundImage ,(0, 0))
            self.__screen.blit(spaceship, (self.player.x, self.player.y))
            pygame.display.update()
            print(self.player.x, self.player.y)


    def start(self):
        while (True):
            if (self.__gameState == "intro"):
                self.playIntro()
            elif (self.__gameState == "play"):
                self.playGame()

gameOb = Game()
gameOb.start()
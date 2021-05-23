import random

import pygame
from pygame import mixer


# cac bien toan cuc
SPRITEGROUP = pygame.sprite.Group()

SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800



class Egg(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/egg/egg_-100.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_0.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_100.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_0.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-10.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-20.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-30.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-40.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-50.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-60.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-70.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-80.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-90.png"))
        self.sprites.append(pygame.image.load("media/images/egg/egg_-100.png"))

        self.current_sprite = 0

        self.IMAGE_INTERVAL = 20
        self.last_update_animation = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH)
        self.rect.y = 0

        self.health = 10
        self.speed = 1

    def update(self):
        self.rect.y += self.speed

        # neu ra khoi man hinh thi se xuat hien lai
        if (self.rect.y > SCREEN_HEIGHT):
            self.rect.x = random.randint(0, SCREEN_WIDTH)
            self.rect.y = 0

        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))


class Laser(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/pixel_laser_yellow.png"))
        self.sprites.append(pygame.image.load("media/images/pixel_laser_blue.png"))
        self.sprites.append(pygame.image.load("media/images/pixel_laser_red.png"))
        self.sprites.append(pygame.image.load("media/images/pixel_laser_green.png"))

        self.current_sprite = -1
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 90))

        self.IMAGE_INTERVAL = 100
        self.last_update_animation = 0

        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.speed = 8

        self.sound = mixer.Sound("media/sounds/shoot.wav")
        self.sound.play()

    def update(self):
        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 90))

        self.rect.y -= self.speed

        # neu ra khoi man hinh thi se bi xoa
        if (self.rect.y < -10):
            SPRITEGROUP.remove(self)




class Player(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-100.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_0.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_100.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_0.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-10.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-20.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-30.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-40.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-50.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-60.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-70.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-80.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-90.png"))
        self.sprites.append(pygame.image.load("media/images/player/space_ship_-100.png"))

        self.IMAGE_INTERVAL = 10
        self.last_update_animation = 0

        self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 93))

        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

        self.health = 5
        self.speed = 3

    def update(self):
        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (100, 93))


class Game():

    def __init__(self):
        pygame.init()

        # spritegroup object
        #self.spritegroup = pygame.sprite.Group()

        # trang thai cua game
        self.__gameState = "intro"

        # FPS
        self.__FPS = 144

        # score and level
        self.__score = 0
        self.__level = 1

        # tao cua so game
        self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        icon = pygame.image.load("media/images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Chicken Invaders")

        # tao va set player o vi tri (x, y) (o giua + phia duoi man hinh)
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)
        SPRITEGROUP.add(self.player)


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
        self.__screen.blit(introText, (((SCREEN_WIDTH/2) - 750/2), (SCREEN_HEIGHT/2) - 31/2 + 350))
        self.__screen.blit(introTitle, (((SCREEN_WIDTH/2) - 914/2), (SCREEN_HEIGHT/2) - 80/2 - 100))
        self.__screen.blit(introAuthor, (((SCREEN_WIDTH/2) - 750/2 + 80), (SCREEN_HEIGHT / 2) - 31/2 + 200))
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
        mixer.music.load("media/sounds/game_play_background_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.transform.scale(pygame.image.load("media/images/play_background.jpg"), (1280, 800))

        # khai bao clock
        clock = pygame.time.Clock()

        # level 1
        # sinh egg
        for i in range(0, 8):
            SPRITEGROUP.add(Egg())

        # --------------------------------------------------------------------------------------------------------------
        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            # Vong lap game: Su kien thay doi -> cap nhat va xu li thong tin -> ve lai game -> Su kien thay doi ...

            # thiet lap FPS
            clock.tick(self.__FPS)

            # su kien tat cua so window
            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        SPRITEGROUP.add(Laser(self.player.rect.x, self.player.rect.y))
            # ----------------------------------------------------------------------------------------------------------
            ### lien tuc lang nghe su kien va thay doi:



            keys = pygame.key.get_pressed()
            # di chuyen player
            if (keys[pygame.K_LEFT] and (self.player.rect.x > 0)):
                self.player.rect.x -= self.player.speed
            elif (keys[pygame.K_RIGHT] and (self.player.rect.x < (SCREEN_WIDTH - self.player.image.get_width()))):
                self.player.rect.x += self.player.speed
            elif (keys[pygame.K_UP] and self.player.rect.y > 0):
                self.player.rect.y -= self.player.speed
            elif (keys[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - self.player.image.get_height())):
                self.player.rect.y += self.player.speed

            # ----------------------------------------------------------------------------------------------------------
            #### lien tuc ve lai game

            # ve thong tin diem so cua player
            mainFont = pygame.font.SysFont("comicsans", 40)
            scoreLabel = mainFont.render(f"Score: {self.__score}", 1, (255, 255, 255))
            self.__screen.blit(scoreLabel, (0, 0))
            # ve thong tin health cua player
            healthOfPlayerLabel = mainFont.render(f"Player's health: {self.player.health}", 1, (255, 255, 255))
            self.__screen.blit(healthOfPlayerLabel, (0, 770))
            # ve thong tin level
            levelLabel = mainFont.render(f"Level: {self.__level}", 1, (255, 255, 255))
            self.__screen.blit(levelLabel, (1175, 0))

            pygame.display.update()
            self.__screen.blit(backgroundImage, (0, 0))
            SPRITEGROUP.draw(self.__screen)
            SPRITEGROUP.update()
            # ----------------------------------------------------------------------------------------------------------


    def start(self):
        while (True):
            if (self.__gameState == "intro"):
                self.playIntro()
            elif (self.__gameState == "play"):
                self.playGame()

gameOb = Game()
gameOb.start()
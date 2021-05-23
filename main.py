import random
import pygame
from pygame import mixer
import time

# list objects trong game
level1 = pygame.sprite.Group()
level2 = pygame.sprite.Group()

level1Enemies = pygame.sprite.Group()
level2Enemies = pygame.sprite.Group()
lazerList = pygame.sprite.Group()

# cac bien toan cuc
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 800

LEVEL = 0
SCORE = 0

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


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

        self.IMAGE_INTERVAL = random.randint(10, 80)
        self.last_update_animation = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = random.randint(-800, 0)

        self.health = 5
        self.speed = random.randint(1, 5)

    def update(self, ):
        self.rect.y += self.speed

        # neu ra khoi man hinh thi se xuat hien lai
        if (self.rect.y > SCREEN_HEIGHT):
            self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
            self.rect.y = random.randint(-800, 0)
            self.speed = random.randint(1, 5)

        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))

        # khi lazer ban trung egg
        for lazer in lazerList:
            if (pygame.sprite.collide_rect(self, lazer)):
                lazerList.remove(lazer)
                self.health -= 1
                if (self.health == 0):
                    level1Enemies.remove(self)
                    self.sound = mixer.Sound("media/sounds/explosion.wav")
                    self.sound.play()
                    global SCORE
                    SCORE += 1
                    if not level1Enemies:
                        mixer.music.load("media/sounds/level_complete.wav")
                        mixer.music.play()
                        completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                        SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                        pygame.display.update()
                        time.sleep(10)
                        global LEVEL
                        LEVEL = 2
                        pygame.display.update()

class UFO_2(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.sprites = []
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-100.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_0.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_100.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_0.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-10.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-20.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-30.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-40.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-50.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-60.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-70.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-80.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-90.png"))
        self.sprites.append(pygame.image.load("media/images/ufo/ufo_-100.png"))

        self.current_sprite = 0

        self.IMAGE_INTERVAL = random.randint(10, 80)
        self.last_update_animation = 0

        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))
        self.rect = self.image.get_rect()
        self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.width)
        self.rect.x = random.randint(-800, 0)

        self.health = 5
        self.speed = random.randint(1, 2)

    def update(self, ):
        self.rect.x += self.speed

        # neu ra khoi man hinh thi se xuat hien lai
        if (self.rect.x > SCREEN_WIDTH):
            self.rect.y = random.randint(0, SCREEN_HEIGHT - self.rect.width)
            self.rect.x = random.randint(-800, 0)
            self.speed = random.randint(1, 2)

        if pygame.time.get_ticks() - self.last_update_animation > self.IMAGE_INTERVAL:
            self.current_sprite += 1
            self.last_update_animation = pygame.time.get_ticks()

        # reset hoat anh
        if (self.current_sprite >= len(self.sprites)):
            self.current_sprite = 0
        self.image = pygame.transform.scale(self.sprites[self.current_sprite], (64, 64))

        # khi lazer ban trung UFO_2
        for lazer in lazerList:
            if (pygame.sprite.collide_rect(self, lazer)):
                lazerList.remove(lazer)
                self.health -= 1
                if (self.health == 0):
                    level2Enemies.remove(self)
                    self.sound = mixer.Sound("media/sounds/explosion.wav")
                    self.sound.play()
                    global SCORE
                    SCORE += 1
                    if not level2Enemies:
                        mixer.music.load("media/sounds/level_complete.wav")
                        mixer.music.play()
                        completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                        SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                        pygame.display.update()
                        time.sleep(10)
                        global LEVEL
                        LEVEL = 3
                        pygame.display.update()

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

        self.speed = 7

        self.sound = mixer.Sound("media/sounds/shot.wav")
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
            lazerList.remove(self)




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

        # neu player cham vao egg
        global SCORE
        for egg in level1Enemies:
            if (pygame.sprite.collide_rect(self, egg)):
                self.sound = mixer.Sound("media/sounds/playerbehit.wav")
                self.sound.play()
                level1Enemies.remove(egg)
                self.health -= 1
                pygame.display.update()

                if (self.health == 0):
                    self.sound = mixer.Sound("media/sounds/game_over_background_music.wav")
                    pygame.mixer.music.stop()
                    gameover_label = pygame.image.load("media/images/gameover_text.png")
                    SCREEN.blit(gameover_label, (SCREEN_WIDTH / 2 - 260, SCREEN_HEIGHT / 2 - 33))
                    pygame.display.update()
                    self.sound.play()
                    time.sleep(10)
                    global LEVEL
                    LEVEL = 0
                    SCORE = 0
                    self.health = 5
                    self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)
                    for enemy in level1Enemies:
                        level1Enemies.remove(enemy)

                elif not level1Enemies:
                    mixer.music.load("media/sounds/level_complete.wav")
                    mixer.music.play()
                    completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                    SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                    pygame.display.update()
                    time.sleep(8)
                    LEVEL = 2
                    pygame.display.update()

        # neu player cham vao UFO_2
        for ufo_2 in level2Enemies:
            if (pygame.sprite.collide_rect(self, ufo_2)):
                self.sound = mixer.Sound("media/sounds/playerbehit.wav")
                self.sound.play()
                level2Enemies.remove(ufo_2)
                self.health -= 1
                pygame.display.update()

                if (self.health == 0):
                    self.sound = mixer.Sound("media/sounds/game_over_background_music.wav")
                    pygame.mixer.music.stop()
                    gameover_label = pygame.image.load("media/images/gameover_text.png")
                    SCREEN.blit(gameover_label, (SCREEN_WIDTH / 2 - 260, SCREEN_HEIGHT / 2 - 33))
                    pygame.display.update()
                    self.sound.play()
                    time.sleep(10)
                    LEVEL = 0
                    SCORE = 0
                    self.health = 5
                    self.rect.center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)
                    for enemy in level2Enemies:
                        level2Enemies.remove(enemy)

                elif not level2Enemies:
                    mixer.music.load("media/sounds/level_complete.wav")
                    mixer.music.play()
                    completedlevel_label = pygame.image.load("media/images/completedlevel_text.png")
                    SCREEN.blit(completedlevel_label, (SCREEN_WIDTH / 2 - 353, SCREEN_HEIGHT / 2 - 26))
                    pygame.display.update()
                    time.sleep(8)
                    LEVEL = 3
                    pygame.display.update()


class Game():

    def __init__(self):
        pygame.init()

        # spritegroup object
        #self.spritegroup = pygame.sprite.Group()

        # trang thai cua game
        self.__gameState = "intro"

        # FPS
        self.__FPS = 144

        # level
        self.__level = 1

        # tao cua so game
        #self.__screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        icon = pygame.image.load("media/images/icon.png")
        pygame.display.set_icon(icon)
        pygame.display.set_caption("Chicken Invaders")

        # tao va set player o vi tri (x, y) (o giua + phia duoi man hinh)
        self.player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2 + 330)


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
        SCREEN.blit(backgroundImage, (0, 0))
        SCREEN.blit(introText, (((SCREEN_WIDTH/2) - 750/2), (SCREEN_HEIGHT/2) - 31/2 + 350))
        SCREEN.blit(introTitle, (((SCREEN_WIDTH/2) - 914/2), (SCREEN_HEIGHT/2) - 80/2 - 100))
        SCREEN.blit(introAuthor, (((SCREEN_WIDTH/2) - 750/2 + 80), (SCREEN_HEIGHT / 2) - 31/2 + 200))
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
                global LEVEL
                LEVEL = 1
                gameIsBeingOpened = False


    def playLevel1(self):
        # add player
        level1.add(self.player)

        # load nhac nen gameplay
        mixer.music.load("media/sounds/level1_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.transform.scale(pygame.image.load("media/images/play_background.jpg"), (1280, 800))

        # khai bao clock
        clock = pygame.time.Clock()

        # ra linh
        for i in range(12):
            level1Enemies.add(Egg())
        # --------------------------------------------------------------------------------------------------------------
        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            # Vong lap game: Su kien thay doi -> cap nhat va xu li thong tin -> ve lai game -> Su kien thay doi ...
            if (LEVEL == 0):
                gameIsBeingPlayed = False
            SCREEN.blit(backgroundImage, (0, 0))
            # thiet lap FPS
            clock.tick(self.__FPS)

            # su kien tat cua so window
            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()

                # player ban lazer bang phim SPACE
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        lazerList.add(Laser(self.player.rect.x, self.player.rect.y))
            # ----------------------------------------------------------------------------------------------------------
            ### lien tuc lang nghe su kien va thay doi:
            keys = pygame.key.get_pressed()
            #global LEVEL
            # di chuyen player
            if (keys[pygame.K_LEFT] and (self.player.rect.x > 0)):
                self.player.rect.x -= self.player.speed
            elif (keys[pygame.K_RIGHT] and (self.player.rect.x < (SCREEN_WIDTH - self.player.image.get_width()))):
                self.player.rect.x += self.player.speed
            elif (keys[pygame.K_UP] and self.player.rect.y > 0):
                self.player.rect.y -= self.player.speed
            elif (keys[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - self.player.image.get_height())):
                self.player.rect.y += self.player.speed
            elif (keys[pygame.K_RETURN] and LEVEL == 2):
                gameIsBeingPlayed = False

            #----------------------------------------------------------------------------------------------------------
            #### lien tuc ve lai game
            # ve thong tin diem so cua player
            mainFont = pygame.font.SysFont("comicsans", 40)
            scoreLabel = mainFont.render(f"Score: {SCORE}", 1, (255, 255, 255))
            SCREEN.blit(scoreLabel, (0, 0))
            # ve thong tin health cua player
            healthOfPlayerLabel = mainFont.render(f"Player's health: {self.player.health}", 1, (255, 255, 255))
            SCREEN.blit(healthOfPlayerLabel, (0, 770))
            # ve thong tin level
            levelLabel = mainFont.render(f"Level: {LEVEL}", 1, (255, 255, 255))
            SCREEN.blit(levelLabel, (1175, 0))
            # ve chi dan qua level 2
            if (LEVEL == 2):
                hdchuyenlv_label = pygame.image.load("media/images/chidanqualevel_text.png")
                SCREEN.blit(hdchuyenlv_label, (SCREEN_WIDTH / 2 - 83, SCREEN_HEIGHT / 2 + 250))

            # draw va update cac SpriteGroup
            level1Enemies.draw(SCREEN)
            level1Enemies.update()

            level1.draw(SCREEN)
            level1.update()

            lazerList.draw(SCREEN)
            lazerList.update()

            pygame.display.update()
            # ----------------------------------------------------------------------------------------------------------

    def playLevel2(self):
        # add player
        level2.add(self.player)
        # load nhac nen gameplay
        mixer.music.load("media/sounds/level2_music.wav")
        mixer.music.play(-1)

        # load playing background image
        backgroundImage = pygame.transform.scale(pygame.image.load("media/images/level2_background.jpg"), (1280, 800))

        # khai bao clock
        clock = pygame.time.Clock()

        # ra linh
        for i in range(12):
            level2Enemies.add(UFO_2())
        # --------------------------------------------------------------------------------------------------------------
        ## day la vong lap game
        gameIsBeingPlayed = True
        while (gameIsBeingPlayed):
            global LEVEL
            if (LEVEL == 0):
                gameIsBeingPlayed = False

            SCREEN.blit(backgroundImage, (0, 0))

            for event in pygame.event.get():
                if (event.type) == pygame.QUIT:
                    gameIsBeingPlayed = False
                    pygame.quit()

                # player ban lazer bang phim SPACE
                elif (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_SPACE):
                        lazerList.add(Laser(self.player.rect.x, self.player.rect.y))
            #-------------------------------------------------------------------------------------------------------
            ### lien tuc lang nghe su kien va thay doi:
            keys = pygame.key.get_pressed()
            #global LEVEL
            # di chuyen player
            if (keys[pygame.K_LEFT] and (self.player.rect.x > 0)):
                self.player.rect.x -= self.player.speed
            elif (keys[pygame.K_RIGHT] and (self.player.rect.x < (SCREEN_WIDTH - self.player.image.get_width()))):
                self.player.rect.x += self.player.speed
            elif (keys[pygame.K_UP] and self.player.rect.y > 0):
                self.player.rect.y -= self.player.speed
            elif (keys[pygame.K_DOWN] and self.player.rect.y < (SCREEN_HEIGHT - self.player.image.get_height())):
                self.player.rect.y += self.player.speed
            elif (keys[pygame.K_RETURN] and LEVEL == 3):
                gameIsBeingPlayed = False
            # ----------------------------------------------------------------------------------------------------------
            #### lien tuc ve lai game
            # ve thong tin diem so cua player
            mainFont = pygame.font.SysFont("comicsans", 40)
            scoreLabel = mainFont.render(f"Score: {SCORE}", 1, (255, 255, 255))
            SCREEN.blit(scoreLabel, (0, 0))
            # ve thong tin health cua player
            healthOfPlayerLabel = mainFont.render(f"Player's health: {self.player.health}", 1, (255, 255, 255))
            SCREEN.blit(healthOfPlayerLabel, (0, 770))
            # ve thong tin level
            levelLabel = mainFont.render(f"Level: {LEVEL}", 1, (255, 255, 255))
            SCREEN.blit(levelLabel, (1175, 0))

            level2Enemies.draw(SCREEN)
            level2Enemies.update()

            level2.draw(SCREEN)
            level2.update()

            lazerList.draw(SCREEN)
            lazerList.update()

            pygame.display.update()
            # ----------------------------------------------------------------------------------------------------------

    def start(self):
        while (True):
            global LEVEL
            if (LEVEL == 0):
                self.playIntro()
            elif (LEVEL == 1):
                self.playLevel1()
            elif (LEVEL == 2):
                self.playLevel2()


gameOb = Game()
gameOb.start()
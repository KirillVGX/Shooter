from pygame import *
from pygame import image as img
import random
font.init()
#import pygame 
#pygame.init() 

window = display.set_mode((700, 500))
display.set_caption('Москаль шутер')
background = transform.scale(image.load('galaxy.jpg'), (700, 500))

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed, width, height):
        super().__init__()
        self.image = transform.scale(img.load(player_image), (width, height))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

bullets = sprite.Group() 
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed

class Player(GameSprite):
    def fire(self):                   # x player.rect.centerx y player.rect.top SPEED   WIDTH  HEIGHT
        bullet = Bullet("bullet.png", player.rect.centerx    ,player.rect.top         , 5     , 5    , 10    )
        bullets.add(bullet)
    '''def firee(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            bullet = Bullet("bullet.png", player.rect.centerx, player.rect.top , 5 , 10 , 20)
            bullet.reset()
            bullet.update()'''

    def update(self):
        keys = key.get_pressed()
        if keys[K_a] and self.rect.x > 1:
            self.rect.x -= self.speed
        if keys[K_d] and self.rect.x < win_width - 95:
            self.rect.x += self.speed
        if keys[K_SPACE]:
            player.fire()
            bullet = Bullet("bullet.png", player.rect.centerx, player.rect.top, 5, 10, 20)
            bullet.reset()
            bullet.update()


class UFO(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.top >= 500:
            self.kill()

class Label(): 
    def __init__(self, x=0, y=0, width=10, height=10, color=None): 
        self.rect = Rect(x, y, width, height)
        self.fill_color = color 
    def color(self, new_color): 
        self.fill_color = new_color 
    def fill(self): 
        draw.rect(window, self.fill_color, self.rect) 
    def outline(self, frame_color, thickness):
        draw.rect(window, frame_color, self.rect, thickness)    
    def collidepoint(self, x, y): 
        return self.rect.collidepoint(x, y)       
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)): 
        self.image = font.SysFont('verdana', fsize).render(text, True, text_color) 
    def draw(self, shift_x=0, shift_y=0): 
        self.fill() 
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y)) 

def pi():
    White = (255, 255, 255) 
    back = (200, 255, 255)
    # Счет
    score_text = Label(0,0,0,0,back) 
    score_text.set_text('Счёт:',25, White) 
    
    score = Label(0,0,0,0,back) 
    score.set_text('0', 25, White) 

    dis_score_text = Label(0,0,0,0,back) 
    dis_score_text.set_text('Пропущено:',25, White)  
    
    dis_score = Label(0,0,0,0,back) 
    dis_score.set_text('0', 25, White) 

a = random.randint(0,600)

ufo = UFO("ufo.png", a, -100, 1, 95, 60)

win_width = 700
win_height = 500

clock = time.Clock()
FPS = 30

player = Player("rocket.png", 275, 417, 6, 95, 80)
#                              x player.rect.centerx, y player.rect.top, SPEED,   WIDTH,  HEIGHT
bullet = Bullet("bullet.png", 275                  , 417              , 5      , 5     , 10    )
 
fontan = font.Font(None, 70)
win = fontan.render('YOU WIN!', True, (215, 215, 0))
lose = fontan.render('YOU LOSE!', True, (180, 0, 0))
bullet = Bullet("bullet.png", player.rect.centerx, player.rect.top, 5, 10, 20)

finish = False
points = 0
dispoints = 0
game = True
while game:
    for i in event.get():
        if i.type == QUIT:
            game = False
        elif i.type == KEYDOWN:
            if i.key == K_SPACE:
                player.fire()
    
    if finish != True:
        keyss = key.get_pressed()
        if keyss[K_SPACE]:
            #bullets.reset()
            bullets.update()
            '''if sprite.collide_rect(ufo, bullets):
                points += 1

        if sprite.collide_rect(ufo, player):
            dispoints += 1  ''' 

        #score.set_text(str(points), 25, White) 
        #score.draw(80,20)
        #dis_score.set_text(str(dispoints), 25, White) 
        #dis_score.draw(170,60)

        window.blit(background, (0, 0))
        player.reset()
        player.update()
   
        #ufo.update()
        #ufo.reset()

        '''score_text.draw(10,20) 
        score.draw(80,20)
        dis_score_text.draw(10,60)
        dis_score.draw(170,60)

        if points >= 30:
            finish = True
            window.blit(win, (200, 200))
        if dispoints >= 20:
            finish = True
            window.blit(lose, (200, 200))'''

    clock.tick(FPS)
    display.update()

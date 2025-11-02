# Create your own shooter
import pygame as gm
from random import randint
gm.init()
gm.mixer.init()
win_width = 700
win_height = 500
mw = gm.display.set_mode((win_width, win_height))
gm.display.set_caption("Shooter game")
img_back = "galaxy.jpg"
img_hero = "rocket.png"
img_enemy = "ufo.png"
img_asteroid = "asteroid.png"
img_bullet = "bullet.png"
img_player2 = "rocket.png"

bg = gm.transform.scale(gm.image.load(img_back), (win_width, win_height))

try:
    gm.mixer.music.load("space.ogg")
    gm.mixer.music.set_volume(0.1)
    gm.mixer.music.play(loops=True)

    fire_sound = gm.mixer.Sound("fire.ogg")
except:
    print("Sound file not found, proceeding without sound...")

gm.font.init()
font1 = gm.font.Font(None, 36)
font2 = gm.font.Font(None, 36)

score = 0  
lost = 0    

class GameSprite(gm.sprite.Sprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__()
        self.image = gm.transform.scale(gm.image.load(img), (width, height))
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    
    def reset(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = gm.key.get_pressed()
        if keys[gm.K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed   
        if keys[gm.K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed

    def fire(self):
        bullet = Bullet(img_bullet, self.rect.centerx - 2, self.rect.top, 10, 20, 15)
        bullets.add(bullet)
        try:
            fire_sound.play()
        except:
            pass 

class Player2(GameSprite):
    def __init__(self, img, x, y, width, height, speed):
        super().__init__(img, x, y, width, height, speed)
        self.last_shot = gm.time.get_ticks()

    def update(self, enemies):
        closest_enemy = None
        closest_dist = float('inf')
        
        for enemy in enemies:
            if enemy.rect.y < self.rect.y:
                dist = abs(enemy.rect.centerx - self.rect.centerx)
                if dist < closest_dist:
                    closest_dist = dist
                    closest_enemy = enemy
        if closest_enemy:
            if self.rect.centerx < closest_enemy.rect.centerx - 5:
                self.rect.x += self.speed
            elif self.rect.centerx > closest_enemy.rect.centerx + 5:
                self.rect.x -= self.speed
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > win_width - 80:
            self.rect.x = win_width - 80

    def auto_fire(self, enemies):
        now = gm.time.get_ticks()
        if now - self.last_shot > 1000: 
            if len(enemies) > 0:
                closest_enemy = None
                closest_dist = float('inf')
                
                for enemy in enemies:
                    if enemy.rect.y < self.rect.y:
                        dist = abs(enemy.rect.centerx - self.rect.centerx)
                        if dist < closest_dist:
                            closest_dist = dist
                            closest_enemy = enemy

                if closest_enemy:
                    bullet = Bullet(img_bullet, self.rect.centerx - 2, self.rect.top, 10, 20, 15)
                    bullets.add(bullet)
                    self.last_shot = now

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        global lost
        if self.rect.y > win_height:
            self.rect.x = randint(80, win_width - 80)
            self.rect.y = 0
            lost += 1

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

ship = Player(img_hero, 5, win_height - 100, 80, 100, 10)
ship2 = Player2(img_player2, win_width - 85, win_height - 100, 80, 100, 5)

monsters = gm.sprite.Group()
asteroids = gm.sprite.Group()
bullets = gm.sprite.Group()

for i in range(3):
    monster = Enemy(
        img_enemy,
        randint(80, win_width - 80),
        -40,
        80, 50,
        randint(1, 5)
    )
    monsters.add(monster)

for i in range(2):
    asteroid = Enemy(
        img_asteroid,
        randint(80, win_width - 80),
        -40,
        80, 50,
        randint(1, 3)
    )
    asteroids.add(asteroid)


finish = False
run = True
clock = gm.time.Clock()
def show_end_screen(text, color):
    end_text = font1.render(text, True, color)
    mw.blit(end_text, (win_width // 2 - end_text.get_width() // 2, win_height // 2 - 20))
    gm.display.update()
    gm.time.delay(3000) 

while run:
    for e in gm.event.get():
        if e.type == gm.QUIT:
            run = False
        elif e.type == gm.KEYDOWN:
            if e.key == gm.K_SPACE:
                ship.fire()

    if not finish:
        mw.blit(bg, (0, 0))


        text = font1.render("Score: " + str(score), True, (255, 255, 255))
        mw.blit(text, (10, 20))

        text_lose = font2.render("Missed: " + str(lost), True, (255, 255, 255))
        mw.blit(text_lose, (10, 50))

        ship.update()
        ship2.update(monsters)
        ship2.auto_fire(monsters)
        monsters.update()
        asteroids.update()
        bullets.update()
        ship.reset()
        ship2.reset()
        monsters.draw(mw)
        asteroids.draw(mw)
        bullets.draw(mw)
        hits = gm.sprite.groupcollide(monsters, bullets, True, True)
        score += len(hits)


        if gm.sprite.spritecollide(ship, monsters, False) or gm.sprite.spritecollide(ship, asteroids, False):
            finish = True
            show_end_screen("YOU LOSE!", (255, 0, 0))

        if gm.sprite.spritecollide(ship2, monsters, False) or gm.sprite.spritecollide(ship2, asteroids, False):
            finish = True
            show_end_screen("YOU LOSE!", (255, 0, 0))


        if lost >= 3:
            finish = True
            show_end_screen("YOU LOSE!", (255, 0, 0))


        if score >= 10:
            finish = True
            show_end_screen("YOU WIN!", (0, 255, 0))

        if len(monsters) < 3:
            monster = Enemy(
                img_enemy,
                randint(80, win_width - 80),
                -40,
                80, 50,
                randint(1, 5)
            )
            monsters.add(monster)

        if len(asteroids) < 2:
            asteroid = Enemy(
                img_asteroid,
                randint(80, win_width - 80),
                -40,
                80, 50,
                randint(1, 3)
            )
            asteroids.add(asteroid)

        gm.display.update()

    clock.tick(60)  


gm.quit()
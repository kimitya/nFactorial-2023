import pygame
from pygame import *
import time
   
pygame.init()


BLACK = (0, 0, 0)
WHITE = (255,255,255)
HEIGHT = 640
WIDTH = 800

def changefile (a, b):
    filename = "levels/savedlevel.txt"
    row_index = a  
    new_row_data = b  

    with open(filename, "r") as f:
        lines = f.readlines()

    line_to_modify = lines[row_index]

    lines[row_index] = new_row_data + "\n"

    with open(filename, "w") as f:
        f.writelines(lines)

filename = "savedlevel.txt" 
with open(filename, "r") as f:
        lines = f.readlines()       
cnt = int(lines[0])

BACKGROUND_COLOR = (26,51,0)
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("fireboy & watergirl")
background = pygame.image.load("images/background.jpg")

timer = pygame.time.Clock()

PLATFORM_WIDTH = 32
PLATFORM_HEIGHT = 32
PLATFORM_COLOR = (51,102,0)

all_sprites = pygame.sprite.Group()

font = pygame.font.SysFont("Verdana", 80)
game_over = font.render("Game Over", True, BLACK)
game_over_rect = game_over.get_rect().center

pause_txt = font.render("Pause", True, BLACK)
pause_txt_rect = pause_txt.get_rect().center

i=1
pygame.mixer.init()
pygame.mixer.music.load(f"music/music{i}.mp3")
pygame.mixer.music.play(-1)

class Water (pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("images/water.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x * 32
        self.rect.y = y * 32
        
class Fire (pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("images/fire.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x * 32
        self.rect.y = y * 32
        
class Swamp (pygame.sprite.Sprite):
    def __init__(self, x,y):
        super().__init__()
        self.image = pygame.image.load("images/swamp.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x * 32
        self.rect.y = y * 32
        
class RedDoor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/reddoor.png")
        self.rect = self.image.get_rect()
        self.rect.x = x*32
        self.rect.y = y*32
class BlueDoor(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/bluedoor.png")
        self.rect = self.image.get_rect()
        self.rect.x = x*32
        self.rect.y = y*32
class Button(pygame.sprite.Sprite):
    def __init__(self,x,y):
         super().__init__()
         self.image = pygame.surface.Surface((32, 32), pygame.SRCALPHA, 32)
         pygame.draw.circle(self.image, "Grey", (16, 16), 16)
         pygame.draw.circle(self.image, "Green", (16, 16), 12)
         self.rect = self.image.get_rect()
         self.rect.x = x * 32
         self.rect.y = y * 32
class Lift(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.surface.Surface((32, 64))
        pygame.draw.rect(self.image, "White", (0, 0, 32, 64))
        self.rect = self.image.get_rect()
        self.rect.x = x * 32
        self.rect.y = y * 32
        self.x1 = x * 32
        self.y1 = y * 32
    def move(self, x2, y2, t):
        if self.rect.y <= y2:
            self.rect.y = y2
        if self.rect.y >= self.y1:
            self.rect.y = self.y1
        if t:
            self.rect.move_ip(0, -4)
        elif not t:
            self.rect.move_ip(0, 4)
        

class Wall (pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/block.jpg")
        self.rect = self.image.get_rect()
        self.rect.x = x * 32
        self.rect.y = y * 32

class Level (object):
    def __init__(self, player):
        self.platform_list = pygame.sprite.Group()
        self.water_list = pygame.sprite.Group()
        self.fire_list = pygame.sprite.Group()
        self.swamp_list = pygame.sprite.Group()
        self.reddoor_list = pygame.sprite.Group()
        self.bluedoor_list = pygame.sprite.Group()
        self.button_list = pygame.sprite.Group()
        self.lift_list = pygame.sprite.Group()
        self.player = player
    
    def update(self):
        self.platform_list.update()
        self.water_list.update()
        self.fire_list.update()
        self.swamp_list.update()
        self.reddoor_list.update()
        self.bluedoor_list.update()
        self.button_list.update()
        self.lift_list.update()
        
        
    def draw(self,screen):
        screen.blit(background,(0,0))
        self.water_list.draw(screen)
        self.lift_list.draw(screen)
        self.platform_list.draw(screen)
        self.fire_list.draw(screen)
        self.swamp_list.draw(screen)
        self.reddoor_list.draw(screen)
        self.bluedoor_list.draw(screen)
        self.button_list.draw(screen)
        


class Level_00(Level):
    global all_sprites
    def __init__(self,player):
        # super().__init__(player)
        Level.__init__(self,player)
        a=open("levels/level0.txt", "r")
        for y in range(0, HEIGHT//PLATFORM_HEIGHT+1):
            for x in range(0, WIDTH//PLATFORM_WIDTH+1):
                k = a.read(1)
                if k == '-':
                    block = Wall (x,y)
                    self.platform_list.add(block)
                    all_sprites.add(block)
                if k == '*': 
                    swamp = Swamp (x,y)
                    self.swamp_list.add(swamp)
                    all_sprites.add(swamp)
                if k == '@':
                    water = Water (x,y)
                    self.water_list.add(water)
                    all_sprites.add(water)
                if k == '&':
                    fire = Fire (x,y)
                    self.fire_list.add(fire)
                    all_sprites.add(fire)
                if k == ':':
                    reddoor= RedDoor(x,y)
                    self.reddoor_list.add(reddoor)
                    all_sprites.add(reddoor)
                if k == ';':
                    bluedoor= BlueDoor(x,y)
                    self.bluedoor_list.add(bluedoor)
                    all_sprites.add(bluedoor)
                if k == 'o':
                    button = Button(x,y)
                    self.button_list.add(button)
                    all_sprites.add(button)
                    
class Level_01(Level):
    global all_sprites
    def __init__(self,player):
        Level.__init__(self,player)
        a=open("levels/level1.txt", "r")
        for y in range(0, HEIGHT//PLATFORM_HEIGHT+1):
            for x in range(0, WIDTH//PLATFORM_WIDTH+1):
                k = a.read(1)
                if k == '-':
                    block = Wall (x,y)
                    self.platform_list.add(block)
                    all_sprites.add(block)
                if k == '*': 
                    swamp = Swamp (x,y)
                    self.swamp_list.add(swamp)
                    all_sprites.add(swamp)
                if k == '@':
                    water = Water (x,y)
                    self.water_list.add(water)
                    all_sprites.add(water)
                if k == '&':
                    fire = Fire (x,y)
                    self.fire_list.add(fire)
                    all_sprites.add(fire)
                if k == ':':
                    reddoor= RedDoor(x,y)
                    self.reddoor_list.add(reddoor)
                    all_sprites.add(reddoor)
                if k == ';':
                    bluedoor= BlueDoor(x,y)
                    self.bluedoor_list.add(bluedoor)
                    all_sprites.add(bluedoor)
                if k == 'o':
                    button = Button(x,y)
                    self.button_list.add(button)
                    all_sprites.add(button)
                if k == "L":
                    self.lift = Lift(x,y)
                    self.lift_list.add(self.lift)
                    all_sprites.add(self.lift)
                    
         
    def update(self):
        super().update()
    def draw(self, screen):
        super().draw(screen) 


class Player(pygame.sprite.Sprite):
	right = True

	def __init__(self, name):
		
		super().__init__()
		self.image = pygame.image.load(name)
		self.rect = self.image.get_rect()
		self.change_x = 0
		self.change_y = 0

	def update(self):
		self.calc_grav()
		self.rect.x += self.change_x


		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.change_x > 0:
				self.rect.right = block.rect.left
			elif self.change_x < 0:
				self.rect.left = block.rect.right

		self.rect.y += self.change_y

		block_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		for block in block_hit_list:
			if self.change_y > 0:
				self.rect.bottom = block.rect.top
			elif self.change_y < 0:
				self.rect.top = block.rect.bottom

			self.change_y = 0
   
	def calc_grav(self):
		if self.change_y == 0:
			self.change_y = 1
		else:
			self.change_y += .95
		if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
			self.change_y = 0
			self.rect.y = HEIGHT - self.rect.height

	def jump(self):
		self.rect.y += 10
		platform_hit_list = pygame.sprite.spritecollide(self, self.level.platform_list, False)
		self.rect.y -= 10

		if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
			self.change_y = -16


	def go_left(self):
		self.change_x = -9 
		if(self.right): 
			self.flip()
			self.right = False

	def go_right(self):
		self.change_x = 9
		if (not self.right):
			self.flip()
			self.right = True


	def stop(self):
		self.change_x = 0

	def flip(self):
		self.image = pygame.transform.flip(self.image, True, False)


running = True
paused = False
player1 = Player('images/fireboy.png')
player2 = Player('images/watergirl.png')

level_list = []

level_list.append(eval(f'Level_0{cnt}(player1)'))
level_list.append(eval(f'Level_0{cnt}(player2)'))


current_level_no = 0
current_level = level_list[current_level_no]

active_sprite_list = pygame.sprite.Group()
player1.level = current_level
player2.level = current_level
player1.rect.x = int(lines[1])
player1.rect.y = int(lines[2])
player2.rect.x = int(lines[3])
player2.rect.y = int(lines[4])
active_sprite_list.add(player1)
active_sprite_list.add(player2)


while running:
    SCREEN.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running=False
            pygame.quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and paused == False:
                paused = True
            elif event.key == pygame.K_SPACE and paused == True:
                paused = False
                
            if event.key == pygame.K_с:
                changefile(0,str(cnt))
                changefile(1,str(player1.rect.x))
                changefile(2,str(player1.rect.y))
                changefile(3,str(player2.rect.x))
                changefile(4,str(player2.rect.y))
                
            if event.key == pygame.K_LEFT:
                player1.go_left()
            if event.key == pygame.K_RIGHT:
                player1.go_right()
            if event.key == pygame.K_UP:
                player1.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT and player1.change_x < 0:
                player1.stop()
            if event.key == pygame.K_RIGHT and player1.change_x > 0:
                player1.stop()
                
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player2.go_left()
            if event.key == pygame.K_d:
                player2.go_right()
            if event.key == pygame.K_w:
                player2.jump()
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a and player2.change_x < 0:
                player2.stop()
            if event.key == pygame.K_d and player2.change_x > 0:
                player2.stop()
         
    if paused == False:
        pygame.mixer.music.unpause()
        active_sprite_list.update()
        current_level.update()
    elif paused == True:
        pygame.mixer.music.pause()
        SCREEN.fill('light blue')
        SCREEN.blit(pause_txt, (WIDTH//2 - pause_txt_rect[0],HEIGHT//2 - pause_txt_rect[1]))
        pygame.display.update()
        
    if player1.rect.right > WIDTH:
        player1.rect.right = WIDTH
    if player1.rect.left < 0:
        player1.rect.left = 0
        
    if player2.rect.right > WIDTH:
        player2.rect.right = WIDTH
    if player2.rect.left < 0:
        player2.rect.left = 0
        
    if pygame.sprite.spritecollideany(player1, current_level.reddoor_list) and pygame.sprite.spritecollideany(player2, current_level.bluedoor_list):
        for i in all_sprites:
            i.kill()
        level_list = []
        cnt += 1
        cnt %= 2
        level_list.append(eval(f"Level_0{cnt}(player1)"))
        level_list.append(eval(f'Level_0{cnt}(player2)'))
        current_level = level_list[current_level_no]
        player1.level = current_level
        player2.level = current_level
        player1.rect.x = 100
        player1.rect.y = 550
        player2.rect.x = 80
        player2.rect.y = 550
        time.sleep(1)
    
    if pygame.sprite.spritecollideany(player1, current_level.button_list) or pygame.sprite.spritecollideany(player2, current_level.button_list):
        t = True
    else:
        t = False
    if cnt == 1:
        current_level.lift.move(9*32, 9*32, t)
    
    lift_hit_list = pygame.sprite.spritecollide(player1, player1.level.lift_list, False)
    for lift in lift_hit_list:
        if player1.change_x > 0:
            player1.rect.right = lift.rect.left
        elif player1.change_x < 0:
            player1.rect.left = lift.rect.right
    lift_hit_list = pygame.sprite.spritecollide(player2, player2.level.lift_list, False)

    for lift in lift_hit_list:
        if player2.change_x > 0:
            player2.rect.right = lift.rect.left
        elif player2.change_x < 0:
            player2.rect.left = lift.rect.right
            
    if pygame.sprite.spritecollideany(player1, current_level.water_list) or pygame.sprite.spritecollideany(player2, current_level.fire_list) or pygame.sprite.groupcollide(active_sprite_list, current_level.swamp_list, False, False):
          i=2
          pygame.mixer.music.load(f"music/music{i}.mp3")
          pygame.mixer.music.play()
          for i in all_sprites:
            i.kill()
          SCREEN.fill('red')
          player1.kill()
          player2.kill()
          SCREEN.blit(game_over, (WIDTH//2 - game_over_rect[0],HEIGHT//2 - game_over_rect[1]))
          pygame.display.update()
          for entity in active_sprite_list:
            entity.kill() 
          time.sleep(2)
          pygame.quit()

    if paused == False:    
        current_level.draw(SCREEN)
        active_sprite_list.draw(SCREEN)
    timer.tick(30)
    
    
    pygame.display.update()
    


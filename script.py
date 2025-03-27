import pygame
import scipy as sp

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption('Jans Shooter Game')

# set framerate
clock = pygame.time.Clock()
FPS = 60

# define player actions variables
moving_left = False
moving_right = False 

BG = (144, 201, 120)

def draw_bg():
    screen.fill(BG)



class Soldier(pygame.sprite.Sprite):
    def __init__(self, char_type, x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.update_time = pygame.time.get_ticks() 
        self.frame_index = 0
        self.animation_list = []
        for i in range(9):
            img = pygame.image.load(f"img\{char_type}\idle\{i}.png")
            img = pygame.transform.scale(img, (int(img.get_width() * scale), int(img.get_width() * scale)))
            self.animation_list.append(img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move(self, moving_left ,moving_right):
        # reset movement variables
        dx = 0
        dy = 0


        # assign movement variables if moving left or right
        if moving_left:
            dx = -self.speed
            self.direction = -1
            self.flip = True
        if moving_right:
            dx = self.speed
            self.direction = 1
            self.flip = False

        # update rectangle position
        self.rect.x += dx
        self.rect.y += dy

    def update_animation(self):
        ANIMATION_COOLDOWN = 100
        self.image = self.animation_list[self.frame_index]
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
            self.update_time = pygame.time.get_ticks()
            self.frame_index += 1
        if self.frame_index >= len(self.animation_list):
            self.frame_index = 0

        

    def draw(self):
        screen.blit(pygame.transform.flip(self.image, self.flip, False), self.rect)

    
player = Soldier("soldier", 200, 200, 1, 5)





run = True
while run:

    clock.tick(FPS)

    draw_bg()
    player.update_animation()
    player.draw()
    player.move(moving_left, moving_right)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
        # Stop the game
            run = False
        # Keyboard input
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False


        # Keyboard button release
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
                                



    pygame.display.update()


pygame.quit()
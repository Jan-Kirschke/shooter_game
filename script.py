import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = int(SCREEN_WIDTH * 0.8)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) 
pygame.display.set_caption('Jans Shooter Game')


x = 200
y = 200
soldier_sheet = pygame.image.load("img\Free Assets Soldier Version Four\Black_Soldier.png")

img = soldier_sheet.subsurface(pygame.Rect(30,30,32,32))
img = pygame.transform.scale(img, (img.get_width(), img.get_width()))

rect = img.get_rect()
rect.center = (x, y)


run = True
while run:


    screen.blit(img, rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()


pygame.quit()
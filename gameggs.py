import pygame

pygame.init()

background = pygame.display.set_mode((480, 360))
pygame.display.set_caption('amuguna')

img_bg = pygame.image.load('img/Blue Sky.svg')
img_apple = pygame.image.load('img/Apple.svg')

size_bg_width = background.get_size()[0]
size_bg_heigth = background.get_size()[1]
 
img_apple_width = img_apple.get_rect().size[0]
img_apple_heigth = img_apple.get_rect().size[1]


xpm = 0
ypm = 0

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT :
            play = False
        if event.type == pygame.MOUSEMOTION:
            xpm, ypm = pygame.mouse.get_pos()
            xpa = xpm - img_apple_width/2
            ypa = ypa - img_apple_heigth/2

background.blit(img_bg, (0, 0))
background.blit(img_apple, (xpa, ypa))
pygame.quit()


import pygame
pygame.init()

bg=pygame.display.set_mode((480, 360))
pygame.display.set_caption("사과 튕기기")

ib = pygame.image.load("img\Blue Sky.svg")
ia = pygame.image.load("img\Apple.svg")

sbw = bg.get_size()[0]
sbh = bg.get_size()[1]

saw = ia.get_rect().size[0]
sah = ia.get_rect().size[1]

xpa = sbw/2 - saw/2
ypa = 0

xsa = 1
ysa = 1

play = True

while play:
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            play = False
        if xpa==sbw or xpa==0 or ypa==sbh or ypa==0:
            print('박치기')
            xpa+=xsa
            ypa+=ysa
        bg.blit(ib, (0, 0))
        bg.blit(ia, (xpa, ypa))
        pygame.display.update()

pygame.quit()

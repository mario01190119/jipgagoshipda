import pygame 

pygame. init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My first Pygmae")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            runnning = False

 
        if event.type == pygame.KEYDOWN :
            if event.key == pygame.K_DOWN:
                print('down')
            if event.key == pygame.K_UP :
                print('up')
            if event.key == pygame.K_RIGHT :
                print('right')
            if event.key == pygame.K_LEFT :
                print('left')
            if event.key == pygame.MOUSEBUTTONDOWN :
                print('click')
            if event.key == pygame.K_SPACE:
                print('universe')
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.key == pygame.BUTTON_LEFT :
                print('left click')
            if event.key == pygame.BUTTON_RIGHT :
                print('right click')
            if event.key == pygame.BUTTON_MIDDLE :
                print('middle click')

    screen.fill((255, 255, 255))
    pygame.display.flip()

pygame.quit()
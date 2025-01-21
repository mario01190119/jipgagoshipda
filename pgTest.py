import pygame
pygame.init()

bg = pygame.display.set_mode((480, 360))
pygame.display.set_caption("draw")

play = True
while play :
    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.type == pygame.MOUSEMOTION :
                if event.button == 1:
                    xp, yp = pygame.mouse.get_pos()
                    pygame.draw.circle(bg, (255, 0, 0), (xp, yp), 8)
        if event.type == pygame.MOUSEBUTTONDOWN :
            if event.button == 3 :
                bg.fill((0, 0, 0))
            pass
            # if event.button == 1:
            #     print('left')
            # elif event.button == 2:
            #     print('right')
            # elif event.button == 3:
            #     print('sc-click')
            # elif event.button == 4:
            #     print('sc-up')
            # elif event.button == 5:
            #     print('sc-d')
        if event.type == pygame.MOUSEBUTTONUP :
            print("mu")
    pygame.display.update()
pygame.quit()

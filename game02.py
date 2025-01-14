import pygame
pygame.init()

bg = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Move with keyboard")

xp = bg.get_size()[0] // 2
yp = bg.get_size()[1] // 2

tx = 0
ty = 0
play = True

while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                ty = -1
            elif event.key == pygame.K_s:
                ty = 1
            elif event.key == pygame.K_a:
                tx = -1
            elif event.key == pygame.K_d:
                tx = 1
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w:
                ty = 0
            elif event.key == pygame.K_s:
                ty = 0
            elif event.key == pygame.K_a:
                tx = 0
            elif event.key == pygame.K_d:
                tx = 0

    xp += tx
    yp += ty

    bg.fill((255, 255, 255))
    pygame.draw.circle(bg, (0, 0, 0), (xp, yp), 5)
    pygame.display.update()

pygame.quit()

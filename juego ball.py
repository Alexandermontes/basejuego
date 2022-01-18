import sys, pygame

pygame.init()

size=800, 600

screen = pygame.display.set_mode(size)

pygame.display.set_caption("JUEGO BALL")

width, height =800,600

speed = [1, 1]

white = 255, 255, 255

ball = pygame.image.load("E://SET_DATOS//basejuego//ball.png")

ballrect = ball.get_rect()

bate = pygame.image.load("E://SET_DATOS//basejuego//bate.png")
baterect = bate.get_rect()

baterect.move_ip(400, 260)

run = True
while run:
    pygame.time.delay(2)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    ballrect=ballrect.move(speed)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_UP]:
        baterect=baterect.move(0,-1)
    if keys[pygame.K_DOWN]:
        baterect=baterect.move(0,1)

    if baterect.colliderect(ballrect):
        speed[0] = -speed[0]

    if ballrect.left < 0 or ballrect.right>width:
        speed[0] = -speed[0]
    if ballrect.top< 0 or ballrect.bottom >height:
        speed[1] = -speed[1]
    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(bate, baterect)
    pygame.display.flip()


pygame.quit()






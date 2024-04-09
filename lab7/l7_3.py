import pygame

pygame.init()
width, height = 700, 700
screen=pygame.display.set_mode((width, height))
clock=pygame.time.Clock()
x, y = 350, 350

running=True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x>=0+25:
            x-=20
    if keys[pygame.K_RIGHT] and x<=width-25:
        x+=20
    if keys[pygame.K_DOWN] and y<=height-25:
        y+=20
    if keys[pygame.K_UP] and y>=0+25:
        y-=20
    if x<25:
        x=25    
    if x>width-25:
        x=width-25
    if y>height-25:
        y=height-25
    if y<25:
        y=25
    
    screen.fill('Black')
    pygame.draw.circle(screen, 'Red', (x, y), 25)
    clock.tick(60)
    
    pygame.display.flip()

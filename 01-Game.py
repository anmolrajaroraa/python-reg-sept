import pygame
pygame.init()

x = y = 0
#red green blue (0-255)
black = 0,0,0
white = 255,255,255
red = 255,0,0
random_color = 100,200,150
screen = pygame.display.set_mode((1000,500))

while True:
    for event in pygame.event.get():
        '''if event.type == pygame.QUIT:
            pygame.quit()
            quit()'''
        pass
    #screen, color, (x,y,width,height)
    screen.fill( white )
    pygame.draw.rect(screen, red, (x,y,50,50))
    x += 1
    y += 1
    pygame.display.update()
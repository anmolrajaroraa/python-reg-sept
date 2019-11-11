import pygame,random
pygame.init()

x = 0
y = 25
#red green blue (0-255)
black = 0,0,0
white = 255,255,255
red = 255,0,0
random_color = 100,200,150
width = 600
height = 300
x2 = random.randint(0,width - 50)
y2 = random.randint(0,height - 50)
moveX = 0
moveY = 0
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()
fps = 100
frog = pygame.image.load('assets/frog.png')
sound = pygame.mixer.Sound('assets/point.wav')
counter = 0
snakeWidth = 50
snakeList = []
snakeLength = 1

def displayScore():
    msg = f"Score : {counter}"
    font = pygame.font.SysFont(None, 25, True, True)
    score = font.render(msg, True, red, None)
    screen.blit(score, (0,0))

def drawSnake():
    for bodyPart in snakeList:
        pygame.draw.rect(screen, red, (bodyPart[0], bodyPart[1], 50,50))

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                moveY = 1
                moveX = 0
            elif event.key == pygame.K_UP:
                moveY = -1
                moveX = 0
            elif event.key == pygame.K_LEFT:
                moveX = -1
                moveY = 0
            elif event.key == pygame.K_RIGHT:
                moveX = 1
                moveY = 0

    screen.fill( white )
    #screen, color, Rect object (x,y,w,h)
    # rect1 = pygame.draw.rect(screen, black, (x,y,50,50))
    rect1 = pygame.Rect((x,y,50,50))
    #rect2 = pygame.draw.rect(screen, random_color, (x2,y2,50,50))
    rect2 = pygame.Rect((x2,y2,50,50))
    # screen, color, (x,y), r
    # pygame.draw.circle(screen, red, (x,y), 50)
    x += moveX
    y += moveY
    screen.blit(frog, (x2,y2))
    displayScore()

    snakeHead = [x,y]
    snakeList.append(snakeHead)
    if len(snakeList) > snakeLength:
        del snakeList[0]
    # print(snakeList)
    drawSnake()

    if rect1.colliderect(rect2):
        x2 = random.randint(0,width-50)
        y2 = random.randint(0,height-50)
        sound.play()
        counter += 1
        # snakeWidth += 50
        snakeLength += 10

    if x > width:
        x = -50
    elif y > height:
        y = -50
    elif x < -50:
        x = width
    elif y < -50:
        y = height

    '''if y > height - 50:
        moveY = -10
    elif y < 50:
        moveY = 10
    elif x > width - 50:
        moveX = -10
    elif x < 50:
        moveX = 10'''

    fps += 1
    pygame.display.update()
    clock.tick(fps)
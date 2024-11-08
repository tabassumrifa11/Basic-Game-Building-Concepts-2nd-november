import pygame

pygame.init()

screen_width, screen_height = 500, 500

screen = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption('color changing sprite')


font = pygame.font.SysFont("Avalon", 36)
text = font.render("My First Game Screen!", True, (44, 98, 22))

colors = {

    'red': pygame.Color('red'),
    'green': pygame.Color('green'),
    'blue': pygame.Color('blue'),
    'yellow': pygame.Color('yellow'),
    'white': pygame.Color('white')

}

current_color = colors['white']

x, y = 30, 30

sprite_width, sprite_height = 60, 60

clock = pygame.time.Clock()

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
            
    pressed = pygame.key.get_pressed()

    if pressed[pygame.K_LEFT]: x = x - 3

    if pressed[pygame.K_RIGHT]: x = x + 3

    if pressed[pygame.K_UP]: y = y - 3

    if pressed[pygame.K_DOWN]: y = y + 3

    x = min(max(0, x), screen_width - sprite_width)

    y = min(max(0, y), screen_height - sprite_height)


    if x == 0: current_color = colors['blue']

    elif x == screen_width - sprite_width: current_color = colors['yellow']
    
    elif y == 0: current_color = colors['red']

    elif y == screen_height - sprite_height: current_color = colors['green']
    
    else: current_color = colors['white']
    
    
    screen.fill((0, 0, 0))
    
    pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
    
    
    screen.blit(text, (85, 150))
    
    pygame.display.flip()
    clock.tick(90)
    
    
pygame.quit()
import pygame

pygame.init()

window = pygame.display.set_mode((400,400))

window.fill((225, 255, 255))

BLUE = (0, 0, 246)

pygame.draw.circle(window, BLUE, (300,300), 50)

pygame.draw.circle(window, BLUE, (100,100), 50, 3)

pygame.display.update()

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            break
        
        
pygame.quit()
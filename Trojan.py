# Import Section
import pygame
import platform

# pygame init and create font for text
pygame.init()
screen = pygame.display.set_mode((500, 300))
textfont = pygame.font.SysFont("", 50)

os_info = platform.uname()

# color of the Screen
RED = (255, 0, 0)
running = True

# Loop for runing the system
while running:
    screen.fill(RED)
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            print(os_info)
            running = False
    textTBD = textfont.render("I Love you baybe :)", 1, (255, 255, 255))
    screen.blit(textTBD, (100, 100))

    pygame.display.update()

pygame.quit()

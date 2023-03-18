# Import Section
import pygame
import platform
import socket

import requests

# pygame init and create font for text
pygame.init()
screen = pygame.display.set_mode((500, 300))
textfont = pygame.font.SysFont("", 50)

# geting Oprating system
os_info = platform.uname()

# grting the local_Ip 
hostname = socket.gethostname()
ip_local = socket.gethostbyname(hostname)
# color of the Screen
RED = (255, 0, 0)
running = True


# geting public Ip 
ret = True
printed = False

public_ip = requests.get('http://api.ipify.org/').text

# Loop for runing the system
while running:
    screen.fill(RED)
    for event in pygame.event.get():

        if ret == True and not printed:
            print('public Ip :' + public_ip) 
            printed = True

        if(event.type == pygame.QUIT):
            print(os_info)
            print()
            running = False
    textTBD = textfont.render("I Love you baybe :)", 1, (255, 255, 255))
    screen.blit(textTBD, (100, 100))

    pygame.display.update()

pygame.quit()

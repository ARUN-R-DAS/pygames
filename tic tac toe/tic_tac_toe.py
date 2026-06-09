import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))

#______________________cooldown___________________________________
class Cooldown:
    def __init__(self, duration):
        self.duration = duration
        self.last_use = 0

    def ready(self):
        now = pygame.time.get_ticks()
        if now - self.last_use >= self.duration:
            self.last_use = now
            return True
        return False

cooldown1 = Cooldown(500)
#___________________update_frame_________________________
def update_frame():
    screen.fill((0,0,0))
    for i in range(3):
        for j in range(3):
            color = (255,255,255)
            border = 2
            pygame.draw.rect(screen, color, (100 + i*100, 100 + j*100, 100, 100), border)
    pygame.display.flip()
#____________________________________________
def get_mouse_pos():
    # only if left clicked
    if event.type == pygame.MOUSEBUTTONDOWN:
        if event.button == 1: # 1 =  left, 2 = right
            # cooldown
            if cooldown1.ready():
                x, y = pygame.mouse.get_pos()
                i = (x - 100) // 100
                j = (y - 100) // 100
                print(i, j)
    
#_________________main_____________________________
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    update_frame()
    get_mouse_pos()
#_____________________________________________
pygame.quit()
sys.exit()

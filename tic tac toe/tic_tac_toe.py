import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800,600))

#______________________initialization_____________________________
selection = (0,0)
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

cooldown1 = Cooldown(250)
#___________________update_frame_________________________
def update_frame(selection):
    screen.fill((0,0,0))
    for i in range(3):
        for j in range(3):
            color = (0,255,0) if selection == (i,j) else (255,255,255)
            border = 0 if selection == (i,j) else 2
            pygame.draw.rect(screen, color, (100 + i*100, 100 + j*100, 100, 100), border)
    pygame.display.flip()
#____________________________________________
def get_mouse_pos(events):
    # only if left clicked
    for event in events:
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1: # 1 =  left, 2 = right
                # cooldown
                if cooldown1.ready():
                    x, y = pygame.mouse.get_pos()
                    i = (x - 100) // 100
                    j = (y - 100) // 100
                    print(i, j)
                    return (i,j)
    
#_________________main_____________________________
def main():
    running = True
    while running:
        events = pygame.event.get() # else the events get lost
        for event in events:
            if event.type == pygame.QUIT:
                running = False
                break
        
        selection = get_mouse_pos(events)
        if selection:
            print(selection)
            update_frame(selection)

    pygame.quit()
    sys.exit()
#_________________Entry point____________________________
if __name__ == "__main__":
    main()


#pygame is a bunch of pre-written python code that makes coding games easier
import pygame #handles graphics, sound, game timings, keyboard input, etc
pygame.init()

#creates game screen and caption
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Silly Shapes")

class butterfly:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
    def draw(self):
        pygame.draw.circle(screen, (0,0,255), (self.xpos, self.ypos), 80)
        pygame.draw.circle(screen, (0,0,255), (self.xpos, self.ypos+110), 100)
        pygame.draw.circle(screen, (0,0,255), (self.xpos+180, self.ypos), 80)
        pygame.draw.circle(screen, (0,0,255), (self.xpos+180, self.ypos+110), 100)
        pygame.draw.ellipse(screen, (255, 255, 0), (self.xpos+50, self.ypos-50, 80, 300))
        pygame.draw.arc(screen,(255,0,0), (self.xpos+60, self.ypos+70, 60, 40), 7*3.14/6,11*3.14/6 , 5)
        pygame.draw.arc(screen,(255,0,0), (self.xpos+60, self.ypos+110, 60, 40), 7*3.14/6,11*3.14/6 , 5)
        pygame.draw.arc(screen,(255,0,0), (self.xpos+60, self.ypos+150, 60, 40), 7*3.14/6,11*3.14/6 , 5)
        pygame.draw.arc(screen,(255,0,0), (self.xpos+60, self.ypos+40, 60, 40), 7*3.14/6,11*3.14/6 , 5)
        pygame.draw.arc(screen,(255,0,0), (self.xpos+60, self.ypos, 60, 40), 7*3.14/6,11*3.14/6 , 5)
        pygame.draw.line(screen,(255,0,0), (self.xpos+80, self.ypos-40),(self.xpos+70, self.ypos-80), 5)
        pygame.draw.line(screen,(255,0,0), (self.xpos+100, self.ypos-40),(self.xpos+110, self.ypos-80), 5)
  
butterfly1 = butterfly(300,200)
butterfly2 = butterfly(500,500)
butterfly3 = butterfly(700,800)

butterfly1.draw()
butterfly2.draw()
butterfly3.draw()

  

pygame.display.flip() #update graphics 

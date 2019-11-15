#https://github.com/sahrudaysherla/pacman-using-python
import pygame

class sprite:
  def __init__(self, x, y, ani):
    self.xpos=x
    self.ypos=y
    self.animations=ani
    self.isdead=False
  def move(self,direction):
    pass


animation="image/animations/"

pacman = sprite(100, 5,animation+"placeholder")
Blinky = sprite(100, 5,animation+"placeholder")
Pinky = sprite(100, 5,animation+"placeholder")
Inky = sprite(100, 5,animation+"placeholder")
Clyde = sprite(100, 5,animation+"placeholder")


#graphics things
pygame.init()

screen_size=200,100

window=pygame.display.set_mode((screen_size[0],screen_size[1]))

def graphics():
  window.fill((0,0,0))
  pygame.display.update()


#movement
key_list=[pygame.K_UP,"U",pygame.K_DOWN,"D",pygame.K_RIGHT,"R",pygame.K_LEFT,"L"]
def key_presses():
  pass

def Ai():
  pass


#main loop
def main_loop():
  while True:
    graphics()
    
    

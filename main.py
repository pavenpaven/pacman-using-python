#https://github.com/sahrudaysherla/pacman-using-python
import pygame

pygame.init()


class sprite:
  def __init__(self, x, y, animation_path, animation_frames):
    self.xpos = x
    self.ypos = y
    self.animations = animations_path
    self.isdead = False
    self.direction = 
  def change_direction(self, direction):
    pass

#Make a folder for images with a folder for animations in it.
animation_path="image/animations/"

#creating all the sprites
#replace "placeholder" with a real folder for the sprites animations. I think pygame does not support gif animations.
pacman = sprite(100, 5, animation+"placeholder")
Blinky = sprite(100, 5, animation+"placeholder")
Pinky = sprite(100, 5, animation+"placeholder")
Inky = sprite(100, 5, animation+"placeholder")
Clyde = sprite(100, 5, animation+"placeholder")


#graphics things

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
    
main_loop()

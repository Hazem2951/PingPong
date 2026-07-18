from pygame import *
'''Required classes'''




#game scene:
back = (200, 255, 255) #background color (background)
win_width = 600
win_height = 500
window = display.set_mode((win_width, win_height))
window.fill(back)


#flags responsible for game state
game = True
finish = False
clock = time.Clock()
FPS = 60

while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   if finish != True:
       window.fill(back)

display.update()
clock.tick(FPS)

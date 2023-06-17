from pygame import *
back = (238, 45, 205)

win_width = 500
win_height = 500

window = display.set_mode((win_height,win_height))
window.fill(back)

a = 1000

clock = time.Clock()
FPS = 60
game = True

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    
    display.update()
    clock.tick(FPS)

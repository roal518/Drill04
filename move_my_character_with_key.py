from pico2d import *

TUK_WIDTH,TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.PNG')
IDLE_character = load_image('Woodcutter_idle.png')
IDLE_character.draw(1000,200)
tuk_ground.draw(0,0)
update_canvas()
delay(10)
close_canvas()
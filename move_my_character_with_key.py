from pico2d import *

TUK_WIDTH,TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.PNG')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
IDLE_character.clip_draw(0,0,100,102,000,0)
MOVE_character.clip_draw(0,0,100,102,100,200)
#tuk_ground.draw(640,512)
update_canvas()
delay(10)
close_canvas()
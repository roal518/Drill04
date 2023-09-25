from pico2d import *

TUK_WIDTH,TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.PNG')
IDLE_character = load_image('Woodcutter_idle.png')
MOVING_character=load_image('Woodcutter_run.png')

def handle_events():
    global running
    global x, y, delay
running = True
moving = True
frame = 0
x, y = TUK_WIDTH // 2 ,  TUK_HEIGHT // 2
hide_cursor()
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    if moving:
        MOVING_character.clip_draw(frame*100)
    elif not moving:
        IDLE_character.clip_draw(frame*100)
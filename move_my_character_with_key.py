from pico2d import *

TUK_WIDTH,TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH,TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.PNG')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
IDLE_character.clip_draw(0,0,100,102,50,190)
# x,y 좌표에서 캐릭터가 제대로 보이는 최솟값
MOVE_character.clip_draw(0,0,100,102,1280,940)
# x,y 좌표에서 캐릭터가 제대로 보이는 최댓값

def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        if event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

running = True
frame = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    update_canvas()
    handle_events()
    frame = (frame+1) % 8
    delay(0.05)

close_canvas()
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
    global running, xdir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_LEFT:
            xdir -=1
        elif event.type == SDL_KEYDOWN and event.key == SDLK_RIGHT:
            xdir +=1


x=800//2
running = True
xdir = 0
ydir = 0
runframe = 0
idleframe = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2,TUK_HEIGHT//2)
    MOVE_character.clip_draw(runframe*100, 0, 100, 102,x, 200)
    update_canvas()
    handle_events()
    x += xdir*5
    runframe = (runframe+1) % 6
    delay(0.05)

close_canvas()
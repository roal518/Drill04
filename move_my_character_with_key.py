from pico2d import *

TUK_WIDTH, TUK_HEIGHT = 1280, 1024
open_canvas(TUK_WIDTH, TUK_HEIGHT)
tuk_ground = load_image('TUK_GROUND.PNG')
IDLE_character = load_image('Woodcutter_idle.png')
MOVE_character = load_image('Woodcutter_run.png')
# IDLE_character.clip_draw(0, 0, 100, 102, 50, 190)
# x,y 좌표에서 캐릭터가 제대로 보이는 최솟값
# MOVE_character.clip_draw(0, 0, 100, 102, 1280, 940)
# x,y 좌표에서 캐릭터가 제대로 보이는 최댓값


def arrived_end():
    global running
    global x, y
    if 50 > x or x > 1280:
        running = False
    if 190 > y or y > 940:
        running = False
def handle_events():
    global running, moving
    global xdir, ydir
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
            elif event.key == SDLK_LEFT:
                xdir -=1
                moving = True
            elif event.key == SDLK_RIGHT:
                xdir +=1
                moving = True
            elif event.key == SDLK_UP:
                ydir += 1
                moving = True
            elif event.key == SDLK_DOWN:
                ydir -= 1
                moving = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                xdir +=1
                moving = False
            elif event.key == SDLK_RIGHT:
                xdir -=1
                moving = False
            elif event.key == SDLK_UP:
                ydir -= 1
                moving = False
            elif event.key == SDLK_DOWN:
                ydir += 1
                moving = False
x = TUK_WIDTH//2
y = TUK_HEIGHT//2
running = True
moving = False
xdir = 0
ydir = 0
runframe = 0
idleframe = 0
while running:
    clear_canvas()
    tuk_ground.draw(TUK_WIDTH//2, TUK_HEIGHT//2)
    if moving:
        if xdir >= 0:
            MOVE_character.clip_draw(runframe*100, 0, 100, 102, x, y)
        elif xdir < 0:
            MOVE_character.clip_composite_draw(runframe * 100, 0, 100, 100, 0, 'h', x, y,100,100)
    else:
        IDLE_character.clip_draw(idleframe*100, 0, 100, 100, x, y)
    update_canvas()
    handle_events()
    arrived_end()
    x += xdir*5
    y += ydir*5

    idleframe = (runframe+1) % 4
    runframe = (runframe+1) % 6
    delay(0.03)

close_canvas()
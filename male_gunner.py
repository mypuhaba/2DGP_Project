from pico2d import *
open_canvas()
gunner = load_image('male_gunner_sprite\\jump_left.png')
x = 70
n = 0
frame = 0
while (x < 800):
    clear_canvas() # width, height = 205, 173
    gunner.clip_draw(frame * 205, 0, 205, 173, x, 80)
    update_canvas()
    frame = (frame + 1) % 4
    x += 10
    delay(0.1)
    get_events()

close_canvas()

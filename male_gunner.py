from pico2d import *
open_canvas()
gunner = load_image('gunner_sprite\\test.png')
x = 70
n = 0
frame = 0
while (x < 800):
    clear_canvas() # width, height = 205, 173
    gunner.clip_draw(frame * 205, 0, 205, 173, x, 0)
    update_canvas()
    frame = (frame + 1) % 4
    x += 30
    delay(0.1)
    get_events()

close_canvas()

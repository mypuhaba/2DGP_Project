from pico2d import *

# class Grass:
#     def __init__(self):
#         self.image = load_image('grass.png')
#
#     def draw(self):
#         self.image.draw(400, 30)

class Gunner:
    def __init__(self):
        self.x, self.y = 0, 90
        self.frame = 0
        self.image = load_image('male_gunner_sprite/run.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 1

    def draw(self):
        self.image.clip_draw(self.frame * 205, 0, 205, 173, x, 80)


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False

open_canvas()


boy = Boy()
grass = Grass()
running = True

# game main loop code
while running:
    handle_events()

    boy.update()

    clear_canvas()
    grass.draw()
    boy.draw()
    update_canvas()

    delay(0.05)

# finalization code
close_canvas()

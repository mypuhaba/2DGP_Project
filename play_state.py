from pico2d import *
import game_framework
import play_state


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Gunner:
    def __init__(self):
        self.x, self.y = 0, 125
        self.frame = 0
        self.dir = 1
        self.imageR = load_image('male_gunner_sprite/run.png')
        self.imageL = load_image('male_gunner_sprite/run_left.png')


    def update(self):

        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 10
        if self.x > 800:
            self.dir = -1
            self.x = 800
        elif self.x < 0:
            self.dir = 1
            self.x = 0
        delay(0.1)


    def draw(self):
        if self.dir == 1:
            self.imageR.clip_draw(self.frame * 205, 0, 205, 173, self.x, self.y)
        else:
            self.imageL.clip_draw(self.frame * 205, 0, 205, 173, self.x, self.y)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == pico2d.SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()

gunner = None
grass = None

def enter():
    global gunner, grass
    gunner = Gunner()
    grass = Grass()


def exit():
    global gunner, grass
    del gunner
    del grass


def update():
    global gunner
    gunner.update()



# 월드를 그린다.
def draw_world():
    grass.draw()
    gunner.draw()

def draw():
    clear_canvas()
    draw_world()
    update_canvas()

def pause():
    pass

def resume():
    pass



def test_self():
    import sys
    this_module = sys.modules['__main__']
    pico2d.open_canvas()
    game_framework.run(this_module)
    pico2d.close_canvas()

if __name__ == '__main__': #만약 단독 실행 상태이면,
    test_self()
import pico2d
from pico2d import *
import game_framework
import play_state


class Forest:
    def __init__(self):
        self.x, self.y = 0, 0
        self.frame = 0
        self.dir = 0
        self.image = load_image('background_image/forest.png')

    def draw(self):
        self.image.draw(400, 300)


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(400, 30)


class Gunner:
    def __init__(self):
        self.x, self.y = 0, 125
        self.frame = 0
        self.dir, self.face_dir = 0, 1
        self.shot = 0
        self.normalR = load_image('gunner_sprite/normal.png')
        self.normalL = load_image('gunner_sprite/normal_left.png')
        self.runR = load_image('gunner_sprite/run.png')
        self.runL = load_image('gunner_sprite/run_left.png')
        # self.jumpR = load_image('gunner_sprite/jump.png')
        # self.jumpL = load_image('gunner_sprite/jump_left.png')
        self.shotR = load_image('gunner_sprite/shot.png')
        self.shotL = load_image('gunner_sprite/shot_left.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += self.dir * 10
        self.x = clamp(40, self.x, 800)
        delay(0.05)

    def draw(self):
        if self.dir == 1:
            self.runR.clip_draw(self.frame * 205, 0, 205, 173, self.x, self.y)
        elif self.dir == -1:
            self.runL.clip_draw(self.frame * 205, 0, 205, 173, self.x, self.y)
        else:
            if self.face_dir == 1:
                if self.shot == 1:
                    self.shotR.clip_draw((self.frame * 7 // 8) * 205, 0, 205, 173, self.x, self.y)
                else:
                    self.normalR.clip_draw(self.frame // 2 * 205, 0, 205, 173, self.x, self.y)
            else:
                if self.shot == 1:
                    self.shotL.clip_draw((self.frame * 7 // 8) * 205, 0, 205, 173, self.x, self.y)
                else:
                    self.normalL.clip_draw(self.frame // 2 * 205, 0, 205, 173, self.x, self.y)



def handle_events():
    events = get_events()
    for event in events:
        if event.type == pico2d.SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            match event.key:
                case pico2d.SDLK_ESCAPE:
                    game_framework.quit()
                case pico2d.SDLK_LEFT:
                    gunner.dir -= 1
                case pico2d.SDLK_RIGHT:
                    gunner.dir += 1
                case pico2d.SDLK_x:
                    gunner.shot = 1

        elif event.type == SDL_KEYUP:
            match event.key:
                case pico2d.SDLK_LEFT:
                    gunner.dir += 1
                    gunner.face_dir = -1
                case pico2d.SDLK_RIGHT:
                    gunner.dir -= 1
                    gunner.face_dir = 1
                case pico2d.SDLK_x:
                    gunner.shot = 0


forest = None
grass = None
gunner = None


def enter():
    global grass, forest, gunner
    forest = Forest()
    grass = Grass()
    gunner = Gunner()


def exit():
    global grass, forest, gunner
    del gunner
    del forest
    del grass


def update():
    global forest, gunner
    # forest.update()
    gunner.update()


# 월드를 그린다.
def draw_world():
    forest.draw()
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


if __name__ == '__main__':  # 만약 단독 실행 상태이면,
    test_self()

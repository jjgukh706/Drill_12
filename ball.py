import os

from pico2d import get_canvas_width, load_image

import game_world

# 이미지 경로를 스크립트 위치 기준으로 만들어 실행 위치(cwd)와 무관하게 로드한다.
_HERE = os.path.dirname(os.path.abspath(__file__))

BALL_SIZE = 23      # ball21x21.png 의 실제 크기
BALL_SPEED = 12     # 프레임당 이동 거리(px)


class Ball:
    image = None
    def __init__(self, x, y, dir):
        self.x, self.y = x, y
        self.dir = dir
        if Ball.image is None:
            Ball.image = load_image(os.path.join(_HERE, 'ball21x21.png'))

    def update(self):
        self.x += self.dir * BALL_SPEED

        # 화면 밖으로 완전히 벗어나면 월드에서 제거한다.
        if self.x < -BALL_SIZE or self.x > get_canvas_width() + BALL_SIZE:
            game_world.remove_object(self)

    def draw(self):
        self.image.draw(self.x, self.y)

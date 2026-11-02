import os

from pico2d import load_image

# 이미지 경로를 스크립트 위치 기준으로 만들어 실행 위치(cwd)와 무관하게 로드한다.
_HERE = os.path.dirname(os.path.abspath(__file__))


class Grass:
    def __init__(self,y):
        self.image = load_image(os.path.join(_HERE, 'grass.png'))
        self.y = y
    def draw(self):
        self.image.draw(400, self.y)

    def update(self):
        pass

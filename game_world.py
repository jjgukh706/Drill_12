# world = []  1차원 리스트

world = [ [], [] ,[]]


# 게임월드에 객체를 추가 할 때에는 layer를 지정
def add_object(o, depth = 0):
    world[depth].append(o)

def remove_object(o, depth = 0):
    for layer in world:
        if o in layer:
            layer.remove(o)
            return
            

# game logic
def update():
    for layer in world:
        for o in layer:
            o.update()

def render():
    for layer in world:
        for o in layer:
            o.draw()

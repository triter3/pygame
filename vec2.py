class Vec2():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def print_vec(self):
        print(str(self.x) + "," + str(self.y))


def print_vec(x,y):
    print(str(x) + "," + str(y))

def zoom_rect(rect, ref):
    rect.x = int(rect.x*ref)
    rect.y = int(rect.y*ref)
    rect.width = int(rect.width*ref)
    rect.height = int(rect.height*ref)

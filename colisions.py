import player
import game_map
import pygame as pg
import vec2 as v

def colision_map(entity,map):
    offset = v.Vec2()
    offset.x = entity.rect.x - map.shift.x
    offset.y = entity.rect.y - map.shift.y
    x = int(offset.x/map.tile_dim)
    y = int(offset.y/map.tile_dim)
    length = v.Vec2()
    length.y = int((offset.y + entity.rect.height - 1)/map.tile_dim)+1
    length.x = int((offset.x + entity.rect.width - 1)/map.tile_dim)+1
    for j in range(y,length.y):
        for i in range(x,length.x):
            aux = v.Vec2(i,j)
            if(entity.get_offset().x < 0): aux.x = length.x + x - i - 1
            if(entity.get_offset().y < 0): aux.y = length.y + y - j - 1
            if map.buffer_map[aux.y][aux.x] != "0":
                r_blk = pg.Rect(0,0, map.tile_dim, map.tile_dim)
                r_blk.x = aux.x*map.tile_dim + map.shift.x
                r_blk.y = aux.y*map.tile_dim + map.shift.y
                pr = get_regression(entity.rect, entity.last_pos, r_blk)
                if pr != None:
                    entity.move(pr, False)
                    entity.colision(get_side(pr))
                    return True
    return False

#colisions entre dos rectangles
def in_colision(rect1, rect2):
    if(rect1.x < rect2.x + rect2.width and rect1.x + rect1.width > rect2.x
    and rect1.y < rect2.y + rect2.height and rect.y + rect1.height > rect2.y):
        return True
    else: return False

def get_regression(rect1, last_pos1, rect2, ref = None):
    x = rect1.x - last_pos1.x
    y = rect1.y - last_pos1.y
    v1 = v.Vec2(rect1.x, rect1.y)
    v2 = v.Vec2(rect2.x, rect2.y)

    if x > 0: v1.x += rect1.width
    else: v2.x += rect2.width
    if y > 0: v1.y += rect1.height
    else: v2.y += rect2.height
    #busca de posicio relativa i calcul del desplaçament
    #que cal aplicar
    if x==0 or (x > 0 and last_pos1.x > v2.x) or (x < 0 and last_pos1.x + rect1.width < v2.x):
        return v.Vec2(0, v2.y - v1.y)
    elif y==0 or (y > 0 and last_pos1.y > v2.y) or (y < 0 and last_pos1.y + rect1.height < v2.y):
        return v.Vec2(v2.x - v1.x, 0)
    else:
        last = v.Vec2(last_pos1.x, last_pos1.y)
        if x < 0: last.x += rect1.width
        if y < 0: last.y += rect1.height
        #areglar cas de divisio per 0
        aux = []
        if (v1.x - last.x) == 0 or (v2.x - last.x) == 0:
            aux.append(round(abs((v2.x - last.x)/(v2.y - last.y)),5))
            aux.append(round(abs((v1.x - last.x)/(v1.y - last.y)),5))
        else:
            aux.append(round(abs((v1.y - last.y)/(v1.x - last.x)),5))
            aux.append(round(abs((v2.y - last.y)/(v2.x - last.x)),5))

        if aux[0] < aux[1]:
            return v.Vec2(0, v2.y - v1.y)
        elif aux[0] > aux[1]:
            return v.Vec2(v2.x - v1.x, 0)
        else:
            if ref == None:
                print("eyyy")
                return(v.Vec2(v2.x - v1.x, v2.y - v1.y))

def get_side(regression):
    if regression.x == 0:
        if regression.y < 0: return "down"
        else: return "up"
    elif regression.y == 0:
        if regression.x < 0: return "right"
    else: return "left"
    return "none"



def abs(x):
    if x >= 0: return x
    return -x

def sgn(x):
    if x > 0: return 1
    elif x == 0: return 0
    return -1

def add_one(x):
    if x < 0: return x - 1
    else:
        return x + 1

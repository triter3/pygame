import player

def colision_map(player, map):
    if(in_colision(player.rect.x, player.rect.y, player.rect.width, player.rect.height))

def in_colision(x_1, y_1, width_1, height_1, x_2, y_2, width_2, height_2):
    if(x_1 < x_2 + width_2 and x_1 + width_1 > x_2
    and y_1 < y_2 + height_2 and y_1 + height_1 > y_2):
        return True;
    else return False;

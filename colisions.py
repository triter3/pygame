import player

def colision_map(player, map):
    offset_x = player.rect.x - map.map_shift_x - map.offset_x
    offset_y = player.rect.y - map.map_shift_y - map.offset_y
    x = int(offset_x/map.tile.get_size())
    y = int(offset_y/map.tile.get_size())
    print(str(y) + "," + str(int((offset_y + player.rect.height)/map.tile.get_size())))
    for j in range(y,int((offset_y + player.rect.height)/map.tile.get_size())+1):
        for i in range(x,int((offset_x + player.rect.width)/map.tile.get_size())+1):
            #print(str(i) + "," +  str(j))
            if map.buffer_map[j][i] == 1:
                return True
    return False

def in_colision(x_1, y_1, width_1, height_1, x_2, y_2, width_2, height_2):
    if(x_1 < x_2 + width_2 and x_1 + width_1 > x_2
    and y_1 < y_2 + height_2 and y_1 + height_1 > y_2):
        return True
    else: return False

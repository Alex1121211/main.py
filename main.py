def main():
    x, y = 300, 400
    width, height = 200, 300
    draw_house(x, y, width, height)
    draw_house_roof(x, y, roof_height=0, width=0)

def draw_house(x, y, width, heigth):
    """

    :param x:
    :param y:
    :param width:
    :param heigth:
    :return:
    """
    print(x, y, width, heigth)
    foundation_heigth = 0.05 * heigth
    walls_width = 0.9 * width
    walls_heigth = 0.5 * heigth
    roof_height = heigth- foundation_heigth - walls_heigth





def draw_house_foundation(x, y, foundation_heigth, width):
    print(x, y, width, foundation_heigth)



def draw_house_walls(x, y, walls_heigth, walls_width):
    print(x, y, walls_heigth, walls_width)




def draw_house_roof(x, y, roof_height, width):
    print(x, y, width, roof_height)
    





main()
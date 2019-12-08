import numpy as np

if __name__ == '__main__':

    with open('input.txt', 'r') as f:

        # input
        lines = f.readline()
        image_data = lines.strip()

        # const
        width  = 25
        height = 6

        # vars for images layers
        layers = []
        new_layer = []
        new_row = []
        height_count = 0
        width_count = 0


        for pixel in image_data:


            if width_count < width:
                new_row.append(pixel)
                width_count += 1
            else:
                # new row
                height_count += 1
                width_count = 1
                new_layer.append(new_row.copy())
                new_row = [pixel]

                if height_count >= height:

                    height_count = 0
                    # add new layer to layers list
                    layers.append(new_layer.copy())
                    new_layer = []

    pic = [[' ' for _ in range(25)] for _ in range(6) ]
    layers.reverse()
    for lay in layers:

        for i in range(len(lay)):
            for j in range(len(lay[0])):

                if lay[i][j] == '1':
                    pic[i][j] = '#'

                elif lay[i][j] == '0':
                    pic[i][j] = ' '
    for p in pic:
        for itm in p:
            print(itm, end='')
        print()

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
        zero_count = 0
        layer_index = 0
        height_count = 0
        width_count = 0

        # vars for zero count
        low_layer = []
        zero_count = 0
        min_count = 1e10

        for pixel in image_data:


            if width_count < width:
                if pixel == '0':
                    zero_count += 1
                new_row.append(pixel)
                width_count += 1
            else:
                # new row
                height_count += 1
                width_count = 1
                new_layer.append(new_row.copy())
                new_row = [pixel]

                if height_count >= height:

                    if zero_count < min_count:
                    # add new lowest zero layer
                        low_layer = new_layer.copy()
                        min_count = zero_count
                    zero_count = 0
                    height_count = 0
                    # add new layer to layers list
                    layers.append(new_layer.copy())
                    new_layer = []

        count1 = 0
        count2 = 0
        for row in low_layer:
            for pix in row:
                if pix == '1':
                    count1 += 1
                elif pix == '2':
                    count2 += 1

        print(count1*count2)

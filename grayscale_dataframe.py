from PIL import Image
import os

def image_to_c_array(path):
    img = Image.open(path).convert('L').resize((64, 64))
    data = list(img.getdata())
    with open('frame_array.h', 'w') as f:
        f.write('const uint8_t frame[64][64] = {\n')
        for i in range(64):
            f.write('  {' + ', '.join(str(data[i*64 + j]) for j in range(64)) + '},\n')
        f.write('};')

image_to_c_array('frame_001.jpg')
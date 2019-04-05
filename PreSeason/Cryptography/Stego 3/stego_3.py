import imageio
import numpy as np
from PIL import Image

def get_rgb(hex_color):
	h = hex_color.lstrip('#')
	return list(int(h[i:i+2], 16) for i in (0, 2, 4))

colors = {}
# Create a 445x300x3 array of 8 bit unsigned integers
data = np.zeros( (445,300,3), dtype=np.uint8 )

with open('Stego 3.txt') as f:
	for line in f:
		line_split = line.split(' ')
		color = line_split[3]
		x = int(line_split[0].split(',')[0])
		y = int(line_split[0].split(',')[-1].rstrip(':'))
		if color not in colors:
			colors[color] = get_rgb(color)
		data[x,y] = colors[color]
# flip image horizontally and rotate it 90° ccw
data = np.rot90(np.flip(data, axis=1))
Image.fromarray(data).show()
imageio.imwrite('Stego 3.png', data)
 

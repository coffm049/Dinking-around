import matplotlib.pyplot as plt
import numpy as np
image = plt.imread("image.png")

# extract pixel intensities
red,green,blue = image[:,:,0], image[:,:,1], image[:,:,2]

red_pix = red.flatten()
green_pix=green.flatten()
blue_pix = blue.flatten()

plt.subplot(3,3,2)
plt.axis('off')
plt.imshow(image)

# rescaling each color and inverting 
new_red = 1- (0.5 * ((red_pix - red_pix.min()) / (red_pix.max() - red_pix.min())))
new_green =1-(0.5 *((green_pix - green_pix.min()) / (green_pix.max() - green_pix.min())))
new_blue = 1-(0.5 * ((blue_pix - blue_pix.min()) / (blue_pix.max() - blue_pix.min())))

plt.subplot(3,3,4)

redim = new_red.reshape(image.shape[:2])
bluim = new_blue.reshape(image.shape[:2])
grim = new_green.reshape(image.shape[:2])
plt.imshow(redim, cmap = 'Reds')

plt.subplot(3,3,5)
plt.imshow(bluim, cmap= 'Blues')
plt.subplot(3,3,6)
plt.imshow(grim, cmap='Greens')

color_image = []
for pix in range(len(new_red)) :
    color_image.append([new_red[pix], new_green[pix], new_blue[pix]])
color_image = np.array(color_image)
new_image = color_image.reshape(image.shape)
plt.subplot(3,3,8)
plt.axis('off')
plt.imshow(new_image)

plt.show()

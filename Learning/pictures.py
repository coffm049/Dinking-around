import matplotlib.pyplot as plt
import numpy as np
image = plt.imread("image.png")

# extract pixel intensities
red,green,blue = image[:,:,0], image[:,:,1], image[:,:,2]

red_pix = red.flatten()
green_pix=green.flatten()
blue_pix = blue.flatten()

low_end = 0

plt.subplot(3,3,1)
plt.axis('off')
plt.imshow(image)

plt.subplot(3,3,4)
#plt.title("Histogram of Intensities")
#plt.hist(red_pix, color='r', bins = 64, alpha = 0.5)
#plt.hist(green_pix, color='g', bins = 64, alpha = 0.5)
#plt.hist(blue_pix, color = 'b', bins = 64, alpha = 0.5)
#plt.xlim((0.1,1))
#plt.ylim((0,10000))
#plt.hist2d(x= red_pix, y = green_pix, bins = (64,64))

# Histogram of red pixels intensities
plt.title("Red")
plt.hist(red_pix, color = 'r', range= (low_end ,1), normed = False, alpha = 0.5, bins = 64)
plt.twinx()
rcdf,rbins,rpatches = plt.hist(red_pix, color='y', range=(low_end,1), normed = True, cumulative = True, alpha = 0.5, bins= 64)

plt.subplot(3,3,5)
plt.title("Blue")
plt.hist(blue_pix, color = 'b', range= (low_end,1), normed = False, alpha = 0.5, bins = 64)
plt.twinx()
bcdf,bbins,bpatches = plt.hist(blue_pix, color='y', range=(low_end,1), normed = True, cumulative = True, alpha = 0.5, bins= 64)


plt.subplot(3,3,6)
plt.title("Green")
plt.hist(green_pix, color = 'g', range= (low_end,1), normed = False, alpha = 0.5, bins = 64)
plt.twinx()
gcdf,gbins,gpatches =plt.hist(green_pix, color='y', range=(low_end,1), normed = True, cumulative = True, alpha = 0.5, bins= 64)
 
new_red = 1 * (red_pix - red_pix.min()) / (red_pix.max() - red_pix.min())
new_green = 1* (green_pix - green_pix.min()) / (green_pix.max() - green_pix.min())
new_blue = 1* ( blue_pix - blue_pix.min()) / (blue_pix.max() - red_pix.min())

plt.subplot(3,3,7)

redim = new_red.reshape(image.shape[:2])
bluim = new_blue.reshape(image.shape[:2])
grim = new_green.reshape(image.shape[:2])
plt.imshow(redim, cmap = 'Reds')

plt.subplot(3,3,8)
plt.imshow(bluim, cmap= 'Blues')
plt.subplot(3,3,9)
plt.imshow(grim, cmap='Greens')

color_image = []
for pix in range(len(new_red)) :
    color_image.append([new_red[pix], new_blue[pix], new_green[pix]])
color_image = np.array(color_image)
new_image = color_image.reshape(image.shape)
# plt.imshow(new_image)

print(blue_pix[:10])
print(new_blue[:10])

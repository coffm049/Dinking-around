import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

image = plt.imread("image.png")

red_pix,green_pix,blue_pix = image[:,:,0], image[:,:,1], image[:,:,2]

red_pix = red_pix.flatten()
red_pix = red_pix.flatten()
red_pix = red_pix.flatten()

x= np.random.normal(0, 10, 30)
y= np.random.normal(7, 2, 30)

df = pd.DataFrame({'red' : [red_pix], 'green': [green_pix], 'blue' : [blue_pix]})

plt.subplot(2,2,1)
plt.hist2d(x= df['red'], y = df['green'], bins = (64,64))
plt.subplot(2,2,2)
plt.hist2d(x=df['red'], y= df['blue'], bins = (64,64))
plt.subplot(2,2,3)
plt.hist2d(x=df['green'], y = df['blue'], bins = (64,64))

#plt.hexbin(x=df['x'], y = df['y'], gridsize= (5,5))
#plt.colorbar()

# sns.jointplot(x='x', y='y', data= df)

plt.show()

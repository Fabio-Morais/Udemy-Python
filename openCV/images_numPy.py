import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


pic = Image.open("DATA/00-puppy.jpg")
#pic.show()
type(pic)
plt.clf()
pic_arr= np.asarray(pic)
print(pic_arr.shape)
x = plt.figure()
plt.imshow(pic_arr)
plt.show()


#0-> NO RED, 255->a pure red
pic_red = pic_arr.copy()
pic_red = pic_red[:, :, 0]# R G B
print(pic_red)
plt.imshow(pic_red)
plt.show()
plt.imshow(pic_red, cmap="gray")
plt.show()

pic_green = pic_arr.copy()
pic_green = pic_green[:, :, 1]# R G B
plt.imshow(pic_green)
plt.show()
plt.imshow(pic_green, cmap="gray")
plt.show()

pic_red = pic_arr.copy()
pic_red[:, :, 2] = 0
plt.imshow(pic_red, cmap="gray")
plt.show()





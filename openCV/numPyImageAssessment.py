import numpy as np
import matplotlib.pyplot as plt
from PIL import Image

mat = np.ones((5,5))*10
print(mat)

# This line sets a "seed" so you get the same random numbers we do
np.random.seed(101)
# This line creates an array of random numbers
arr = np.random.randint(low=0,high=100,size=(5,5))

print(arr.max())
print(arr.min())

pic = Image.open("DATA/00-puppy.jpg")
pic.show()

pic_arr = np.asarray(pic)
print(pic_arr.shape)

aux = pic_arr.copy()
aux[:, :, 0] = 0
aux[:, :, 1] = 0
plt.imshow(aux)
plt.show()
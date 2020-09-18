import numpy as np

matri_ones = np.ones((2,5))
matri_zeros = np.zeros((2,5))
print(matri_ones)
print("\n")
print(matri_zeros)
print("\n-----------------------------------------")

arr = np.random.randint(0,100,10)
print(arr)
print(f"max = {arr.max()}")
print(f"indice = {arr.argmax()}")
print(f"mean = {arr.mean()}")
arr_new = arr.reshape((5,2))
print(arr_new)
print("\n-----------------------------------------")
# np.arange() -> create vector
mat = np.arange(0,100).reshape(10,10)
print(mat)
print()
print(f"[2,1] = {mat[2,1]}")
print()
print(mat[:,1]) # :-> everything | 1-> column 1
print()
print(mat[0,:])
print("\nrow: 0 to 3\ncolumn 0 to 2:")
print(mat[0:3, 0:2])
print()
x = mat.copy()
x[0:3, 0:5] = 0
print(x)





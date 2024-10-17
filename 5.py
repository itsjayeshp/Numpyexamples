import numpy as np


#  Exercise -----

# arr = np.array([[4, 2, 1], [6, 4, 2]])
# arr = np.expand_dims(arr, axis=0)

# print(arr)



#  Exercise -----


# image = np.random.randint(
#     low=0, 
#     high=256, 
#     size=(200, 300, 3), 
#     dtype=np.uint8
# )
# image_extended = np.expand_dims(image, axis=0)
# print(image_extended)


#  Exercise -----


# image1 = np.random.randint(
#     low=0, 
#     high=256, 
#     size=(200, 300, 3), 
#     dtype=np.uint8
# )
# image2 = np.random.randint(
#     low=0, 
#     high=256, 
#     size=(200, 300, 3), 
#     dtype=np.uint8
# )

# image1 = np.expand_dims(image1, axis=0)
# image2 = np.expand_dims(image2, axis=0)
# images = np.append(image1, image2, axis=0)
# print(images)


#  Exercise -----

# arr = np.array([[[1, 2, 3], [6, 3, 2]]])
# arr = np.squeeze(arr)

# print(arr)


#  Exercise -----


# arr = np.array([[0.4], [0.9], [0.5], [0.6]])
# arr = np.squeeze(arr)

# print(arr)

#  Exercise -----


# arr = np.array(
#     [
#         [4.99, 3.49, 9.99],
#         [1.99, 9.99, 14.99],
#         [14.99, 2.39, 7.29],
#     ]
# )

# arr = np.ravel(arr)
# print(arr)

#  Exercise -----


# arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# row = arr[np.newaxis, :]
# column = arr[:, np.newaxis]

# print(row)
# print(column)

#  Exercise -----


arr = np.full((10, 4), fill_value=False)
arr = arr.reshape(5, 2, 4)
print(arr)


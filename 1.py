import numpy as np


#  Exercise -----
# arr  = np.zeros(shape=(5,5), dtype='int16')
# print(arr)


#  Exercise -----

# Solution I:
# arr = np.ones(shape=(10,10) , dtype='float32') * 8
# print(arr)

# Solution II:
# arr = np.full(shape=(10,10) , fill_value=8 , dtype='float32')
# print(arr)


#  Exercise -----

# arr = np.arange(10,100)
# print(arr)


#  Exercise -----

# Solution I:
# arr = np.arange(10, 100).reshape(-1, 10)
# print(arr)

# Solution II:
# arr = np.arange(10, 100).reshape(9, 10)
# print(arr)

# Solution III:
# arr = np.arange(10, 100).reshape(9, -1)
# print(arr)


#  Exercise -----


# arr = np.eye(N=8, dtype='int16')
# print(arr)


#  Exercise -----

# arr = np.array(
#     [
#         [
#             [1,2,3,4],
#             [5,6,7,8],
#             [9,8,7,6],
#         ],
#          [
#             [7, 2, 3, 1],
#             [6, 2, 0, 9],
#             [0, 1, 9, 1],
#         ],
#     ]
# )
# print(arr)
# print(arr.ndim)


#  Exercise -----


# arr = np.array(
#     [
#         ['4', '3', '6', '2', '1'],
#         ['7', '2', '1', '2', '6'],
#     ],
#     dtype='<U1',
# )

# print(arr)
# arr = arr.astype('float16')
# print(arr)


#  Exercise -----


# arr = np.array([4, 5, 67, 8, 2])
# print(arr)
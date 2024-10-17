import numpy as np

#  Exercise -----



# A = np.array(
#     [
#         [False, True, True, False, True],
#         [False, False, True, True, True],
#         [True, False, False, True, False],
#     ]
# )
# B = np.array(
#     [
#         [
#             [False, True, True, False, True],
#             [False, False, True, True, True],
#             [True, False, False, True, False],
#         ]
#     ]
# )
# C = np.array(
#     [
#         [[False, True, True, False, True]],
#         [[False, False, True, True, True]],
#         [[True, False, False, True, False]],
#     ]
# )

# print(A.shape)
# print(B.shape)
# print(C.shape)





#  Exercise -----


# A = np.array(
#     [
#         [False, True, True, False, True],
#         [False, False, True, True, True],
#         [True, False, False, True, False],
#     ]
# )
# B = np.array(
#     [
#         [
#             [False, True, True, False, True],
#             [False, False, True, True, True],
#             [True, False, False, True, False],
#         ]
#     ]
# )
# C = np.array(
#     [
#         [[False, True, True, False, True]],
#         [[False, False, True, True, True]],
#         [[True, False, False, True, False]],
#     ]
# )
# D = np.array([True, False])

# print(A.ndim)
# print(B.ndim)
# print(C.ndim)
# print(D.ndim)



#  Exercise -----


# arr = np.array(
#     [
#         [6, 7, 7, 3, 9],
#         [7, 4, 8, 4, 0],
#         [1, 5, 3, 2, 4],
#         [7, 8, 9, 8, 2],
#     ]
# )
# print(arr.size)


#  Exercise -----


# A1 = np.array([3, 5, 1])
# A2 = np.array([3, 5, 1], dtype=np.int8)
# A3 = np.array([3, 5, 1], dtype=np.int16)
# A4 = np.array([3, 5, 1], dtype='float')

# print(A1.itemsize)
# print(A2.itemsize)
# print(A3.itemsize)
# print(A4.itemsize)


#  Exercise -----


# A1 = np.array([3, 5, 1])
# A2 = np.array([3, 5, 1], dtype=np.int8)
# A3 = np.array([3, 5, 1], dtype=np.int16)
# A4 = np.array([3, 5, 1], dtype='float')

# print(A1.nbytes)
# print(A2.nbytes)
# print(A3.nbytes)
# print(A4.nbytes)


#  Exercise -----


# A1 = np.array([3, 5, 1, 2, 5, 4])
# A2 = np.array([3, 5, 1, 4, 7, 3, 8, 24], dtype=np.int8)
# A3 = np.array([3, 5, 1, 6, 2], dtype=np.int16)

# total = {'A1': A1.nbytes, 'A2': A2.nbytes, 'A3': A3.nbytes}

# print(min(total, key=total.get))



#  Exercise -----



# arr = np.array(
#     [
#         [3, 4, 0, 5, 6],
#         [9, 7, 4, 0, 6],
#         [1, 9, 6, 7, 9],
#         [7, 6, 9, 8, 8],
#         [2, 2, 1, 5, 2],
#         [9, 7, 5, 5, 9],
#         [6, 9, 9, 5, 2],
#         [9, 6, 1, 8, 1],
#     ],
#     dtype='float64',
# )

# print('float64:', arr.nbytes)
# print('float32:', arr.astype('float32').nbytes)
# print('int16:', arr.astype('int16').nbytes)



#  Exercise -----




# Solution I:
# arr = np.zeros((3, 8, 4), dtype='int')
# arr = arr.reshape(-1, arr.shape[2])

# print(arr)


# Solution II:
# arr = np.zeros((3, 8, 4), dtype='int')
# arr = arr.reshape(3 * 8, 4)

# print(arr)
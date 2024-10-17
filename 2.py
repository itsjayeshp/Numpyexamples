import numpy as np



#  Exercise -----



# arr = np.diag(np.arange(10))
# print(arr)


#  Exercise -----


# arr = np.ones(shape=(4, 4), dtype='int')
# arr = np.pad(arr * 5, pad_width=1, constant_values=0)
# print(arr)


#  Exercise -----

# arr = np.zeros(shape=(6, 6), dtype='int')
# arr[::2, ::2] = 2
# arr[1::2, ::2] = 4
# print(arr)


#  Exercise -----


# arr = np.array(
#     [
#         [4.99, 3.49, 9.99],
#         [1.99, 9.99, 14.99],
#         [14.99, 2.39, 7.29],
#     ]
# )
# result = np.zeros_like(arr)
# print(result)


#  Exercise -----


# arr = np.array(
#     [
#         [4.99, 3.49, 9.99],
#         [1.99, 9.99, 14.99],
#         [14.99, 2.39, 7.29],
#     ]
# )
# result = np.full_like(arr, 9.99)
# print(result)


#  Exercise -----


# arr = np.tri(N=6)
# print(arr)


#  Exercise -----


# arr = np.array(
#     [
#         [False, True, True, False, True],
#         [False, False, True, True, True],
#     ]
# )
# arr = arr.astype('int')
# print(arr)


#  Exercise -----


arr = np.array([[4, 5, 67, 8, 2, 4], [4, 2, 5, 7, 2, 5]], dtype='int32')
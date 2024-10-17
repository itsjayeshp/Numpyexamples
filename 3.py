import numpy as np

#  Exercise -----


# rates = [
#     [1.97, 1.04, 1.35, 2.17, 2.29, 4.38],
#     [1.34, 2.04, 1.37, 2.09, 1.29, 3.38],
# ]
# arr = np.asarray(rates)
# print(arr)


#  Exercise -----


# title = 'hello my name is jayesh and i am numpy dev'
# tokens = title.split(' ')
# arr = np.asarray(tokens).reshape(2, -1)
# print(arr)



#  Exercise -----


# arr = np.tile(np.arange(10), (5, 2))
# print(arr)


#  Exercise -----

# arr = np.array(
#     [
#         [[3, 2, 4, 0, 1, 3], [5, 0, 4, 4, 4, 1], [3, 2, 4, 1, 1, 4]],
#         [[5, 5, 4, 5, 1, 3], [2, 2, 5, 2, 4, 0], [5, 1, 3, 4, 2, 3]],
#     ]
# )
# result = np.ones_like(arr)
# print(result)



#  Exercise -----


# arr = np.concatenate(
#     (
#         np.linspace(0, 1, 11).reshape(1, -1),
#         np.zeros((4, 11)),
#     ),
#     axis=0,
# )
# print(arr)



#  Exercise -----


# x = np.linspace(0, 1, 11)
# y = np.linspace(0, 1, 11)
# xx, yy = np.meshgrid(x, y)
# print(xx)
# print(yy)



#  Exercise -----



# Solution I:
# string_data = '4 2 6 2 7 10 6 2 14'
# arr = np.fromstring(string_data, dtype='int16', sep=' ')

# print(arr)


# Solution II:
# string_data = '4 2 6 2 7 10 6 2 14'
# arr = np.array([int(num) for num in string_data.split()], dtype='int16')

# print(arr)



#  Exercise -----

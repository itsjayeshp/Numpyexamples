import numpy as np

# myarr = np.array([[1,2,3,4],[23,4,5,6]])
# # print(myarr)
# arr = np.array([1,2,3,4,5,6,7,8,9])

# arange = np.arange(-100,-10,2)
# # print(arange)

# zero = np.zeros((5,3))
# print(zero)

# print(np.ones((4,4)))


# print(np.linspace(0,10,11))
# print(np.eye(5))

# print(np.random.rand(5,3))

# print(np.random.randn(10))
# print(np.random.randn(2,3))

# print(np.random.randint(0,11,4))
# print(np.random.randint(0,11,(2,4)))


# np.random.seed(42)
# print(np.random.rand(1))

# np.random.seed(42)
# print(np.random.rand(1))


# arr1 = np.arange(0,20)
# print(arr1.reshape(4,5))

# arnarr = np.random.randint(0,101,10)
# print(arnarr)
# print(arnarr.min())
# print(arnarr.max())
# print(arnarr.argmax())
# print(arnarr.argmin())
# print(arnarr.dtype)
# print(arnarr.shape)
# a = arnarr.reshape(2,5)
# print(a.shape)


arr = np.arange(0,11)
# print(arr)
# print(arr[1])
# print(arr[1:5])
# print(arr[0:5])
# print(arr[:5])
# print(a = arr[5:])

# arr[0:5] =100
# print(arr)

# slice_Of_Arry = arr[0:5]
# print(slice_Of_Arry)     [0 1 2 3 4]

# slice_Of_Arry[:] = 99
# print(slice_Of_Arry)    [99 99 99 99 99] 

# print(arr)   [99 99 99 99 99  5  6  7  8  9 10]

# arr_Copy = arr.copy()
# arr_Copy[:] =  99

# print(arr_Copy)   [99 99 99 99 99 99 99 99 99 99 99]
# print(arr)   [ 0  1  2  3  4  5  6  7  8  9 10]



arr_2d = np.array([[1,2,3],[4,5,6],[7,8,9]])


# print(arr_2d)  
        # [[1 2 3]
        #  [4 5 6]
        #  [7 8 9]]           


# print(arr_2d.shape)       (3, 3)
# print(arr_2d[0])      [1 2 3]
# print(arr_2d[2])            [7 8 9]
# print(arr_2d[1][1])     5
# print(arr_2d[1,1])     5
# print(arr_2d[0,2])     3

# print(arr_2d[:2])
# [[1 2 3]
#  [4 5 6]]
# print(arr_2d[:2,1:])    
# [[2 3]
#  [5 6]] 


# arr = np.arange(1,11)
# print(arr)               [ 1  2  3  4  5  6  7  8  9 10]
# print(arr > 4)         [False False False False  True  True  True  True  True  True]

# bool_arr = arr > 4
# print(arr[bool_arr])            [ 5  6  7  8  9 10] indexes
# print(arr[arr> 4])    [ 5  6  7  8  9 10]


# ----------------------------

arr = np.arange(0,11)
# print(arr)              [ 0  1  2  3  4  5  6  7  8  9 10]
# print(arr + 5)  [ 5  6 7  8  9 10 11 12 13 14 15]/
# print(arr - 2)   [-2 -1  0  1  2  3  4  5  6  7  8]

# print(arr + arr)   [ 0  2  4  6  8 10 12 14 16 18 20]
# print(arr* arr)   [  0   1   4   9  16  25  36  49  64  81 100]
# print(arr / arr)   RuntimeWarning  [nan  1.  1.  1.  1.  1.  1.  1.  1.  1.  1.]

# print(np.sqrt(arr))
# print(np.sin(arr))
# print(np.log(arr))

# print(arr.sum())  55
# print(arr.mean())   5.0
# print(arr.max())  10
# print(arr.var())  10.0
# print(arr.std())   3.1622776601683795

arr2d = np.arange(0,25).reshape(5,5)
# print(arr2d)
# print(arr2d.sum())    300
# print(arr2d.sum(axis=0))  [50 55 60 65 70]
# print(arr2d.sum(axis=1))    [ 10  35  60  85 110]



# exercise=================


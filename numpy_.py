# import numpy

# # a = numpy.random.randint(1, 10, (5, 5))

# # b = numpy.random.randint(1, 10, (5, 5))


# # print(a.shape)
# # print(a.sum())
# # print(a.ndim)
# # print(a.size)
# # print(a.dtype)
# # print(a[:,2]) lay cot 2
# # c = numpy.arange(12)
# # c = c.reshape((4,3))
# # print(c)
# # ** = exponnent
# # print(a>5)
# # print(a[a>2])
# # print(a[a!=2])
# # print(a)
# # print(a[1:4,1:4]) copy hang 1 4 cot 1 4


# # b=numpy.full((5,5),0)
# # [[0 0 0 0 0]
# #  [0 0 0 0 0]
# #  [0 0 0 0 0]
# #  [0 0 0 0 0]
# #  [0 0 0 0 0]]

# # b=numpy.linspace(0,1,10)
# # [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556
# #  0.66666667 0.77777778 0.88888889 1.        ]

# # numpy.random.seed(0)
# # b=numpy.random.random((4,4))          *** seed ***

# # b=numpy.array([2,4,6])

# # print(b.std())     do lech chuan
# # print(b.mean())    trung binh cong

# # b = numpy.random.normal(100, 2, (4, 4)) # mean std size
# # [[100.47434514  97.30210326 100.77097575 100.05257759]
# #  [ 97.37753209  97.48033056 103.79640591 101.01925668]
# #  [ 98.71072205 102.87928033  97.51533889 102.27740562]
# #  [ 99.96321722  99.82455273 100.80341041  96.51555803]]


# # c = numpy.concatenate((a, b))


# #  [[4 7 3 6 1]   intergrate a , b
# #  [4 3 7 3 4]
# #  [9 2 6 1 6]
# #  [8 7 1 9 8]
# #  [9 6 1 1 8]
# #  [1 5 6 6 8]
# #  [8 2 1 3 1]
# #  [6 7 3 9 8]
# #  [7 9 2 9 1]
# #  [8 8 3 7 2]]


# # c = numpy.vstack((a, b))
# # c = numpy.hstack((a, b))



# # [[1 9 3 5 6 9 2 9 1 5]
# #  [3 4 9 3 1 6 6 3 2 3]
# #  [6 2 2 6 1 1 3 6 2 8]
# #  [1 6 5 9 3 8 2 6 8 8]
# #  [5 7 1 2 8 2 9 6 7 6]]
# # vstack  vertical
# # hstack  horizontal

# # c, c2, c3 = numpy.split(a, [2, 5])
# # [[3 5 8 9 1]
# #  [2 3 2 7 1]]


# # c = numpy.sort(c, axis=0)  # sort theo cot
# # c = numpy.sort(c, axis=1)  # sort theo hang

# numpy.random.seed(69)
# c = numpy.random.randint(0, 10, (3, 3))
# numpy.random.seed(67)
# b = numpy.random.randint(0, 10, (3, 3))
# print(b)
# print(c)
# print(c.dot(b))  #  bang voi c@b 

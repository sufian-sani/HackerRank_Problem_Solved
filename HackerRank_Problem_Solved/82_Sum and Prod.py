import numpy

N, M = map(int, input().split())
storage = numpy.array([input().split() for _ in range(N)],dtype=int)

print(numpy.prod(numpy.sum(storage, axis=0)))
# print(numpy.prod(storage))

'''
my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.prod(my_array, axis = 0))             #Output : [3 8]
print(numpy.prod(my_array, axis = 1))             #Output : [ 2 12]
print(numpy.prod(my_array, axis = None))          #Output : 24
print(numpy.prod(my_array))                       #Output : 24
'''
'''
my_array = numpy.array([ [1, 2], [3, 4] ])

print(numpy.sum(my_array, axis = 0))          #Output : [4 6]
print(numpy.sum(my_array, axis = 1))          #Output : [3 7]
print(numpy.sum(my_array, axis = None))       #Output : 10
print(numpy.sum(my_array))                    #Output : 10
'''
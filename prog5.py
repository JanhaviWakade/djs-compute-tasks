import numpy

def arrays(arr):
    l=list(numpy.array(arr,float))
    l.reverse()
    l=numpy.array(l)
    return l
arr = input().strip().split(' ')
result = arrays(arr)
print(result)
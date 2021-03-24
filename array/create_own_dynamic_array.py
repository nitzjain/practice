'''
the aim is to create your own dynamic array.
If the array gets filled up, then double the size of the array.
So we create a new array with double the size and rename it to the first array.
We use ctypes library to create an array object.
'''

import ctypes

class DynamicArray(object):
    #init method. Has 3 components to initialize
    def __init__(self):
        self.n = 0 #element count
        self.capacity = 1 #array capacity
        self.A = self.make_array(self.capacity) #make array is a func we will create which will create an array with the given capacity. A is just a reference for array name.

    #length method to give the array's length
    def __len__(self):
        return self.n

    #retrieve an element from the array. If the index k is out of bounds, return error else return the value at k.
    def __getitem__(self, k):

        if not 0 <= k < self.n:
            return IndexError('K is out of bounds!!!!')

        return self.A[k]

    #add an element to the array. If the elements are more, double the size of the array.
    def append(self,element):

        if self.n == self.capacity:
            self._resize(2*self.capacity)

        self.A[self.n] = element
        self.n += 1
    #user defined function to create a new array B, copy all elements of A to B  and rename B to A.
    def _resize(self,new_cap):
        B = self.make_array(new_cap)
        for i in range(self.n):
            B[i] = self.A[i]
        self.A = B
        self.capacity = new_cap

    #using ctypes to make actual object.
    def make_array(self,new_cap):
        return (new_cap * ctypes.py_object)()



#actual call
D = DynamicArray()
D.append(1444)
print(D.__getitem__(0))
D.append(2000)
print(D.__getitem__(1))
print(D.__len__())

#or
C = DynamicArray()
C.append(12)
print(C[0])
C.append(20)
print(C[1])
print(len(C))

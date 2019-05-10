import numpy as np 
array = np.array([[1,2,3,4,5],[6,7,8,9,10]])  # vector 1D
print(array)
print("Dimension :",array.shape)

# dynamic array , we are going to exdend double size of array
import ctypes

class DynamicArray(object):
    # initializer ( constructor )
    def __init__(self):
        self.n = 0 # number of elements
        self.capacity = 1 # capacity 
        self.A = self.make_array(self.capacity) # it's how to change array 

    def __len__(self):
        """
        return element number
        """
        return self.n
    def __getitem__(self,k):
        """
        return value of the index which given
        """
        if not 0 <=k<self.n:
            return IndexError("k is out of bound")
        return self.A[k]

    def append(self,eleman):
        """
        append element to array
        """
        # if the array is full, make it double
        if self.n == self.capacity:
            self._resize(2*self.capacity)
        self.A[self.n] = eleman # element add
        self.n +=1 # increase number of element1 
    def _resize(self,new_cap):
        """
        increase array capacity
        """
        B = self.make_array(new_cap) # new array

        # move old array(A) values to new array (B)

        for k in range(self.n):
            b[k] = self.A[k]
        
        self.A = B 
        self.capacity = new_cap # update the capacity

    
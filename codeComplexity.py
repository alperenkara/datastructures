# which algorithm is better ?

def sum_square1(x):

    sum = 0 

    for x in range(1,x+1):
        sum += x**2
    return sum

def sum_square2(x):
    
    return (x*(x+1)*(2*x+1))/6

# Big O Notation
# 1)Why we use Big-O rather then Runtime ?
     # to eleminate CPU differences
# 2)Why imput size is important ?
    # because we use input size in Big-O

    

# which algorithm is better ?

def sum_square1(x):

    sum = 0 

    for x in range(1,x+1):
        sum += x**2
    return sum

def sum_square2(x):
    
    return (x*(x+1)*(2*x+1))/6

# Big O Notation


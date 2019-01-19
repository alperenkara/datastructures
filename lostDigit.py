"""
Input = 10 - x = 4
Output = 6

Input = 1x * 11 = 121
Output = 1

Input = 1x0 / 3 = 50
Output = 5
"""

def lostDigit(string):
    # give values to x between 0-9
    # write before the equation
    # write after equation
    # compare them 

    for i in range(10):
        #i-> 0 1 2 3 4 5.. 9
        c = string.replace("x",str(i))
        # it will change every "x" from string with i value
        k = string.index("=")
        if eval(c[:k]) == eval(c[k+1:]):
            return print(str(i))

lostDigit("12x / 11 = 11")
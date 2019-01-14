# factorial


def factorial(m):
    f = 1
    for i in range(1, m + 1):
        f = f * i
    return f


print(factorial(5))

# reverse word
# input = "istanbul"
# output = "lubnatsi"


def reverse(m):
    result = ""
    # result = []
    # result = list()
    # start, stop, step
    for i in range(len(m)-1, -1, -1):
        result += m[i]
    return result


print(reverse("istanbul"))


def reverse2(k):
    return k[::-1]

print(reverse2("alperen"))

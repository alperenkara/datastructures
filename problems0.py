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
        # m=8, m[7] 6 5 4 3 2 1 0
        result += m[i]
    return result


print(reverse("istanbul"))


def reverse2(k):
    return k[::-1]

print(reverse2("alperen"))
deneme = "1234"
print(deneme[::-1])
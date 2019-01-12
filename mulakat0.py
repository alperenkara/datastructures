# Deep copy ve Shallow copy arasindaki farklar ?
# Deep Copy'de yeni liste degismedi
import copy
old_list = [[1, 1, 1], [2, 2, 2]]
new_list = copy.deepcopy(old_list)
old_list[0][2] = 2000
print("Old list : {}".format(old_list))
print("New list : {}".format(new_list))
# Shallow Copy'de yeni liste degisti
old_list = [[1, 1, 1], [2, 2, 2]]
new_list = copy.copy(old_list)
old_list[1][2] = 2000
print("Shallow Old list : {}".format(old_list))
print("Shallow New list : {}".format(new_list))

# list ve tuple arasindaki farklar
liste = [1,2,3,4,5,6,7]
liste[3] = 100
print(liste)
tup = (1,2,3,4,5,6,7)
# tup[3] = 200
print(tup)

dictionary = {"ankara":1000, "istanbul":2000}
print(dictionary["ankara"])

# when we don't know how many input arguments we will use, we put *args
# kwargs works in dictionary logic
def deneme(*args):
    for each in args:
        print(each)
print(deneme(1,2,3,4,5))

def deneme2(**kwargs):
    for each in kwargs:
        print(each,kwargs[each])

print(deneme2(a='!',b=2,c=3,d=4,e=5))
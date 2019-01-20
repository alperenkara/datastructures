# array rotation
# input = [2,3,4,5]
# output = [4,5,2,3]

def arrayRotation(list):
    new_index_first = list[0]
    new_list_second = list[:new_index_first]
    del list[:new_index_first]
    new_list = list + new_list_second
    return print(new_list)

arrayRotation([3,4,5,6,7,8,9,10])

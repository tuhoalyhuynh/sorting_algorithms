import math


def merge(arr1, arr2):
    output = []
    target_output_legth  = len(arr1) + len(arr2)

    while len(output) < target_output_legth:
        if len(arr1) == 0:
            output += arr2
            arr2 = []
        elif len(arr2) == 0:
            output += arr1
            arr1 = []
        elif arr1[0] < arr2[0]:
            output.append(arr1[0])
            arr1 = arr1[1:]
        else:
            output.append(arr2[0])
            arr2 = arr2[1:]

    return output

def merge_sort(arr):
    pass

def split(arr):
    midpoint = len(arr)//2
    arr1 = arr[:midpoint]
    arr2 = arr[midpoint:]

    if len(arr1) <= 1 and len(arr2) <= 1:
        return merge(arr1, arr2)

    split_arr1 = split(arr1)
    split_arr2 = split(arr2)

    return merge(split_arr1, split_arr2)

print(split([100,2,3,400,5,6,7,8]))

# print(merge_sort([0,4,1,5,7]))
# print(merge([2,3], [3,6]))
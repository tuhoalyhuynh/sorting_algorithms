import math

def merge_sort(arr):
    unsorted_arr = []
    if len(arr) == 1:
        unsorted_arr.append(arr[0])

    if len(arr) % 2 == 0:
        mid = len(arr)//2
        left_array = [arr[:mid]]
        right_array = [arr[mid:]]
        merge_sort(left_array)
        merge_sort(right_array)
        print(left_array)
        print(right_array)
    else:
        mid = len(arr)//2
        left_array = [arr[:math.floor(mid)]]
        mid_array = [arr[math.floor(mid)]]
        right_array = [arr[math.ceil(mid):]]
        merge_sort(left_array)
        # merge_sort(mid_array)
        merge_sort(right_array)
        print(left_array)
        print(right_array)

    return unsorted_arr



print(merge_sort([0,4,1,5,7]))
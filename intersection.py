# def intersection(arr1, arr2):
#     match_arr = []
#     for i in arr1:
#         # value1 = arr1[i]
#         for j in arr2:
#             # value2 = arr2[j]
#             if i == j:
#                 match_arr.append(i)
#     return match_arr

def intersection(arr1, arr2):
    output = {}
    arr3 = []

    for a in arr1:
        output[str(a)] = True

    for b in arr2:
        if str(b) in output:
            arr3.append(b)

    return arr3

print(intersection([0,1,4,5,8],[0,2,7,9,4]))
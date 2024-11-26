# Given an array arr, the goal is to find out the smallest number that is repeated exactly ‘k’ times.
# Note: If there is no such element then return -1.


def findDuplicate(arr, k):
    count_dict = {}
    for num in arr:
        count_dict[num] = count_dict.get(num, 0) + 1
    candidates = [num for num, count in count_dict.items() if count == k]
    if candidates:
        return min(candidates)
    return -1


print(findDuplicate([2, 2, 5, 2, 4, 8, 9], 3))

# Given two arrays arr1 and arr2 of equal size, the task is to find whether the given arrays are equal. Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.


def check(arr1, arr2) -> bool:
    arr1.sort()
    arr2.sort()
    if arr1 == arr2:
        return True
    else:
        return False


print(check([1, 5, 9, 2, 4], [4, 2, 5, 1, 9]))

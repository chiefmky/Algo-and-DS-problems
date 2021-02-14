# Packaging Automation
def maxItems(numGroups, arr):
    print("Original Array : ", arr)
    arr.sort()
    arr[0] = 1
    for i in range(1, numGroups):
        if arr[i] - arr[i - 1] > 1:
            arr[i] = arr[i - 1] + 1
    print("Rearranged arr ", arr)
    return arr[-1]
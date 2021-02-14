def stringMan(mystr, N, M):
    # mystr[N:M+1].sort(reverse = True)
    print(mystr[N:M+1])
    print(mystr[N:M+1].sort())
    return mystr

def rotate3x3(a):
    if len(a) == 0 or len(a) != len(a[0]):
        return False
    n = len(a)

    top = a[0]
    bottom = a[-1]
    right = column(a, len(a) - 1)
    right = right[::-1]
    left = column(a, 0)
    left = left[::-1]

    temp = []

    for i in range(len(top)):
        temp.append(top[i])

    # left to top
    for i in range(len(top)):
        a[0][i] = left[i]

    # bottom to left
    for i in range(len(left)):
        a[i][0] = bottom[i]

    # right to bottom
    for i in range(len(bottom)):
        a[-1][i] = right[i]

    # top to right
    for i in range(len(right)):
        a[i][-1] = temp[i]
    return a

def column(matrix, i):
    return [row[i] for row in matrix]

def rotateImage(a):
    if len(a) == 0 or len(a) != len(a[0]):
        return False
    n = len(a)

    for layer in range(0, n // 2):
        first = layer
        last = n - 1 - first
        for i in range(first, last):
            offset = i - first
            top = a[first][i]
            bottom = a[last][last - offset]
            left = a[last - offset][first]
            right = a[i][last]

            # //left -> top
            a[first][i] = left

            # bottom ->left
            a[last - offset][first] = bottom

            # right -> bottom
            a[last][last - offset] = right

            # top ->right
            a[i][last] = top
    return a

def rotate(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: void Do not return anything, modify matrix in-place instead.
    """
    n = len(matrix[0])
    # transpose matrix
    for i in range(n):
        for j in range(i, n):
            matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]

            # reverse each row
    for i in range(n):
        matrix[i].reverse()

def mergeTwoArr(self, l1: list, l2: list) -> list:

    l3 = [None] * (len(l1) + len(l2))

    i, j, k = 0, 0, 0

    while i < len(l1) and j < len(l2):
        if l1[i] <= l2[j]:
            l3[k] = l1[i]
            i += 1
        else:
            l3[k] = l2[j]
            j += 1
        k += 1

    while i < len(l1):
        l3[k] = l1[i]
        i += 1
        k += 1

    while j < len(l2):
        l3[k] = l2[j]
        j += 1
        k += 1

    return l3


if __name__ == "__main__":
    root = [2, 5, 1]
    stack, output = [root, ], []

    print(stack)
    print(output)

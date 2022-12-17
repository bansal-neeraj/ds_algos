matix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

n = len(matix[0])
for layer in range(n // 2):
    start = layer
    end = n - 1 - layer

    top, left, bottom, rigth = [], [], [], []
    for i in range(start, end + 1):
        # store top
        top1 = matix[layer][i]

        # # left -> top
        matix[layer][i] = matix[n - 1 - i][layer]

        # bottom -> left
        matix[n - 1 - i][layer] = matix[n - 1 - layer][n - 1 - i]
        # print('bottom',matix[n - 1 - layer][n - 1 - i])
        # # right -> bottom
        matix[n - 1 - layer][n - 1 - i] = matix[i][n-1-layer]
        # # top -> right
        matix[i][n-1-layer] = top1

        top.append(matix[layer][i])
        left.append(matix[n-1-i][layer])
        bottom.append(matix[n-1-layer][n-1-i])
        rigth.append(matix[i][n-1-layer])

# print(top)
# print(left)
# print(bottom)
# print(rigth)

print(matix)

matrix =[
    [1,0,0,1,1,0],
    [0,1,0,0,1,0],
    [0,0,1,0,1,1],
    [1,1,0,1,0,0],
    [1,0,0,1,1,0],
    [0,0,1,0,1,1]
    ]

for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        neshane = matrix[i][j]
        if neshane == 0:
            continue
        else:
            if j<1 and i==0:
                if matrix[i][j+1] == 1 or matrix[i+1][j] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if j>4 and i==0:
                if matrix[i][j-1] == 1 or matrix[i+1][j] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if j<1 and i>4:
                if matrix[i-1][j] == 1 or matrix[i][j+1] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if j>4 and i>4:
                if matrix[i][j-1] == 1 or matrix[i-1][j] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if (j>0 and j<5)and(i==0):
                if matrix[i][j-1] == 1 or matrix[i][j+1] == 1 or matrix[i+1][j] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if (j==0)and (i>0 and i<5):
                if matrix[i-1][j] == 1 or matrix[i][j+1] == 1 or matrix[i+1][j] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if (j>0 and j<5)and(i == 5):
                if matrix[i-1][j] == 1 or matrix[i][j-1] == 1 or matrix[i][j+1] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if (j==5)and(i>0 and i<5):
                if matrix[i-1][j] == 1 and matrix[i][j-1] == 1 or matrix[i+1][j] == 1:
                    continue
                else:
                    matrix[i][j] = 0
            if (i<0 and i>5)and(j>0 and j<5):
                if matrix[i-1][j] == 1 or matrix[i][j-1] == 1 or matrix[i][j+1] == 1 or matrix[i+1][j]:
                    continue
                else:
                    matrix[i][j] = 0


print(matrix)



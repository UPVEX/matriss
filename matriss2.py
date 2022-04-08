matrix =[
    [1,0,0,1,1,0],
    [0,1,0,0,1,0],
    [0,0,1,0,1,1],
    [1,1,0,1,0,0],
    [1,0,0,1,1,0],
    [0,0,1,0,1,1]
    ]

def baresi(x,y,z):
    if x == 0 and y == 0:
        z = 0
        return z
    else:
        z = 1
        return z
def baresi_two(x,y,z,a):
    if x == 0 and y == 0 and z == 0:
        a = 0
        return a
    else:
        a = 1
        return a

def baresi_three(x,y,z,a,b):
     if x == 0 and y == 0 and z == 0 and a == 0:
        b = 0
        return b
     else:
        b = 1
        return b


for i in range(len(matrix)):
    for j in range(len(matrix[i])):
        neshane = matrix[i][j]
        if neshane == 0:
            continue
        else:
            if j<1 and i==0:
                matrix[i][j] = baresi(matrix[i][j+1],matrix[i+1][j],matrix[i][j])
            if j>4 and i==0:
                matrix[i][j] = baresi(matrix[i][j-1],matrix[i+1][j],matrix[i][j])
            if j<1 and i>4:
                matrix[i][j] = baresi(matrix[i-1][j],matrix[i][j+1],matrix[i][j])
            if j>4 and i>4:
                matrix[i][j] = baresi(matrix[i][j-1],matrix[i-1][j],matrix[i][j])
            if (j>0 and j<5)and(i==0):
                matrix[i][j] = baresi_two(matrix[i][j-1],matrix[i][j+1],matrix[i+1][j],matrix[i][j])
            if (j==0)and (i>0 and i<5):
                matrix[i][j] = baresi_two(matrix[i-1][j],matrix[i][j-1],matrix[i][j+1],matrix[i][j])
            if (j>0 and j<5)and(i == 5):
                matrix[i][j] = baresi_two(matrix[i-1][j],matrix[i][j-1],matrix[i][j+1],matrix[i][j])
            if (j==5)and(i>0 and i<5):
                matrix[i][j] = baresi_two(matrix[i-1][j],matrix[i][j-1],matrix[i+1][j],matrix[i][j])
            if (i<0 and i>5)and(j>0 and j<5):
                matrix[i][j] = baresi_three(matrix[i-1][j],matrix[i][j-1],matrix[i][j+1],matrix[i+1][j],matrix[i][j])

print (matrix)

                

def transpose(M):
    transposedMatrix = []
    if len(M) != 0:
        transposedMatrix = [[0] * len(M) for i in range(len(M[0]))]
        for i in range(len(M)):
            for j in range(len(M[0])):
                transposedMatrix[j][i] = M[i][j]
    return transposedMatrix

def powers(M,a,b):
    powered = [[0] * abs((a-1)-b) for i in range(len(M))]
    for i in range(len(powered)):
        n=a
        for j in range(len(powered[0])):
            if n<=b:
                powered[i][j] = M[i]**n
                n+=1
    return powered

def matmul(A,B):
    # nxk*kxm ger nxm
    matris = [[0 for i in range(len(B[0]))] for j in range(len(A))]
    # len(B[0]) ger n
    # len(A) ger m
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A[0])):
                matris[i][j] += A[i][k] * B[k][j]
    return matris

def invert(mat): # Städa upp koden här?
    a = mat[0][0]
    b = mat[0][1]
    c = mat[1][0]
    d = mat[1][1]

    det = a * d - b * c

    return [[d / det, -b / det], [-c / det, a / det]]

def loadtxt(file):
    with open(file) as texten: # Öppna filen
        listan = []
        for line in texten:
            line = line.split()
            if line: # om line finns
                line = [float(i) for i in line]
                listan.append(line)
    return listan



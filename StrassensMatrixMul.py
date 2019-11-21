from copy import deepcopy

sample0=[[4,5,4,2],
         [9,2,4,2],
         [3,6,4,2],
         [3,2,7,2]]

sample1=[[1,0,0,0],
         [0,1,0,0],
         [0,0,1,0],
         [0,0,0,1]]

def matrixadd(matrix0,matrix1):
    matrix2=[]
    for i in range(len(matrix0)):matrix2.append([0]*len(matrix0))
    for i in range(len(matrix0)):
        for v in range(len(matrix0)):
            matrix2[i][v]=matrix0[i][v]+matrix1[i][v]
    return matrix2

def matrixsub(matrix0,matrix1):
    matrix2=[]
    for i in range(len(matrix0)):matrix2.append([0]*len(matrix0))
    for i in range(len(matrix0)):
        for v in range(len(matrix0)):
            matrix2[i][v]=matrix0[i][v]-matrix1[i][v]
    return matrix2

def matrixmul(matrix0,matrix1):
    matrix0=deepcopy(matrix0)
    matrix1=deepcopy(matrix1)
    if len(matrix0)==1:return [[matrix0[0][0]*matrix1[0][0]]]
    sidelen=len(matrix0)//2
    a=[i[:sidelen] for i in matrix0[:sidelen]]
    b=[i[sidelen:] for i in matrix0[:sidelen]]
    c=[i[:sidelen] for i in matrix0[sidelen:]]
    d=[i[sidelen:] for i in matrix0[sidelen:]]
    e=[i[:sidelen] for i in matrix1[:sidelen]]
    f=[i[sidelen:] for i in matrix1[:sidelen]]
    g=[i[:sidelen] for i in matrix1[sidelen:]]
    h=[i[sidelen:] for i in matrix1[sidelen:]]
    p1=matrixmul(a,matrixsub(f,h))
    p2=matrixmul(matrixadd(a,b),h)
    p3=matrixmul(matrixadd(c,d),e)
    p4=matrixmul(d,matrixsub(g,e))
    p5=matrixmul(matrixadd(a,d),matrixadd(e,h))
    p6=matrixmul(matrixsub(b,d),matrixadd(g,h))
    p7=matrixmul(matrixsub(a,c),matrixadd(e,f))
    r=matrixsub(matrixadd(p5,matrixadd(p4,p6)),p2)
    s=matrixadd(p1,p2)
    t=matrixadd(p3,p4)
    u=matrixsub(matrixsub(matrixadd(p1,p5),p3),p7)
    return [r[i]+s[i] for i in range(sidelen)]+[t[i]+u[i] for i in range(sidelen)]
print(matrixmul(sample0,sample1))
    

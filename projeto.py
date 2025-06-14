import random as r
#inicializar matriz
matriz=[]
for i in range(6):
    matriz.append([0]*6)
satelites=0
# colocar 0s e 1s
while satelites<4:
    i=r.randint(0,5)
    j=r.randint(0,5)
    if matriz[i][j]!=1:
        matriz[i][j]=1
        satelites+=1


print(matriz)
import random as r

#funcao para printar matriz bonita
def mostramatriz(entrada):
    for i in range(len(entrada)):
        linha=""
        for j in range(len(entrada[i])):
            linha+=" "+str(entrada[i][j])
        print("[",linha, "]")

#inicializar matriz real e a que o usuario ve
matriz=[]
amostradinha=[]
for i in range(6):
    matriz.append([0]*6)
    amostradinha.append(['?']*6)
satelites=0

# colocar 0s e 1s em lugares aleatorios(1 e o satelite)
while satelites<4:
    i=r.randint(0,5)
    j=r.randint(0,5)
    if matriz[i][j]!=1:
        matriz[i][j]=1
        satelites+=1

# loop de acoes do jogo de fato
encontrados=0
while encontrados<4:
    print("Aqui o tabuleiro")
    mostramatriz(amostradinha)
    linha=int(input("Fala qual linha voce acha que o satelite ta (numero de 0 a 5)"))
    coluna=int(input("Agora coluna"))
    if#........

mostramatriz(matriz)

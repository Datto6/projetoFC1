import random as r

#funcao para printar matriz bonita
def mostramatriz(entrada):
    for i in range(len(entrada)):
        linha=""
        for j in range(len(entrada[i])):
            linha+=" "+str(entrada[i][j])  #usa str para concatenar a matriz que era int antes
        print("[",linha, "]")

#inicializar matriz real e a que o usuario ve
matriz=[]
amostradinha=[]
for i in range(6):
    matriz.append([0]*6)
    amostradinha.append(['?']*6)


# colocar 0s e 1s em lugares aleatorios(1 e o satelite)
satelites=0 #Controla qntd de satelites
while satelites<4:
    i=r.randint(0,5)
    j=r.randint(0,5)
    #Condicao impede redundancia(satelites em lugares distintos)
    if matriz[i][j]!=1:
        matriz[i][j]=1
        satelites+=1

# loop de acoes do jogo de fato
encontrados=0
tentativas=0 #conta o numero de tentativas
pontosfeitos=[] #guarda par coordenada em tupla p o usuario n entrar um ponto duas vezes e mudar de X--> . 
while encontrados<4:
    print("Aqui o tabuleiro:")
    mostramatriz(amostradinha) #printa resultado de rodada anterior ou rodada 0 na 1 vez
    linha=int(input("Fala qual linha voce acha que o satelite ta (numero de 0 a 5)"))
    coluna=int(input("Agora coluna"))
    while linha>5 or coluna>5 or linha<0 or coluna<0:
        print("Input errado, entre 0 e 5.")
        linha=int(input("Linha."))
        coluna=int(input("Coluna"))
    #Avaliar se o usuário acertou ou errou
    if matriz[linha][coluna]==1 and (linha,coluna) not in pontosfeitos:
        amostradinha[linha][coluna]="X"
        matriz[linha][coluna]=-1
        encontrados+=1
    elif (linha,coluna) in pontosfeitos: #impede erro de -1-->0 e X--> . se usuario repetir ponto ja modificado
        print("Voce ja deu essa coordenada, + uma tentativa pelo amor de deus ")
    else: #errou
        amostradinha[linha][coluna]="."
    pontosfeitos.append((linha,coluna))
    tentativas+=1

if encontrados==4: #printar numero de tentativas e aproveitamento porque sim
    print("Voce precisou de "+str(tentativas),"para terminar. Tabuleiro final abaixo")
    mostramatriz(amostradinha)
    aproveitamento=4/tentativas
    print("Aproveitamento de ",round(aproveitamento*100), "%")

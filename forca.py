import random 
# Cria uma lista de palavras
palavras= ['python', 'programacao', 'computador']

# Sorteio das palavras
palavra_sorteada= random.choice(palavras)

# String com traços que representam as letras
# o len vale pela palavra escolhida aleatoriamente e imprime a mesma quantidade de letras como "-"
palavras_escondida = '-' * len(palavra_sorteada)

letras_adivinhadas = []

max_tentativas = 5

while True:
    # mostra a palavra escondida 
    print(palavras_escondida)
    
    letra = input("Digite uma letra: ")
    
    #verifica se a letra já foi digitada
    if letra in letras_adivinhadas:
        print("Essa letra já foi digitada, tente outra")
        continue
    # caso não for repitida, ela é adicionada a lista de letras_adivinhadas
    letras_adivinhadas.append(letra)
    
    #verifica se a letra está na palavra escolhida
    if letra in palavra_sorteada:
        lista =[]
        for indice in range(len(palavra_sorteada)): #percorre as letras da palavra
            if letra == palavra_sorteada[indice]: #verifica o indice da letra e caso foi verdadeiro, é adicionada a lista
                lista.append(letra)
            else:
                lista.append(palavras_escondida[indice]) #caso contrario, adiciona o -
        palavras_escondida=''.join(lista) # se digitou uma letra que esta na palavra, é adicionada a palavra sorteada
    
    else:
        max_tentativas -= 1
        print(f"letra não encontrada. Você tem mais {max_tentativas} tentativas")
        
    # verificação de vitoria
    if palavras_escondida == palavra_sorteada:
        print("Parabén, você ganhou")
        break
    elif max_tentativas== 0:
        print(f"Você perdeu. a palavra era {palavra_sorteada}")
        break

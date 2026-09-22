import math #importação da biblioteca
from math import pow #importação da função da biblioteca
# Fórmula do montante final: M= C*(1+i)^t  
# * = Multiplicação | + = soma | ^ = Potenciação

# Função Juros Compostos
def composto(capital, juros, tempo):
    return capital*pow((1+juros),tempo)
    # C = capital * pow((1+juros),tempo) = (1+i)^i
    
    # float porque pode ser um valor quebrado com centavos
capital = float(input("Digite o valor do Capital de investimento?\n")) 
    # float porque ser um valor com virgulas 
juros = float(input("Qual o juros anual em porcentagem(%)?\n")) 
    # meses pode ser inteiro pois não iremos adicionar dias a função
tempo = int(input("Por quantos meses será o investimento?\n")) 

juros = juros / 100  # 3% = 3/100
tempo = tempo / 12   # para transformar em anos

valor_final_composto = composto(capital, juros, tempo) #chamada da função com os valores fornecidos
print(f"O valor final será: {valor_final_composto}")

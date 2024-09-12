# -*- coding: utf-8 -*-
"""Desafio Target

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1R2p9eboz8p3HxRk4aolfSlr8pDGK5XdD
"""

#Pergunta 1

INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K = K + 1
    SOMA = SOMA + K

SOMA

#Pergunta 2

def pertence_fibonacci(numero):
    fib_a, fib_b = 0, 1

    if numero == fib_a or numero == fib_b:
        return f"O número {numero} pertence à sequência de Fibonacci."

    while fib_b < numero:
        fib_a, fib_b = fib_b, fib_a + fib_b

    if fib_b == numero:
        return f"O número {numero} pertence à sequência de Fibonacci."
    else:
        return f"O número {numero} não pertence à sequência de Fibonacci."

try:
    numero = int(input("Informe um número: "))
    print(pertence_fibonacci(numero))
except ValueError:
    print("Por favor, insira um número válido.")

#Pergunta 3

import json

# Ler o arquivo JSON
def ler_dados_json(arquivo):
    with open(arquivo, 'r') as f:
        dados = json.load(f)
    return dados

#Calcular o menor e maior faturamento e a média mensal
def calcular_faturamento(dados):
    #Checar se valor existe, se não, usa faturamento
    faturamentos = [item.get('valor', item.get('faturamento')) for item in dados if item.get('valor', item.get('faturamento', 0)) > 0]

    if not faturamentos:
        raise ValueError("Não há faturamento para calcular.")

    menor_faturamento = min(faturamentos)
    maior_faturamento = max(faturamentos)
    media_mensal = sum(faturamentos) / len(faturamentos)

    dias_acima_da_media = sum(1 for item in dados if item.get('valor', item.get('faturamento', 0)) > media_mensal)

    return menor_faturamento, maior_faturamento, dias_acima_da_media

def main():
    dados = ler_dados_json('/content/drive/MyDrive/Arquivos/dados.json')
    menor, maior, dias_acima_media = calcular_faturamento(dados)

    print(f"Menor valor de faturamento: {menor}")
    print(f"Maior valor de faturamento: {maior}")
    print(f"Número de dias com faturamento acima da média: {dias_acima_media}")

if __name__ == "__main__":
    main()

#Pergunta 4

faturamento_estados = {
    "SP": 67836.43,
    "RJ": 36678.66,
    "MG": 29229.88,
    "ES": 27165.48,
    "Outros": 19849.53
}

#Calcular o percentual de representação
def calcular_percentuais(faturamento_estados):
    total_faturamento = sum(faturamento_estados.values())

    percentuais = {}
    for estado, faturamento in faturamento_estados.items():
        percentual = (faturamento / total_faturamento) * 100
        percentuais[estado] = percentual

    return percentuais

def main():
    percentuais = calcular_percentuais(faturamento_estados)

    print("Percentual de representação por estado:")
    for estado, percentual in percentuais.items():
        print(f"{estado}: {percentual:.2f}%")

if __name__ == "__main__":
    main()

#Pergunta 5

def inverter_string(s):
    #Converter a string em lista
    lista_caracteres = list(s)
    inicio = 0
    fim = len(lista_caracteres) - 1

    #Loop para inverter os caracteres
    while inicio < fim:
        lista_caracteres[inicio], lista_caracteres[fim] = lista_caracteres[fim], lista_caracteres[inicio]
        inicio += 1
        fim -= 1

    #Converter a lista de volta para uma string
    return ''.join(lista_caracteres)

def main():
    entrada = input("Digite a string que deseja inverter: ")
    resultado = inverter_string(entrada)
    print("String invertida:", resultado)

if __name__ == "__main__":
    main()
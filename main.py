
import random

def cumprimento(texto):
    return f'Olá, {texto}'
def media_7_numeros():
    numeros = [random.randint(1, 100) for _ in range(7)]
    return numeros sum(numeros) / len(numeros)import random

if __name__ == '__main__':
    nome_completo = 'Giovanna Neves Candido'
    print(cumprimento(nome_completo))
    nums, media = media_7_numeros()
    print('numeros sorteados:', nums)
    print('media:', media)
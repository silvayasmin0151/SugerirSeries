import random
import os
lista = []


def escolha():
    try:
        res = int(input('Digite sua opção: '))
    except ValueError as err:
        print('Insira uma opção válida!')
        escolha()
    else:
        if res > 5 or res < 0:
            print('Insira uma opção válida!')
            escolha()
        else:
            if res == 5:
                sair = input('Deseja realmente sair?[S/N]')
                if sair.lower() == 's':
                    os.system('EXIT')
                else:
                    escolha()
            else:
                inserir_serie(res)


def inserir_serie(res):
    if res == 1:
        opcao = input('Digite o que você quer assistir: ')
        lista.append(opcao)
        print(opcao + ' adicionado com sucesso!')
        escolha()
    if res == 2:
        if len(lista) == 0:
            print('A lista está vazia!')
            escolha()
        else:
            print(lista)
            escolha()
    if res == 3:
        if len(lista) == 0:
            print('A lista já está vazia!')
            escolha()
        else:
            lista.clear()
            print('Lista removida com sucesso!')
            escolha()
    if res == 4:
        qtd = len(lista)
        if qtd == 0:
            print('A lista está vazia!')
            escolha()
        else:
            num = random.randrange(qtd)
            print(lista[num])
            escolha()

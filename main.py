import fsugerir
import os

def tela_menu():
      print('------------------------------------------------------')
      print('         BEM-VINDO(A)          \n')
      print('Não consegue escolher qual série ou '
            'filme assistir??')
      print('Deixe que nós decidimos por você!\n')
      print('[1] Adicione o que pretende assistir')
      print('[2] Ver lista')
      print('[3] Remover lista')
      print('[4] Sortear serie/filme')
      print('[5] Sair')
      print('------------------------------------------------------')

print('Não consegue se decidir entre o que assistir?\n'
      'esse script para indecisos vai escolher por você\n'
      'basta inserir as series ou filmes que você está em duvida na lista\n')

os.system('PAUSE')
os.system('CLS')
tela_menu()
fsugerir.escolha()

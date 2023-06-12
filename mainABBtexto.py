import os
from abb import ArvoreBinariaDeBusca

def cls():
  os.system('cls' if os.name == 'nt' else 'clear')

def ocorrencias(a, t):
    v = t.split()
    v2 = list(dict.fromkeys(v))
    for i in v2:
        print(a.frequencia(i))

def menu(a):
    while True:
        print('''
(1) Digitar texto
(2) Exibir palavras do texto Ascendente/Descendente
(3) Exibir frequencia de ocorrência das palavras
(4) Mostrar o nível de desbalanceamento da árvore
(5) Sair
    ''')
        op = int(input("Escolha uma opção: "))
        if op == 1:
            cls()
            a.esvaziar()
            t = input("Digite o texto: ")
            v = t.split()
            for i in range(len(v)):
                a.add(v[i])
        elif op == 2:
            cls()
            print('''
(a) Ascentente
(b) Descendente
            ''')
            e = input("Escolha uma opção: ")
            cls()
            if e == "a":
                a.emordem()
                print('')
            elif e == "b":
                a.desordem()
                print('')
        elif op == 3:
            cls()
            ocorrencias(a, t)
        elif op == 4:
            pass
        elif op == 5:
            cls()
            print("Programa Encerrado!")
            break
        else:
            print("Opção inválida! Tente novamente.")


a = ArvoreBinariaDeBusca()
menu(a)
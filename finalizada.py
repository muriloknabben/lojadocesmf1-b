doces = []
preco = []
volume = []
estoque = []

'''#TODO Acrescentar estoque
#TODO Ajustar '''

def valida_int(msg):
    try:
        return int(input(msg))
    except ValueError:
        print("Digite apenas números inteiros, por favor.")
        return None

def valida_float(msg):
    try:
        return float(input(msg))
    except ValueError:
        print("Digite apenas números, por favor.")
        return None

def valida_nome(nome_doce):
    if not nome_doce.replace(" ", "").isalpha():
        return " "
    else:
        return nome_doce

def menu():
    print("")
    print("--------------------------------")
    print("      Armázem Loja de Doce      ")
    print("--------------------------------")
    print("1) Cadastrar produto")
    print("2) Listar produtos cadastrados")
    print("3) Atualizar lista de produtos")
    print("4) Registrar vendas")
    print("5) Deletar produto")
    print("6) Sair") #XXX A saida como 6 pode complicar na adição de novas funções
    '''cadastrar, listar, alterar e deletar'''

def cadastrar(): #
    nome_doce = input("Digite o nome do produto que será cadastrado: ").strip().title()

    #if not nome_doce.replace(" ", "").isalpha():
    #    print(f"O nome '{nome_doce}' é inválido. Digite um nome com letras apenas!")
    #    return

    if valida_nome(nome_doce) == " ":
        print(f"O nome '{nome_doce}' é inválido. Digite um nome com letras apenas!")
        return


    try:
        preco_doce = float(input("Digite o preço do doce: "))
    except ValueError:
        print("Preço inválido! Digite apenas números")
        return

    try:
        estoque_doce = int(input("Digite quantos doces há no estoque: "))
    except ValueError:
        print("valor inválido! Digite apenas números inteiros")
        return
    estoque.append(estoque_doce)
    doces.append(nome_doce)
    preco.append(preco_doce)
    print("Produto cadastrado com sucesso!")

def listar():
    for i in range(len(doces)):
        print(f'{i + 1}) {doces[i]} - Preço: R${preco[i]:.2f} - Estoque: {estoque[i]}')

def atualizar():
    print("Essa é sua lista: ")
    listar()
    try:
        id_item = int(input("Digite o código do item que você deseja atualizar: ")) - 1
    except ValueError:
        print('Digite apenas números, por favor.')
        return
    if id_item < 0 or id_item >= len(doces):
        print('Por favor, digite um código de prduto existente.')
    else:
        desejo = input('O que você deseja alterar([n]ome, [p]reço ou [e]stoque)? ').lower()
        match(desejo):
            case 'n':
                novo_nome = input('Qual é o novo nome? ')
                if valida_nome(novo_nome) == " ":
                    print(f"O nome '{novo_nome}' é inválido. Digite um nome com letras apenas!")
                    return
                doces[id_item] = novo_nome
            case 'p':
                novo_preco = valida_float("Digite o novo preço doce: ")
                if novo_preco is None:
                    return
                preco[id_item] = novo_preco
            case 'e':
                novo_estoque = valida_int('Digite o novo estoque: ')
                if novo_estoque is None:
                    return
                estoque[id_item] = novo_estoque
            case _:
                print('Por favor digite "n" para nome, "p" para preço ou "e" para estoque')
        print('Essa é sua lista atualizada:')
        listar()

def vendas():
    listar()
    try:
        i = int(input("Digite a posição do doce que você deseja: ")) - 1
    except ValueError:
        print("Posição inválida! Digite apenas números")
        return
    if not estoque[i]:
        print("Não há estoque do item desejado")
    print(f"O doce vendido foi {doces[i]}")
    try:
        volume_doce = int(input(f"Digite quantos {doces[i]} foram vendidos: "))
    except ValueError:
        print("Quantidade inválida! Digite apenas números")
        return
    estoqnovo = estoque[i] - volume_doce
    del estoque[i]
    estoque.append(estoqnovo)
    print(f"O valor recebido foi {preco[i] * volume_doce}")


def deletar_produto():
    if not doces:
        print("Nenhum produto cadastrado.")
        return

    listar()
    try:
        e = int(input("posição do doce para deletar: ")) - 1
    except ValueError:
        print("Digite apenas números!")
        return
        '''e.isdigit() and'''
    if 0 <= int(e) < len(doces):
        i = int(e)
    elif e in doces:
        i = doces.index(e)
    else:
        print("Inválido.")
        return

    print(doces[i], "deletado.")
    del doces[i]
    del preco[i]


def sair():
    return False


def main():
    menu()
    try:
        op = int(input("Digite a opção: "))
    except ValueError:
        print("Digite apenas números!")
        return True
    match(op):
        case 1:
            cadastrar()
        case 2 | 3 | 4 | 5: 
            if not doces:
                print("Nenhum produto cadastrado ainda. Cadastre primeiro!")
            else:
                if op == 2:
                    listar()
                elif op == 3:
                    atualizar()
                elif op == 4:
                    vendas()
                elif op == 5:
                    deletar_produto()
        case 6: 
            confirmar = input("Tem certeza que deseja sair? (s/n): ").lower()
            if confirmar == "s":
                print("Saindo do sistema... Até logo!")
                return False
        case _:
            print("Digite uma das opções abaixo")
    return True

if __name__ == "__main__":
    while True:
        if not main(): 
            break
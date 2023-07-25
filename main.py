from rotas.rotas import *


mensagem = '''
    1 - Cadastrar cliente
    2 - Cadastrar ação
    3 - Realizar aálise da carteira
    4 - Imprimir relatório da carteira
    5 - Sair'''

validador_de_repeticao = True

pessoasDb = []

while validador_de_repeticao:
    print(mensagem)
    
    opçao = int(input
                ("Qual opção você deseja: "))
    
    match opçao:
        case 1:
            pessoa = cadastrar_pessoa()
            pessoasDb.append(pessoa)
            validador_de_repeticao = menu_principal()
            
        # case 2:

        # case 3:

        # case 4:

        case 5:
            print("Até a proxima!")
            break
    print(pessoasDb)
    
        

    

    

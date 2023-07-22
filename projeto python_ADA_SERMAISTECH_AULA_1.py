    
mensagem = '''
    1 - Cadastrar cliente
    2 - Cadastrar ação
    3 - Realizar aálise da carteira
    4 - Imprimir relatório da carteira
    5 - Sair'''

pessoasDb = []

def cadastrarPessoa():
    pessoa = {
                'nome' : input("Digite seu nome: "),
                'cpf' : input("Digite seu cpf: "),
                'rg' : input("Digite seu rg: "),
                'dataDeNascimento' : input("Digite sua data de nascimento: ")
            }
    pessoasDb.append(pessoa)

while True:
    print(mensagem)
    
    opçao = int(input
                ("Qual opção você deseja: "))

    match opçao:
        case 1:
            
            cadastrarPessoa()
            print('Cadastro criado com sucesso!')
            
        # case 2:

        # case 3:

        # case 4:

        case 5:
            print("Até a proxima!")
            break
    print(pessoasDb)
    
        

    

    

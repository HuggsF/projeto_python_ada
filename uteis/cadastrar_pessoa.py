
def cadastrar_pessoa():
    pessoa = {

                'nome' : input("Digite seu nome: "),
                'cpf' : input("Digite seu cpf: "),
                'rg' : input("Digite seu rg: "),
                'data_de_nascimento' : input("Digite sua data de nascimento: "),
                'cep' : input("Digite seu CEP: "),
                'numero_da_casa' : input("Digite o número de sua casa: ")
            }
    return pessoa
    
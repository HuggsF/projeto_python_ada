def menu_principal():
    continuar = True
    while continuar:
        resposta = input(('Deseja voltar ao menu principal? (sim/não)'))
        if resposta.upper() == "SIM":
            validador = True
            continuar = False
        elif resposta.upper() == "NAO":
            validador = False
            continuar = False
        else:
            print("Digite sim ou não.")        
    return validador
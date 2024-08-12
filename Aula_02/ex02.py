'''
    Crie o menu de acesso do jogo com as seguintes opções "Jogar, configurar, sair"
    Hoje a gente vai criar o configurar, de as opções ao usuario para ele configurar o jogo dele
    Nessas configurações coloque uma terceira config "dificuldade" o usuario vai poder escolher entre 1 - 3
'''

from openpyxl import Workbook, load_workbook

def config():
    
    try:
        wb = load_workbook(filename='campo.xlsx')
        config = wb['config']
    except:
        wb = Workbook()
        config = wb.create_sheet('config')
        config.cell(column=1, row=1, value="Linhas")
        config.cell(column=1, row=2, value="Colunas")
        config.cell(column=2, row=1, value="5")
        config.cell(column=2, row=2, value="5")

    linhas = config.cell(column=2, row=1).value
    colunas = config.cell(column=2, row=2).value

    wb.save('campo.xlsx')

    # print(str(linhas))
    # print(str(colunas))

    return linhas, colunas


def CriarTabuleiro(linhas, colunas):
    for i in range(0, int(linhas)):
        # for j in range(0, int(colunas)):
            # print('*', end = " ")
            # print('{:5}'.format('[ * ]'), end = " ")
        # print()
        print('[ * ] ' * int(colunas))
        print('------' * int(colunas))

def Configuracao():

    linhas = input("Digite um numero maior que 0 (linhas): \033[32m")
    print('\033[0;0m')

    while int(linhas) <= 0:
        linhas = input('digite um novo número que seja maior que zero (linhas): \033[32m')
        print('\033[0;0m')

    colunas = input("Digite um numero maior que 0 (Colunas): \033[32m")
    print('\033[0;0m')

    while int(colunas) <= 0:
        colunas = input('digite um novo número que seja maior que zero (Colunas): \033[32m')
        print('\033[0;0m')

    try:
        wb = load_workbook(filename='campo.xlsx')
        config = wb['config']
        config.cell(column=2, row=1, value=str(linhas))
        config.cell(column=2, row=2, value=str(colunas))
        wb.save('campo.xlsx')
        return 'sucesso meu patrão'
    except:
        return 'XIII deu ruim'

    
linhas, colunas = config()

print('''
    _______      ____    ,---.    ,---..-------.     ,-----.            ,---.    ,---..-./`) ,---.   .--.   ____     ______         ,-----.     
   /   __  \   .'  __ `. |    \  /    |\  _(`)_ \  .'  .-,  '.          |    \  /    |\ .-.')|    \  |  | .'  __ `. |    _ `''.   .'  .-,  '.   
  | ,_/  \__) /   '  \  \|  ,  \/  ,  || (_ o._)| / ,-.|  \ _ \         |  ,  \/  ,  |/ `-' \|  ,  \ |  |/   '  \  \| _ | ) _  \ / ,-.|  \ _ \  
,-./  )       |___|  /  ||  |\_   /|  ||  (_,_) /;  \  '_ /  | :        |  |\_   /|  | `-'`"`|  |\_ \|  ||___|  /  ||( ''_'  ) |;  \  '_ /  | : 
\  '_ '`)        _.-`   ||  _( )_/ |  ||   '-.-' |  _`,/ \ _/  |        |  _( )_/ |  | .---. |  _( )_\  |   _.-`   || . (_) `. ||  _`,/ \ _/  | 
 > (_)  )  __ .'   _    || (_ o _) |  ||   |     : (  '\_/ \   ;        | (_ o _) |  | |   | | (_ o _)  |.'   _    ||(_    ._) ': (  '\_/ \   ; 
(  .  .-'_/  )|  _( )_  ||  (_,_)  |  ||   |      \ `"/  \  ) /         |  (_,_)  |  | |   | |  (_,_)\  ||  _( )_  ||  (_.\.' /  \ `"/  \  ) /  
 `-'`-'     / \ (_ o _) /|  |      |  |/   )       '. \_/``".'          |  |      |  | |   | |  |    |  |\ (_ o _) /|       .'    '. \_/``".'   
   `._____.'   '.(_,_).' '--'      '--'`---'         '-----'            '--'      '--' '---' '--'    '--' '.(_,_).' '-----'`        '-----'     
                                                                                                                                                
''')

while True:

    print('1 - Jogar (Em desenvolvimento)')
    print('2 - Configurar (Em desenvolvimento)')
    print('3 - Sair')

    seletor = input('selecione a braba: \033[32m')
    print('\033[0;0m', end='')
    

    if seletor == '1':
        print('Jogar')

        linhas, colunas = config()
        CriarTabuleiro(linhas, colunas)

    elif seletor == '2':
        print('Configurar')
        
        teste = Configuracao()
        print(teste)

    elif seletor == '3':
        print('Saindo')
        break

    else:
        print('Opção invalida')
    

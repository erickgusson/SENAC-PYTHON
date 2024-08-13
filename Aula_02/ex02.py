from openpyxl import Workbook, load_workbook
import random

def configs():
    
    try:
        wb = load_workbook(filename='campo.xlsx')
        config = wb['config']
    except:
        wb = Workbook()
        config = wb.create_sheet('config')
        config.cell(column=1, row=1, value="Linhas")
        config.cell(column=1, row=2, value="Colunas")
        config.cell(column=1, row=3, value="Dificuldade")
        config.cell(column=2, row=1, value="5")
        config.cell(column=2, row=2, value="5")
        config.cell(column=2, row=3, value="1")

    linhas = config.cell(column=2, row=1).value
    colunas = config.cell(column=2, row=2).value
    dificuldade = config.cell(column=2, row=3).value

    wb.save('campo.xlsx')

    # print(str(linhas))
    # print(str(colunas))

    config = {
        'linhas'        : int(linhas),
        'colunas'       : int(colunas),
        'dificuldade'   : int(dificuldade)
    }

    return config

def CriarTabuleiro(linhas, colunas):
    for i in range(0, int(linhas)):
        # for j in range(0, int(colunas)):
            # print('*', end = " ")
            # print('{:5}'.format('[ * ]'), end = " ")
        # print()
        print('[ * ] ' * int(colunas))
        print('------' * int(colunas))

def ConfigCampo():

    linhas = input("Digite um numero maior que 0 (linhas): \033[32m")
    print('\033[0;0m', end='')

    while int(linhas) <= 0:
        linhas = input('digite um novo número que seja maior que zero (linhas): \033[32m')
        print('\033[0;0m', end='')

    colunas = input("Digite um numero maior que 0 (Colunas): \033[32m")
    print('\033[0;0m', end='')

    while int(colunas) <= 0:
        colunas = input('digite um novo número que seja maior que zero (Colunas): \033[32m')
        print('\033[0;0m', end='')

    dificuldade = input("\n1 - Facil\n2 - Médio\n3 - Dificil \nEscolha uma nova dificuldade: \033[32m")
    print('\033[0;0m', end='')

    while int(dificuldade) <= 0 or int(dificuldade) >= 4:
        dificuldade = input('digite um novo número de 1 e 3: \033[32m')
        print('\033[0;0m', end='')

    try:
        wb = load_workbook(filename='campo.xlsx')
        config = wb['config']

    except:
        wb = Workbook()
        config = wb.create_sheet('config')

    config.cell(column=1, row=1, value="Linhas")
    config.cell(column=1, row=2, value="Colunas")
    config.cell(column=1, row=3, value="dificuldade")
    config.cell(column=2, row=1, value=str(linhas))
    config.cell(column=2, row=2, value=str(colunas))
    config.cell(column=2, row=3, value=str(dificuldade))
    wb.save('campo.xlsx')

def CalcularBombas():
    '''
        Descubra o valor total de casas "casas" no tabuleiro e a partir desse total calcule a quantidade de bombas que vai ter no tabuleiro
        facil   -> 15%
        médio   -> 30%
        Dficil  -> 50%
    '''

    config = configs()
    totalCasas = config['linhas']  * config['colunas']

    if config['dificuldade'] == 1:
        porcentoBombas = 0.15

    if config['dificuldade'] == 2:
        porcentoBombas = 0.30

    if config['dificuldade'] == 3:
        porcentoBombas = 0.50

    totalBombas = int(float(totalCasas) * float(porcentoBombas))
    arrayzada = []

    for i in range(0, totalBombas):
        numeroAleatorio = random.randint(1, totalCasas)
        if arrayzada.count(numeroAleatorio) >= 1 :
            print('repetido')
            i = i - 1
        else:
            arrayzada.append(numeroAleatorio)
        # print('Bomba no: ' + str(arrayzada[i]))

    arrayzada.sort()
    for i in range(0, len(arrayzada)):
        print('Bomba no: ' + str(arrayzada[i]))

    print(totalBombas)
    print
    input()

CalcularBombas()
config = configs()
print('''\
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
        config = configs()
        CriarTabuleiro(config['linhas'], config['colunas'])

    elif seletor == '2':
        print('Configurar')
        ConfigCampo()

    elif seletor == '3':
        print('Saindo')
        break

    else:
        print('Opção invalida')
    

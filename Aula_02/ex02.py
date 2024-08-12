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
        print('[ * ] ' * int(colunas))
        # print()
        print('------' * int(colunas))


linhas, colunas = config()


while True:

    seletor = input('selecione a braba: \033[32m')
    print('\033[0;0m', end='')

    if seletor == '1':
        print('Jogar')
        CriarTabuleiro(linhas, colunas)
    elif seletor == '2':
        print('Configurar')
    elif seletor == '3':
        print('Saindo')
        break
    else:
        print('Opção invalida')
    






import PySimpleGUI as sg
import criptografar as cp

# Layout da janela
def janela_opcao():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Opção', size=(6, 1)), sg.Combo(['Criptografar', 'Descriptografar'], size=(
            16, 1), default_value='Criptografar', key='opcao')],
        [sg.Button('Próximo')]
    ]
    return sg.Window('Selecionar opção', layout=layout, finalize=True)

# Layout da janela
def janela_cripto():
    sg.theme('DarkBlue')
    layout_l = [
        [sg.Text('Mensagem:')], 
        [sg.Multiline(key='mensagem1', size=(20, 5))]
    ]
    layout_r = [
        [sg.Text('Mensagem Criptografada:')],
        [sg.Output(size=(20, 5))],
    ]

    layout = [
        [sg.T('Criptografar', font='_ 18', justification='c', expand_x=True)],
        [sg.HSep()],
        [sg.Col(layout_l), sg.Col(layout_r)],
        [sg.Button('Voltar'), sg.Button('Criptografar')]
    ]
    return sg.Window('Criptografar', layout=layout, finalize=True)

# Layout da janela
def janela_descripto():
    sg.theme('DarkBlue')
    layout_l = [
        [sg.Text('Mensagem Criptografada:')],
        [sg.Multiline(key='mensagem2', size=(20, 5))]
    ]

    layout_r = [
        [sg.Text('Mensagem Descriptografada:')],
        [sg.Output(size=(20, 5))]
    ]

    layout = [
        [sg.T('Descriptografar', font='_ 18', justification='c', expand_x=True)],
        [sg.HSep()],
        [sg.Col(layout_l), sg.Col(layout_r)],
        [sg.Button('Voltar'), sg.Button('Descriptografar')]
    ]
    return sg.Window('Descriptografar', layout=layout, finalize=True)

# Abrindo a janela
janela1, janela2, janela3 = janela_opcao(), None, None

# Rodando as janelas infinitamente
while True:
    window, event, values = sg.read_all_windows()
    # Quando a janela for fechada
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela3 and event == sg.WINDOW_CLOSED:
        break
    # Escolhendo a próxima janela
    if window == janela1 and event == 'Próximo':
        if values['opcao'] == 'Criptografar':
            janela2 = janela_cripto()
        else:
            janela3 = janela_descripto()
        janela1.close()
    # Voltando para janela principal
    if window == janela2 and event == 'Voltar':
        janela2.close()
        janela1 = janela_opcao()
    if window == janela3 and event == 'Voltar':
        janela3.close()
        janela1 = janela_opcao()
    # Evento dos botões
    if window == janela2 and event == 'Criptografar':
        frase = values['mensagem1']
        print(cp.cripto(frase))
    if window == janela3 and event == 'Descriptografar':
        frase = values['mensagem2']
        print(cp.descripto(frase))

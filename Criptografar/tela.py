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
    layout = [
        [sg.Text('Criptografar')],
        [sg.HSep()],
        [sg.Text('Mensagem:')], 
        [sg.Multiline(key='mensagem1', size=(20, 5))],
        [sg.Text('Mensagem Criptografada:')],
        [sg.Output(size=(20, 5))],
        [sg.Button('Voltar'), sg.Button('Criptografar')]
    ]
    return sg.Window('Criptografar', layout=layout, finalize=True)

# Layout da janela
def janela_descripto():
    sg.theme('DarkBlue')
    layout = [
        [sg.Text('Descriptografar')],
        [sg.HSep()],
        [sg.Text('Mensagem Criptografada:')],
        [sg.Multiline(key='mensagem2', size=(20, 5))],
        [sg.Text('Mensagem Descriptografada:')],
        [sg.Output(size=(20, 5))],
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
        janela1.hide()
    # Voltando para janela principal
    if window == janela2 and event == 'Voltar':
        janela2.hide()
        janela1.un_hide()
    if window == janela3 and event == 'Voltar':
        janela3.hide()
        janela1.un_hide()
    # Evento dos botões
    if window == janela2 and event == 'Criptografar':
        frase = values['mensagem1']
        print(cp.cripto(frase))
    if window == janela3 and event == 'Descriptografar':
        frase = values['mensagem2']
        print(cp.descripto(frase))

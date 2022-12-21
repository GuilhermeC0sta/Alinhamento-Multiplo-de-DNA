#######################################################################
# Necessaria a instalacao do PySimpleGUI (pip install pysimplegui)
# Este é o arquivo principal

import PySimpleGUI as sg
from alinhamento_func import alinhamento
from background_tk import background

def janela_login():
    layout = [
        [sg.Text("Quantas sequências pretende alinhar ?")],
        [sg.Input(key='numseq')],
        [sg.Button("Continuar")]   
    ]
    return sg.Window("Início", layout=layout, finalize=True)

def janela_print(texto):
    layout = [
        [sg.Text("Alinhamentos:")],
        [sg.Print(texto, background_color='red')],
        [sg.Button("Continuar")]   
    ]
    return sg.Window("Alinhamento Múltiplo de DNA", layout=layout, finalize=True)    

def janela_seq2():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)

def janela_seq3():
    layout = [[sg.Text('Preencha com as sequências desejadas:')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    

def janela_seq4():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Input(key='seq4')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    

def janela_seq5():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Input(key='seq4')],
        [sg.Input(key='seq5')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    

def janela_seq6():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Input(key='seq4')],
        [sg.Input(key='seq5')],
        [sg.Input(key='seq6')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    

def janela_seq7():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Input(key='seq4')],
        [sg.Input(key='seq5')],
        [sg.Input(key='seq6')],
        [sg.Input(key='seq7')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    

def janela_seq8():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Input(key='seq4')],
        [sg.Input(key='seq5')],
        [sg.Input(key='seq6')],
        [sg.Input(key='seq7')],
        [sg.Input(key='seq8')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    

def janela_seq9():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Input(key='seq4')],
        [sg.Input(key='seq5')],
        [sg.Input(key='seq6')],
        [sg.Input(key='seq7')],
        [sg.Input(key='seq8')],
        [sg.Input(key='seq9')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    

def janela_seq10():
    layout = [[sg.Text('Preencha com as sequências desejadas:'), sg.Text(size=(15,1), key='-OUTPUT-')],
        [sg.Input(key='seq1')],
        [sg.Input(key='seq2')],
        [sg.Input(key='seq3')],
        [sg.Input(key='seq4')],
        [sg.Input(key='seq5')],
        [sg.Input(key='seq6')],
        [sg.Input(key='seq7')],
        [sg.Input(key='seq8')],
        [sg.Input(key='seq9')],
        [sg.Input(key='seq10')],
        [sg.Button('Voltar'), sg.Button('Alinhar')]
    ]
    return sg.Window("Sequências", layout=layout, finalize=True)    


janela1, janela2, janela3 = janela_login(), None, None
while True:
    window, event, values = sg.read_all_windows()
    if window == janela1 and event == sg.WINDOW_CLOSED:
        break
    if window == janela2 and event == sg.WINDOW_CLOSED:
        break
    if window == janela1 and event == "Continuar":
        numseq = int(values['numseq'])
        if numseq == 2:
            janela2 = janela_seq2()
        elif numseq == 3:
            janela2 = janela_seq3()
        elif numseq == 4:
            janela2 = janela_seq4()
        elif numseq == 5:
            janela2 = janela_seq5()
        elif numseq == 6:
            janela2 = janela_seq6()
        elif numseq == 7:
            janela2 = janela_seq7()
        elif numseq == 8:
            janela2 = janela_seq8()
        elif numseq == 9:
            janela2 = janela_seq9()
        elif numseq == 10:
            janela2 = janela_seq10()
        janela1.hide()
    if window == janela2 and event == "Voltar":
        janela2.hide()
        janela1.un_hide()
    if window == janela2 and event == "Alinhar":
        sequencias_entrada = []
        for i in range(numseq):
            sequencias_entrada.append(values['seq'+str(i+1)])  
        seqt = alinhamento(sequencias_entrada, numseq)
        janela2.hide()        
        background(seqt, numseq)

window.close()

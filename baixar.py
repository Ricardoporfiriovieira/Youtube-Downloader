from PySimpleGUI.PySimpleGUI import read_all_windows
from pytube import YouTube, streams
from os import path, rename
from PySimpleGUI import Text, Input, Button, Checkbox, Window, theme, WINDOW_CLOSED, one_line_progress_meter

def janela1():
    theme('DarkAmber')
    tela = [
    [Text('Coloque aqui a url do vídeo: ')],
    [Input(key='input')],
    [Button('Continuar'), Button('Sair')],
    ]

    return Window('Youtube Downloader', layout=tela, finalize=True)

def janela2():
    theme('DarkAmber')
    tela = [
        [Text(key='mostra_titulo')],
        [Text('Escolha o Formato do seu Download.')],
        [Checkbox('Mp4', key='mp4'), Checkbox('Mp3', key='mp3')],
        [Button('Download'), Button('Voltar')]
    ]

    return Window('Youtube Downloader', layout=tela, finalize=True)

jn1, jn2 = janela1(), None

while True:
    window, event, values = read_all_windows()
    if event == WINDOW_CLOSED or event == 'Sair':
        break
    if window == jn1 and event == 'Continuar':
        link = values['input']
        jn2 = janela2()
        mostrarTitulo = YouTube(link)
        jn1.hide()
        window = jn2
        window['mostra_titulo'].update(mostrarTitulo.title)
    if window == jn2 and event == 'Voltar':
        jn1 = janela1()
        jn2.hide()
    if event == 'Download': 
        if values['mp4'] == True:
            yt = YouTube(link)
            video = yt.streams.get_highest_resolution()
            som = video.download()
            nome, ext = path.splitext(som)
            novo_som = nome + '_video' + '.mp4'
            rename(som, novo_som)
            for i in range(1000):  
                if not one_line_progress_meter('Download...', i + 1, 1000, 'Executando o Seu Download...', i*300, orientation='h'):
                    break

        if values['mp3'] == True:
            yt = YouTube(link)
            audio = yt.streams.filter(only_audio=True).first()
            som = audio.download()
            print(som)
            nome, ext = path.splitext(som)
            novo_som = nome + '.mp3'
            rename(som, novo_som)
            for i in range(1000):  
                if not one_line_progress_meter('Download...', i + 1, 1000, 'Executando o Seu Download...', i*300, orientation='h'):
                    break
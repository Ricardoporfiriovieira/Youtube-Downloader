from PySimpleGUI.PySimpleGUI import Popup, read_all_windows
from pytube import YouTube, Playlist
from pytube.exceptions import RegexMatchError, AgeRestrictedError
from pytube import request
from os import path, rename
from PySimpleGUI import Text, Input, Button, Checkbox, Window, theme, WINDOW_CLOSED, one_line_progress_meter, popup

def progress_callback(stream, chunk, bytes_remaining):

    try:

        size = video.filesize
        progress = int(((size - bytes_remaining) / size) * 100)
        theme('DarkAmber')
        if not one_line_progress_meter('Youtube Installer', progress, 100, (f'Executando o seu download...'), orientation='h', size=(20,20)):
            Popup('Fechando o Porgrama...')
            exit()
            

    except NameError:

        size = video_baixar.filesize
        progress = int(((size - bytes_remaining) / size) * 100)
        theme('DarkAmber')
        if not one_line_progress_meter('Executando o seu Download', progress, 100, (f'Executando o {c}º download de {len(p.video_urls)} arquivos'), orientation='h', size=(20,20)):
            Popup('Fechando o Porgrama...')
            exit()



def complete_callback(stream, file_handle):

    try:

        layout = [[Text(f'Seu {c}º Download de {len(p.video_urls)} foi Concluido com sucesso')],
              [Text('Aperte no Botão "Cancelar" para Cancelar o Download.')],
              [Button('Continuar'), Button('Cancelar')]]

        window = Window('Window Title', layout, enable_close_attempted_event=True, auto_close=True, auto_close_duration=2)

        event, values = window.read()
        if event == 'Cancelar':
            exit()
    except NameError:

        layout = [[Text(f'Seu Download foi Concluido com sucesso!')],
              [Button('Ok')]]
        window = Window('Window Title', layout, enable_close_attempted_event=True, auto_close=True, auto_close_duration=2)

        event, values = window.read()



def janela1():

    theme('DarkAmber')
    tela = [
    [Text('Coloque aqui a url do vídeo: ')],
    [Input(key='input')],
    [Button('Continuar'), Button('Sair')]
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
    print(event, 'read')

    if event == WINDOW_CLOSED or event == 'Sair':
        break

    if window == jn1 and event == 'Continuar':

        link = values['input']
        jn2 = janela2()
        jn1.hide()
        window = jn2

        try:

            mostrarTitulo = YouTube(link)
            window['mostra_titulo'].update(mostrarTitulo.title)

        except RegexMatchError:

            c = 0
            lista = []
            p = Playlist(link)
            window['mostra_titulo'].update(f'Deseja fazer o Download de uma Playlist com {len(p.video_urls)} arquivos?')

    if window == jn2 and event == 'Voltar':

        jn1 = janela1()
        jn2.hide()

    if event == 'Download': 

        if values['mp4'] == True:

            try:

                request.default_range_size = 1048576  
                yt_video = YouTube(link)
                video = yt_video.streams.get_highest_resolution()
                yt_video.register_on_complete_callback(complete_callback)
                yt_video.register_on_progress_callback(progress_callback)
                som = video.download()
                nome, ext = path.splitext(som)
                novo_som = nome + '_video' + '.mp4'
                rename(som, novo_som)

            except RegexMatchError:

                request.default_range_size = 1048576  
                p = Playlist(link)

                for url in p.video_urls:

                    try:

                        c += 1
                        video_playlist = YouTube(url)
                        lista.append(video_playlist.title) 
                        video_baixar = video_playlist.streams.get_highest_resolution()
                        video_playlist.register_on_complete_callback(complete_callback)
                        video_playlist.register_on_progress_callback(progress_callback) 
                        video_baixar.download()
                        
                    except AgeRestrictedError:

                        popup('Esse vídeo tem restrição de idade porfavor tente outra url.',auto_close=True ,auto_close_duration=2)
                        pass


        if values['mp3'] == True:

            try:

                yt = YouTube(link)
                audio = yt.streams.filter(only_audio=True).first()
                yt.register_on_complete_callback(complete_callback)
                yt.register_on_progress_callback(progress_callback)
                som = audio.download()
                print(som)
                nome, ext = path.splitext(som)
                novo_som = nome + '.mp3'
                rename(som, novo_som)

            except RegexMatchError:

                request.default_range_size = 1048576  
                p_music = Playlist(link)

                for url in p_music.video_urls:

                    try:

                        c += 1
                        yt_playlist = YouTube(url)
                        video_baixar = yt_playlist.streams.filter(only_audio=True).first()
                        yt_playlist.register_on_complete_callback(complete_callback)
                        yt_playlist.register_on_progress_callback(progress_callback)
                        som_playlist = video_baixar.download()
                        print(som_playlist)
                        nome, ext = path.splitext(som_playlist)
                        novo_som = nome + '.mp3'
                        rename(som_playlist, novo_som)

                    except AgeRestrictedError:

                        popup('Esse vídeo tem restrição de idade porfavor tente outra url.',auto_close=True ,auto_close_duration=2)
                        pass

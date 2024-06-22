from PySimpleGUI import (
    read_all_windows, 
    Popup, 
    Text, 
    Input, 
    Button, 
    Checkbox, 
    Window, 
    theme, 
    WINDOW_CLOSED, 
    one_line_progress_meter, 
    popup
)
from pytube import YouTube, Playlist, request
from pytube.exceptions import RegexMatchError, AgeRestrictedError
from os import path, rename


def progress_callback(stream, chunk, bytes_remaining):
    size = stream.filesize
    progress = int(((size - bytes_remaining) / size) * 100)
    if not one_line_progress_meter('Youtube Installer', progress, 100, 'Executando o seu download...', orientation='h', size=(20, 20)):
        Popup('Fechando o Programa...')
        exit()


def complete_callback(stream, file_handle):
    layout = [[Text(f'Seu download foi concluído com sucesso!')],
              [Button('Ok')]]
    window = Window('Download Completo', layout, auto_close=True, auto_close_duration=2)
    event, _ = window.read()
    if event == WINDOW_CLOSED:
        window.close()


def download_video(link, is_playlist, format):
    if is_playlist:
        p = Playlist(link)
        for idx, url in enumerate(p.video_urls, start=1):
            download_single_video(url, format, idx, len(p.video_urls))
    else:
        download_single_video(link, format)


def download_single_video(link, format, current_index=1, total_files=1):
    yt = YouTube(link)
    if format == 'mp4':
        video = yt.streams.get_highest_resolution()
        yt.register_on_complete_callback(complete_callback)
        yt.register_on_progress_callback(progress_callback)
        file_path = video.download()
        rename(file_path, path.splitext(file_path)[0] + '_video.mp4')
    elif format == 'mp3':
        audio = yt.streams.filter(only_audio=True).first()
        yt.register_on_complete_callback(complete_callback)
        yt.register_on_progress_callback(progress_callback)
        file_path = audio.download()
        rename(file_path, path.splitext(file_path)[0] + '.mp3')


def create_main_window():
    theme('DarkAmber')
    layout = [
        [Text('Coloque aqui a URL do vídeo:')],
        [Input(key='input')],
        [Button('Continuar'), Button('Sair')]
    ]
    return Window('Youtube Downloader', layout=layout, finalize=True)


def create_format_window(title):
    theme('DarkAmber')
    layout = [
        [Text(title, key='mostra_titulo')],
        [Text('Escolha o formato do seu download:')],
        [Checkbox('Mp4', key='mp4'), Checkbox('Mp3', key='mp3')],
        [Button('Download'), Button('Voltar')]
    ]
    return Window('Youtube Downloader', layout=layout, finalize=True)


jn1, jn2 = create_main_window(), None

while True:
    window, event, values = read_all_windows()

    if event in (WINDOW_CLOSED, 'Sair'):
        break

    if window == jn1 and event == 'Continuar':
        link = values['input']
        try:
            yt = YouTube(link)
            title = yt.title
            is_playlist = False
        except RegexMatchError:
            p = Playlist(link)
            title = f'Deseja fazer o download de uma playlist com {len(p.video_urls)} arquivos?'
            is_playlist = True

        jn2 = create_format_window(title)
        jn1.hide()

    if window == jn2 and event == 'Voltar':
        jn2.hide()
        jn1.un_hide()

    if window == jn2 and event == 'Download':
        format = 'mp4' if values['mp4'] else 'mp3'
        download_video(link, is_playlist, format)

window.close()

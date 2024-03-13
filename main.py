import flet as ft
import os
import gettext
import time
from ytmusicapi import YTMusic
files = []
oauth = ""
status = bool

if not os.path.exists("browser.json"):
    ytmusic = YTMusic()
    oauth = "されていません"
    status = False
else:
    ytmusic = YTMusic("browser.json")
    oauth = "されています"
    status = True

def main(page:ft.Page):
    page.title = "YouTubeMusic Uploader"
    page.window_center()
    page.padding = 24

    def clear_files(e):
        global files
        files.clear()
        selected_files.value = "\n".join(files)
        selected_files.update()

    def sel_files(e:ft.FilePickerResultEvent):
        global files
        if e.files:
            for f in e.files:
                files.append(f.path)
        else:
            pass
        selected_files.value = "\n".join(files)
        selected_files.update()
    
    pick_files_dialog = ft.FilePicker(on_result=sel_files)
    selected_files = ft.TextField(value="",multiline=True,max_lines=10,min_lines=10,expand=True,label="アップロードするファイル",prefix_icon=ft.icons.AUDIO_FILE)
    page.overlay.extend([pick_files_dialog])

    def upload(e):
        if status == False:
            progress_text.value = "アカウントにログインしていないため、アップロードできません"
            progress_text.update()
        else:
            if len(files) != 0:
                upload_btn.disabled = True
                upload_btn.update()
                done = 0
                for file_path in files:
                    file_name = os.path.basename(file_path)
                    done += 1
                    progress_text.value = f"{file_name}をアップロードしています... ( {done}/{len(files)} )"
                    progress_text.update()
                    progress = done / len(files)
                    progress_bar.value = progress
                    progress_bar.update()
                    ytmusic.upload_song(file_path)
                    time.sleep(0)
                    

                progress_text.value = "アップロードが完了しました"
                progress_text.update()
                upload_btn.disabled = False
                upload_btn.update()
                if after_clear.value == True:
                    files.clear()
                    selected_files.value = "\n".join(files)
                    selected_files.update()
                else:
                    pass
            
            else:
                progress_text.value = "ファイルが選択されていません"
                progress_text.update()

    oauth_text = ft.Text(value=f"アカウントにログイン{oauth}")
    progress_text = ft.Text("待機しています。")
    progress_bar = ft.ProgressBar(value=0)

    after_clear = ft.Checkbox(label="アップロード後にリストをクリア")

    clear_btn = ft.TextButton("クリア",on_click=clear_files,icon=ft.icons.CLEAR)

    upload_btn = ft.FloatingActionButton("アップロード",icon=ft.icons.UPLOAD,on_click=upload)

    open_files_dialog = ft.TextButton("ファイルを追加",icon=ft.icons.ADD,on_click=lambda _: pick_files_dialog.pick_files(allow_multiple=True,allowed_extensions=["mp3","flac","m4a","ogg","wma"]))

    page.add(ft.Row([selected_files,ft.Column([open_files_dialog,clear_btn])]),after_clear,oauth_text,progress_text,progress_bar,upload_btn)

if __name__ == "__main__":
    ft.app(main)
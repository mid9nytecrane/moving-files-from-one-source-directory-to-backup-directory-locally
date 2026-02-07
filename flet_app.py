import flet as ft
import os
import shutil
import datetime

def organize_files(src_path, dst_path, log_callback=None):
    if not os.path.exists(src_path):
        if log_callback: log_callback(f"Source path {src_path} does not exist.")
        return
    if not os.path.exists(dst_path):
        try:
            os.makedirs(dst_path)
            if log_callback: log_callback(f"Created destination directory {dst_path}")
        except Exception as e:
            if log_callback: log_callback(f"Error creating destination directory: {str(e)}")
            return

    try:
        files = os.listdir(src_path)
    except Exception as e:
        if log_callback: log_callback(f"Error listing source directory: {str(e)}")
        return

    mapping = {
        '.png': 'image', '.jpeg': 'image', '.jpg': 'image', '.JPG': 'image', '.svg': 'image', '.gif': 'image', '.jpe': 'image',
        '.pdf': 'pdf_files',
        '.mp3': 'audio', '.wav': 'audio',
        '.mp4': 'videos', '.mkv': 'videos',
        '.txt': 'textfolder'
    }

    for file in files:
        src_file_path = os.path.join(src_path, file)
        if os.path.isdir(src_file_path):
            continue

        _, ext = os.path.splitext(file)
        folder_name = mapping.get(ext.lower(), 'others')

        target_folder = os.path.join(dst_path, folder_name)
        if not os.path.exists(target_folder):
            try:
                os.makedirs(target_folder)
            except Exception as e:
                if log_callback: log_callback(f"Error creating folder {folder_name}: {str(e)}")
                continue

        dst_file_path = os.path.join(target_folder, file)

        try:
            if os.path.exists(dst_file_path):
                if log_callback: log_callback(f"Skipping {file}, already exists in {folder_name}")
            else:
                shutil.move(src_file_path, dst_file_path)
                if log_callback: log_callback(f"Moved {file} to {folder_name}")
        except Exception as e:
            if log_callback: log_callback(f"Error moving {file}: {str(e)}")

def main(page: ft.Page):
    page.title = "File Organizer"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    src_dir = ft.TextField(label="Source Directory", expand=True)
    dst_dir = ft.TextField(label="Destination Directory", expand=True)

    log_area = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

    def log(message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        log_area.controls.append(ft.Text(f"[{now}] {message}"))
        page.update()

    def start_organizing(e):
        if not src_dir.value or not dst_dir.value:
            log("Please provide both source and destination directories.")
            return

        log(f"Starting organization from {src_dir.value} to {dst_dir.value}...")
        organize_files(src_dir.value, dst_dir.value, log)
        log("Finished organization.")

    page.add(
        ft.Column([
            ft.Text("File Organizer", size=30, weight=ft.FontWeight.BOLD),
            ft.Row([src_dir]),
            ft.Row([dst_dir]),
            ft.Button("Start Organizing", on_click=start_organizing),
            ft.Text("Logs:", size=20, weight=ft.FontWeight.BOLD),
            ft.Container(
                content=log_area,
                border=ft.border.all(1, ft.Colors.OUTLINE),
                border_radius=5,
                height=300,
            )
        ], expand=True)
    )

if __name__ == "__main__":
    ft.run(main)

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
    page.title = "Neumorphic File Organizer"
    page.bgcolor = "#EDEDED"
    page.padding = 40
    page.theme_mode = ft.ThemeMode.LIGHT

    # Neumorphic styling constants
    BG_COLOR = "#EDEDED"
    LIGHT_SHADOW = "#FFFFFF"
    DARK_SHADOW = "#B0B0B0"

    neumorphic_shadow = [
        ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=DARK_SHADOW,
            offset=ft.Offset(5, 5),
        ),
        ft.BoxShadow(
            spread_radius=1,
            blur_radius=10,
            color=LIGHT_SHADOW,
            offset=ft.Offset(-5, -5),
        ),
    ]

    src_dir_input = ft.TextField(
        label="Source Directory",
        border=ft.InputBorder.NONE,
        expand=True,
        hint_text="Enter source path...",
        content_padding=15,
    )

    dst_dir_input = ft.TextField(
        label="Destination Directory",
        border=ft.InputBorder.NONE,
        expand=True,
        hint_text="Enter destination path...",
        content_padding=15,
    )

    log_area = ft.ListView(expand=True, spacing=5, padding=10, auto_scroll=True)

    def log(message):
        now = datetime.datetime.now().strftime("%H:%M:%S")
        log_area.controls.append(ft.Text(f"[{now}] {message}", color=ft.Colors.BLACK54))
        page.update()

    def start_organizing(e):
        if not src_dir_input.value or not dst_dir_input.value:
            log("Please provide both source and destination directories.")
            return

        log(f"Starting organization from {src_dir_input.value} to {dst_dir_input.value}...")
        organize_files(src_dir_input.value, dst_dir_input.value, log)
        log("Finished organization.")

    page.add(
        ft.Column([
            ft.Text("File Organizer", size=40, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
            ft.Container(height=20),

            ft.Container(
                content=src_dir_input,
                bgcolor=BG_COLOR,
                border_radius=15,
                shadow=neumorphic_shadow,
                padding=ft.Padding.symmetric(horizontal=10),
            ),

            ft.Container(height=20),

            ft.Container(
                content=dst_dir_input,
                bgcolor=BG_COLOR,
                border_radius=15,
                shadow=neumorphic_shadow,
                padding=ft.Padding.symmetric(horizontal=10),
            ),

            ft.Container(height=30),

            ft.Container(
                content=ft.TextButton(
                    content=ft.Text("Start Organizing", size=18, weight=ft.FontWeight.W_600),
                    on_click=start_organizing,
                    style=ft.ButtonStyle(color=ft.Colors.BLUE_600),
                ),
                bgcolor=BG_COLOR,
                border_radius=15,
                shadow=neumorphic_shadow,
                alignment=ft.Alignment(0, 0),
                width=200,
                height=50,
            ),

            ft.Container(height=40),

            ft.Text("Logs:", size=22, weight=ft.FontWeight.BOLD, color=ft.Colors.BLACK87),
            ft.Container(
                content=log_area,
                bgcolor=BG_COLOR,
                border_radius=15,
                shadow=neumorphic_shadow,
                height=300,
                expand=True,
                padding=10,
            )
        ], scroll=ft.ScrollMode.AUTO, expand=True)
    )

if __name__ == "__main__":
    ft.run(main, view=ft.AppView.WEB_BROWSER, port=8550)

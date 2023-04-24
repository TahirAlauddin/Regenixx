from qt_core import *
from utils import *
from core.json_themes import Themes
from widgets.py_push_button import PyPushButton
import requests
import time
import os
import json
import zipfile


class DownloadWindow(QMainWindow):
    pause = False
    downloaded = False

    def __init__(self):
        super().__init__()
        self.setWindowTitle('File Downloader')
        self.setFixedSize(500, 200)

        self.themes = Themes().items

        widget = QWidget()
        layout = QVBoxLayout(widget)
        self.setCentralWidget(widget)

        frame = QFrame()
        horizontalLayout = QHBoxLayout(frame)

        set_stylesheet(widget, widgetStyle, 
            bg_color = "#2c313c",
            text_color = "#fff",
            text_font = "9pt 'Manrope'",
            border_radius = 0,
            border_size = 2,
            border_color = "transparent")

        # Title/Heading
        self.title = QLabel("Downloading Updates")
        set_stylesheet(self.title, labelStyle, 
                       color=self.themes["app_color"]["context_color"],
                       bg_color='transparent'
        )
        layout.addWidget(self.title)

        # Create progress bar
        self.progress_bar = QProgressBar()
        set_stylesheet(self.progress_bar, progressBarStyles, radius=10,
                       bg_color=self.themes['app_color']['bg_one'],
                       color=self.themes['app_color']['bg_three'],
                       gradient_color_start=self.themes['app_color']['context_color'],
                       gradient_color_stop=self.themes['app_color']['context_pressed'],
                       )
        x = self.progress_bar.styleSheet()
        layout.addWidget(self.progress_bar)

        # Pause download button
        pause_button = PyPushButton(text='Pause',
                        radius=8,
                        color='#FFF',
                        bg_color=self.themes["app_color"]["bg_one"],
                        bg_color_hover=self.themes["app_color"]["dark_three"],
                        bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        pause_button.clicked.connect(self.pause_download)
        pause_button.setFixedSize(QSize(150, 40))
        horizontalLayout.addWidget(pause_button)

        # Resume download button
        resume_button = PyPushButton(text='Resume', radius=8,
            color='#FFF',
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        resume_button.clicked.connect(self.resume_download)
        resume_button.setFixedSize(QSize(150, 40))
        horizontalLayout.addWidget(resume_button)

        # Cancel button
        cancel_button = PyPushButton(text='Cancel', radius=8,
            color='#FFF',
            bg_color=self.themes["app_color"]["bg_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        cancel_button.clicked.connect(self.cancel_download)
        cancel_button.setFixedSize(QSize(150, 40))
        horizontalLayout.addWidget(cancel_button)

        layout.addWidget(frame)
        frame.setLayout(horizontalLayout)

        self.start_download()
        

    def pause_download(self):
        self.pause = True

    def resume_download(self):
        self.pause = False
        

    def start_download(self):
        # Set the URL of the file you want to download

        # Start the download in a separate thread
        self.download_thread = DownloadThread(url, window=self)
        self.download_thread.progress.connect(self.update_progress)
        self.download_thread.start()


    def update_progress(self, progress):
        # Update the progress bar with the download progress
        self.progress_bar.setValue(progress)
        if progress == 100:
            if self.downloaded:
                # Close window, installation successful                
                result = self.showSuccessfullyUpdatedInfoMessage()
                if result == QMessageBox.Ok:
                    self.close()
                return
            
            self.progress_bar.setValue(0)
            self.downloaded = True
            self.installation_thread = InstallationThread(url, self)
            self.title.setText("Installing Updates")
            self.installation_thread.progress.connect(self.update_progress)
            self.installation_thread.start()


    def showSuccessfullyUpdatedInfoMessage(self, window_title=None, text=None, buttons=None):
        if not text:
            text = "Update Installed successfully! You may close the window now."
        if not window_title:
            window_title = "Updated Success!"
        if not buttons:
            buttons = [QMessageBox.Ok]

        messageBox = QMessageBox(self)
        messageBox.setWindowTitle(window_title)
        messageBox.setText(text)
        messageBox.setIcon(QMessageBox.Information)
        # Add some custom styles to the QMessageBox
        messageBox.setStyleSheet(messageBoxStyle)
        
        # Add a button to the QMessageBox and show it
        for button in buttons:
            messageBox.addButton(button)

        return messageBox.exec()


    def cancel_download(self):
        # Cancel the download in the download thread
        if hasattr(self, 'download_thread'):
            messageBox = self.showSuccessfullyUpdatedInfoMessage("Confirmation", "Are you sure you want to cancel this operation?", 
                                                    [QMessageBox.Yes, QMessageBox.No])
            if messageBox == QMessageBox.Yes:
                self.download_thread.cancel()
                

class DownloadThread(QThread):
    progress = Signal(int)

    def __init__(self, url, window):
        super().__init__()
        self.url = url
        self.window = window

    def run(self):
        # Get filename from the url
        self.output_filename = url.split('amazonaws.com/')[1].split('?')[0]
        # Send a GET request to the URL and stream the download
        response = requests.get(self.url, stream=True)

        # Get the total file size in bytes
        total_size = int(response.headers.get('content-length', 0))

        # Define a chunk size for streaming the download in parts
        chunk_size = 1024  # 1 KB

        # Initialize the progress variables
        downloaded_size = 0
        progress = 0

        with open(self.output_filename, 'wb') as video_file:
            # Start downloading the file in chunks
            for chunk in response.iter_content(chunk_size=chunk_size):
                # Check if the download is cancelled
                if self.isInterruptionRequested():
                    break

                if self.window.pause:
                    while self.window.pause:
                        time.sleep(0.1)

                # Write the chunk to a file (or do something with the data)
                video_file.write(chunk)

                # Update the downloaded size and progress
                downloaded_size += len(chunk)
                progress = (downloaded_size / total_size) * 100

                # Emit the progress signal
                self.progress.emit(progress)


    def cancel(self):
        # Request interruption of the download thread
        self.requestInterruption()


class InstallationThread(QThread):
    progress = Signal(int)

    def __init__(self, url, window):
        super().__init__()

        self.output_filename = url.split('amazonaws.com/')[1].split('?')[0]
        self.window = window


    def unzip_file_in_chunks(self, zip_file_path, destination_folder, chunk_size=1024*1024):
        # Initialize the progress variables
        installed_size = 0
        progress = 0
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            #? Total size for a zip file must be found this way, not using os.path.getsize
            #? This is the uncompressed size of the zipfile.
            total_size = sum(info.file_size for info in zip_ref.infolist())

            for zipped_file_info in zip_ref.infolist():
                # Ensure the nested directory structure is created
                file_destination_path = os.path.join(destination_folder, zipped_file_info.filename)
                if zipped_file_info.is_dir():
                    os.makedirs(file_destination_path, exist_ok=True)
                    continue

                with zip_ref.open(zipped_file_info, 'r') as zipped_file:
                    
                    with open(file_destination_path, 'wb') as output_file:
                        while True:
                            chunk = zipped_file.read(chunk_size)
                            if not chunk:
                                break
                            
                            # Check if the download is cancelled
                            if self.isInterruptionRequested():
                                break

                            if self.window.pause:
                                while self.window.pause:
                                    time.sleep(0.1)

                            # Write the chunk to a file (or do something with the data)
                            output_file.write(chunk)

                            # Update the downloaded size and progress
                            installed_size += len(chunk)
                            progress = (installed_size / total_size) * 100
                            # Emit the progress signal
                            self.progress.emit(progress)


    def run(self):
        self.unzip_file_in_chunks(self.output_filename, os.path.abspath('.'), chunk_size=1024)
        
        # with open('version.json', 'r') as inputJson:
        #     object = json.load(inputJson)
        #     object['version'] = self.output_filename.strip('regenixx-').strip('.zip')
        # with open('version.json', 'w') as outputJson:
        #     json.dump(object, outputJson)



    def cancel(self):
        # Request interruption of the download thread
        self.requestInterruption()


if __name__ == '__main__':
    import sys
    if len(sys.argv) <= 1:
        sys.exit()

    url = sys.argv[1]
    app = QApplication([])
    window = DownloadWindow()
    window.show()
    app.exec()

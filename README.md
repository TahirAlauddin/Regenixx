Command to create installer
    pyinstaller -Fw --onefile --icon=icon.ico --add-data "fonts;fonts" main.py

Command to create installer for download_updates.py
    pyinstaller -Fw --onefile --icon=icon.ico download_updates.py
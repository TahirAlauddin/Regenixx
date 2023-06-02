Command to create installer
    pyinstaller -Fw --onefile --icon=icon.ico --add-data "fonts;fonts" main.py

Command to create installer for download_updates.py
    pyinstaller -Fw --onefile --icon=icon.ico download_updates.py

Everytime a new update is released, `settings.json` and `version.json` file are always updated

Make sure to include the Environment Variables in the software when deploying the changes
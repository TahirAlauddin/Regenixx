# ///////////////////////////////////////////////////////////////
#
# BY: WANDERSON M.PIMENTA
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.0
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts, any information in the visual
# interface (GUI) can be modified without any implication.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html
#
# ///////////////////////////////////////////////////////////////

# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from uis.windows.main_window.functions_main_window import *
from s3_bucket_url import get_url, get_latest_version
from utils import messageBoxStyle
from subprocess import Popen
import sys
import os
import logging
import traceback
import datetime
import ctypes
import json
import time

myappid = 'tahiralauddin.regenixx.1.0.2' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)



# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from core.json_settings import Settings

# IMPORT PY ONE DARK WINDOWS
# ///////////////////////////////////////////////////////////////
# MAIN WINDOW
from uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from widgets import *

# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'

# MAIN WINDOW
# ///////////////////////////////////////////////////////////////
class MainWindow(QMainWindow):

    pdfCreateSignal = Signal()
    pdfCreateShowProgressSignal = Signal(str)
    removeProgressBar = Signal()
    patientAddedToDatabaseSignal = Signal()
    downloadUpdatesSignal = Signal()

    def __init__(self):
        super().__init__()

        self.SetupMainWindow = SetupMainWindow
        self.image_plan1 = self.image_plan2 = self.image_plan3 = None
        self.diagnosesLineEdits = []
        self.pdfCreateSignal.connect(self.showPDFCreatingProgressBar)
        self.pdfCreateShowProgressSignal.connect(self.updateProgressBar)
        self.removeProgressBar.connect(self.hideProgressBar)
        self.patientAddedToDatabaseSignal.connect(self.refreshPatientsPage)
        self.downloadUpdatesSignal.connect(self.handleDownloadUpdatesSignal)
        

        from threading import Thread

        thread = Thread(target=self.checkForUpdates)
        # thread.daemon = True
        thread.start()

        # SETUP MAIN WINDOW
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # Remove Selection If Clicked By "btn_close_left_column"
        if btn.objectName() != "btn_settings":
            self.ui.left_menu.deselect_all_tab()

        # Get Title Bar Btn And Reset Active         
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")
        top_settings.set_active(False)

        # LEFT MENU
        # ///////////////////////////////////////////////////////////////
        
        # HOME BTN
        if btn.objectName() == "btn_home":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 1
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # DIAGNOSIS BTN
        if btn.objectName() == "btn_diagnoses":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 2
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # LOAD USER PAGE
        if btn.objectName() == "btn_patients":
            # Select Menu
            self.ui.left_menu.select_only_one(btn.objectName())

            # Load Page 3 
            MainFunctions.set_page(self, self.ui.load_pages.page_3)
    

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)

                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn       (REMOVED FOR NOW)     
            # top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            # top_settings.set_active_tab(False)            

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPosition().toPoint()
    
    def showPDFCreatingProgressBar(self):
        from uis.windows.splash_screen import SplashScreen
        self.splashScreen = SplashScreen(self)
        self.splashScreen.progress("Initializing...")

    def updateProgressBar(self, message=None):
        self.splashScreen.progress(message)

    def hideProgressBar(self):
        self.splashScreen.close()

    def refreshPatientsPage(self):
        from setup_patients_ui import setup_patients
        setup_patients(self)

    def remove_all_widgets(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.remove_all_widgets(child.layout())

    def showPatientsDetail(self, patient):
        # Remove previous labels 

        self.remove_all_widgets(self.ui.load_pages.plan1ServicesVerticalLayout)
        self.remove_all_widgets(self.ui.load_pages.plan2ServicesVerticalLayout)
        self.remove_all_widgets(self.ui.load_pages.plan3ServicesVerticalLayout)
        

        self.ui.load_pages.pages.setCurrentIndex(3)
        self.ui.load_pages.patientNameLabel.setText(patient['name'])
        self.ui.load_pages.patientDateOfBirth.setText(patient['date_of_birth'])
        
        self.ui.load_pages.patientDateAddedLabel.setText(patient['date_added'])
        icon = QIcon()
        icon.addFile('gui/images/svg_icons/icon-clock.png')
        self.ui.load_pages.patientDateAddedLabel.setIcon(icon)

        services = patient['service_plans'][0]
        discount = services['discount']
        plan1Subtotal = 0
        self.ui.load_pages.plan1Discount.setText(str(discount)+'%')
        for service, price in services['services']:
            serviceLabel = QLabel(service)
            priceLabel = QLabel('$'+str(price))
            serviceLabel.setMinimumWidth(700)
            horizontalLayout = QHBoxLayout()
            horizontalLayout.setContentsMargins(9,9,9,9)
            horizontalLayout.addWidget(serviceLabel)
            horizontalLayout.addWidget(priceLabel) #, 1, Qt.AlignRight)
            # Spacer
            spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            horizontalLayout.addItem(spacer)
            self.ui.load_pages.plan1ServicesVerticalLayout.addLayout(horizontalLayout)
            priceLabel.setAlignment(Qt.AlignRight)
            plan1Subtotal += price

        services = patient['service_plans'][1]
        discount = services['discount']
        plan2Subtotal = 0
        self.ui.load_pages.plan2Discount.setText(str(discount)+'%')
        for service, price in services['services']:
            serviceLabel = QLabel(service)
            priceLabel = QLabel('$'+str(price))
            serviceLabel.setMinimumWidth(700)
            horizontalLayout = QHBoxLayout()
            horizontalLayout.setContentsMargins(9,9,9,9)
            horizontalLayout.addWidget(serviceLabel)
            horizontalLayout.addWidget(priceLabel) #, 1, Qt.AlignRight)
            # Spacer
            spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            horizontalLayout.addItem(spacer)
            self.ui.load_pages.plan2ServicesVerticalLayout.addLayout(horizontalLayout)
            priceLabel.setAlignment(Qt.AlignRight)
            plan2Subtotal += price

        services = patient['service_plans'][2]
        discount = services['discount']
        plan3Subtotal = 0
        self.ui.load_pages.plan3Discount.setText(str(discount)+'%')
        for service, price in services['services']:
            serviceLabel = QLabel(service)
            priceLabel = QLabel('$'+str(price))
            serviceLabel.setMinimumWidth(700)
            horizontalLayout = QHBoxLayout()
            horizontalLayout.setContentsMargins(9,9,9,9)
            horizontalLayout.addWidget(serviceLabel)
            horizontalLayout.addWidget(priceLabel) #, 1, Qt.AlignRight)
            # Spacer
            spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            horizontalLayout.addItem(spacer)
            self.ui.load_pages.plan3ServicesVerticalLayout.addLayout(horizontalLayout)
            priceLabel.setAlignment(Qt.AlignRight)
            plan3Subtotal += price


        self.ui.load_pages.plan1SubtotalAmount.setText(f'$ {plan1Subtotal}')
        self.ui.load_pages.plan2SubtotalAmount.setText(f'$ {plan2Subtotal}')
        self.ui.load_pages.plan3SubtotalAmount.setText(f'$ {plan3Subtotal}')

        self.ui.load_pages.plan1DiscountAmount.setText(f'$ {plan1Subtotal*discount/100}')
        self.ui.load_pages.plan2DiscountAmount.setText(f'$ {plan2Subtotal*discount/100}')
        self.ui.load_pages.plan3DiscountAmount.setText(f'$ {plan3Subtotal*discount/100}')

        self.ui.load_pages.plan1TotalAmount.setText(f'$ {plan1Subtotal - (plan1Subtotal*discount/100)}')
        self.ui.load_pages.plan2TotalAmount.setText(f'$ {plan2Subtotal - (plan2Subtotal*discount/100)}')
        self.ui.load_pages.plan3TotalAmount.setText(f'$ {plan3Subtotal - (plan3Subtotal*discount/100)}')


    def goBackToPatientsPage(self):
        self.ui.load_pages.pages.setCurrentIndex(2)


    def checkForUpdates(self):
        while True:
            latest_version = get_latest_version().strip('.zip').strip('regenixx-')
            # Check if the local version matches the latest version
            with open('version.json', 'r') as f:
                version_data = json.load(f)
            local_version = version_data["version"]

            if local_version != latest_version:
                # Get user's input, whether they want to update the software or not
                self.downloadUpdatesSignal.emit()
                break
                    
            time.sleep(5)

    def showUpdateAvaiableWindow(self):
        messageBox = QMessageBox()
        messageBox.setWindowTitle("Update Available")
        messageBox.setText("New Update is available. Do you want to download new updates?")
        messageBox.setIcon(QMessageBox.Information)
        # Add some custom styles to the QMessageBox
        messageBox.setStyleSheet(messageBoxStyle)
        
        # Add a button to the QMessageBox and show it
        messageBox.addButton(QMessageBox.Yes)
        messageBox.addButton(QMessageBox.No)

        button_chosen = messageBox.exec()

        if button_chosen == QMessageBox.No:
            messageBox.close()
            return False
        elif button_chosen == QMessageBox.Yes:
            # Dead end
            return True


    def download_updates(self):
        url = get_url()
        Popen(['python', 'download_updates.py', url])
        sys.exit()


    def handleDownloadUpdatesSignal(self):

        downloadUpdates = self.showUpdateAvaiableWindow()
        if downloadUpdates:
            self.download_updates()
            

def main():
    global window, app
    # Configure logger
    logger = logging.getLogger(__name__)
    logger.setLevel(logging.ERROR)

    # Create file handler
    handler = logging.FileHandler('error.log')
    handler.setLevel(logging.ERROR)

    # Create formatter
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    # Add handler to logger
    logger.addHandler(handler)

    # Example code that generates an error
    try:

        app = QApplication(sys.argv)
        app.setWindowIcon(QIcon("icon.svg"))
        window = MainWindow()

        # EXEC APP
        # ///////////////////////////////////////////////////////////////
        sys.exit(app.exec())

    except Exception as e:
        # Get error message with traceback
        error_message = traceback.format_exc()

        # Format error message with timestamp
        log_message = f"{datetime.datetime.now()} - ERROR - {error_message}"

        # Write error message to file
        logger.error(log_message)



# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    main()

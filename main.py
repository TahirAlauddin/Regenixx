# ///////////////////////////////////////////////////////////////
#
# PROJECT MADE WITH: Qt Designer and PySide6
# V: 1.0.5
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
from setup_patients_ui import setup_patients
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

myappid = 'tahiralauddin.regenixx.1.0.5' # arbitrary string
ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

from threading import Thread


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
    closed = False

    def __init__(self):
        super().__init__()

        self.SetupMainWindow = SetupMainWindow
        self.image_plan1 = self.image_plan2 = self.image_plan3 = None
        self.diagnosesLineEdits = []
        self.pdfCreateSignal.connect(self.showPDFCreatingProgressBar)
        self.pdfCreateShowProgressSignal.connect(self.updateProgressBar)
        self.removeProgressBar.connect(self.handleRemoveProgressBar)
        self.patientAddedToDatabaseSignal.connect(self.refreshPatientsPage)
        self.downloadUpdatesSignal.connect(self.handleDownloadUpdatesSignal)
        
        #! This block of code must run in each update, each version of the software
        thread = Thread(target=self.checkForUpdates)
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

    def handleRemoveProgressBar(self):
        self.splashScreen.close()
        self.splashScreen.ui.progressBar.setValue(0)
        self.splashScreen.counter = 0
        self.splashScreen.smoothCounter = 0

    def refreshPatientsPage(self):
        setup_patients(self)

    def remove_all_widgets(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
            elif child.layout():
                self.remove_all_widgets(child.layout())

    def addServicesInPatientsPage(self, layout, discountLabel, services):
        """ This function adds Dynamic details of a patient's Plan +to UI"""
        discount = services['discount']
        planSubtotal = 0
        discountLabel.setText(str(discount)+'%')
        for service, price, quantity in services['services']:
            serviceTitle = f'{service}'
            if str(quantity).isdigit() and int(quantity) > 1:
                serviceTitle = f'{service} x ({quantity})'
                price *= int(quantity)
                
            serviceLabel = QLabel(serviceTitle)
            priceLabel = QLabel(f"$ {'{:.2f}'.format(price)}")
            serviceLabel.setMinimumWidth(700)
            # Service Title and Price should show horizontally
            horizontalLayout = QHBoxLayout()
            horizontalLayout.setContentsMargins(9,9,9,9)
            horizontalLayout.addWidget(serviceLabel)
            horizontalLayout.addWidget(priceLabel)
            # Spacer
            spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
            horizontalLayout.addItem(spacer)
            # Add all of the QWidgets to the main layout
            layout.addLayout(horizontalLayout)
            priceLabel.setAlignment(Qt.AlignRight)
            planSubtotal += price

        return planSubtotal, discount

    def showPatientsDetail(self, patient):

        # Remove previous labels 
        self.remove_all_widgets(self.ui.load_pages.plan1ServicesVerticalLayout)
        self.remove_all_widgets(self.ui.load_pages.plan2ServicesVerticalLayout)
        self.remove_all_widgets(self.ui.load_pages.plan3ServicesVerticalLayout)


        # Other Attributes
        self.ui.load_pages.pages.setCurrentIndex(3)
        self.ui.load_pages.deletePatientButton.setObjectName(str(patient['id']))
        self.ui.load_pages.patientNameLabel.setText(patient['name'])
        self.ui.load_pages.patientDateOfBirth.setText(patient['date_of_birth'])
        self.ui.load_pages.patientDateAddedLabel.setText(patient['date_added'])
        
        icon = QIcon('gui/images/svg_icons/icon-clock.png')
        self.ui.load_pages.patientDateAddedLabel.setIcon(icon)

        icon = QIcon('gui/images/svg_icons/icon-delete.png')
        self.ui.load_pages.deletePatientButton.setIcon(icon)


        services = patient['service_plans'][0]
        plan1Subtotal, plan1Discount = self.addServicesInPatientsPage(
                            self.ui.load_pages.plan1ServicesVerticalLayout,
                            self.ui.load_pages.plan1Discount, services)

        services = patient['service_plans'][1]
        plan2Subtotal, plan2Discount = self.addServicesInPatientsPage(
                            self.ui.load_pages.plan2ServicesVerticalLayout,
                            self.ui.load_pages.plan2Discount, services)

        services = patient['service_plans'][2]
        plan3Subtotal, plan3Discount = self.addServicesInPatientsPage(
                            self.ui.load_pages.plan3ServicesVerticalLayout,
                            self.ui.load_pages.plan3Discount, services)

        # Subtotals for all plans
        self.ui.load_pages.plan1SubtotalAmount.setText(f'$ {"{:.2f}".format(plan1Subtotal)}')
        self.ui.load_pages.plan2SubtotalAmount.setText(f'$ {"{:.2f}".format(plan2Subtotal)}')
        self.ui.load_pages.plan3SubtotalAmount.setText(f'$ {"{:.2f}".format(plan3Subtotal)}')

        # Discount Prices for all plans
        self.ui.load_pages.plan1DiscountAmount.setText(f'$ {"{:.2f}".format(plan1Subtotal*plan1Discount/100)}')
        self.ui.load_pages.plan2DiscountAmount.setText(f'$ {"{:.2f}".format(plan2Subtotal*plan2Discount/100)}')
        self.ui.load_pages.plan3DiscountAmount.setText(f'$ {"{:.2f}".format(plan3Subtotal*plan3Discount/100)}')

        # Total prices for all plans
        self.ui.load_pages.plan1TotalAmount.setText(f'$ {"{:.2f}".format(plan1Subtotal - (plan1Subtotal*plan1Discount/100))}')
        self.ui.load_pages.plan2TotalAmount.setText(f'$ {"{:.2f}".format(plan2Subtotal - (plan2Subtotal*plan2Discount/100))}')
        self.ui.load_pages.plan3TotalAmount.setText(f'$ {"{:.2f}".format(plan3Subtotal - (plan3Subtotal*plan3Discount/100))}')

        
    def deletePatient(self):
        icon = QIcon('gui/images/svg_icons/icon-delete-pressed.png')
        self.ui.load_pages.deletePatientButton.setIcon(icon)
        button_chosen = self.showQMessageBox('Confirm Deletion', 'Are you sure you want to delete the patient record?',
                             [QMessageBox.Yes, QMessageBox.No])
        if button_chosen == QMessageBox.No:
            icon = QIcon('gui/images/svg_icons/icon-delete.png')
            self.ui.load_pages.deletePatientButton.setIcon(icon)
            return

        self.ui.load_pages.goBackToPatientstPageButton.click()
        Database.delete_patient(int(self.ui.load_pages.deletePatientButton.objectName()))
        setup_patients(self)


    def goBackToPatientsPage(self):
        self.ui.load_pages.pages.setCurrentIndex(2)


    def checkForUpdates(self):
        with open('version.json', 'r') as f:
            version_data = json.load(f)
        local_version = version_data["version"]
        while True:
            latest_version = get_latest_version(local_version).strip('.zip').strip('regenixx-')
            # Check if the local version matches the latest version

            if local_version <= latest_version:
                # Get user's input, whether they want to update the software or not
                self.downloadUpdatesSignal.emit()
                break

            if self.closed:
                break
                
            # Check for new updates every 10 seconds
            time.sleep(10)

    def closeEvent(self, event):
        self.closed = True
        event.accept()


    def showUpdateAvaiableWindow(self):
        # Get the user selection
        button_chosen = self.showQMessageBox(window_title="Update Available", 
                            text="New Update is available. Do you want to download new updates?",
                            buttons=[QMessageBox.Yes, QMessageBox.No])
        # If user pressed no, return False
        if button_chosen == QMessageBox.No:
            return False
        # If user pressed yes, return True
        elif button_chosen == QMessageBox.Yes:
            # Dead end, close the GUI and download updates
            return True
        
    def showQMessageBox(self, window_title=None, text=None, buttons=None):
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


    def download_updates(self):
        url = get_url()
        if getattr(sys, 'frozen', False):
            # Running as a bundled executable, use _MEIPASS to get the temp folder
            Popen(['updater.exe', url])
        else:
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

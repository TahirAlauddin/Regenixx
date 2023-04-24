# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
import os
import sqlite3
from generate_pdf import generatePDF
from round_image import add_rounded_border
from threading import Thread
import winreg
from constants import EXCEL_FILE_NAME

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *
from widgets.py_autocomplete_box import AutocompleteSearchBox

# FUNCTIONS
class MainFunctions():
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # SET MAIN WINDOW PAGES
    # ///////////////////////////////////////////////////////////////
    def set_page(self, page):
        self.ui.load_pages.pages.setCurrentWidget(page)

    # SET LEFT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_left_column_menu(
        self,
        menu,
        title,
        icon_path
    ):
        self.ui.left_column.menus.menus.setCurrentWidget(menu)
        self.ui.left_column.title_label.setText(title)
        self.ui.left_column.icon.set_icon(icon_path)

    # RETURN IF LEFT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def left_column_is_visible(self):
        width = self.ui.left_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # RETURN IF RIGHT COLUMN IS VISIBLE
    # ///////////////////////////////////////////////////////////////
    def right_column_is_visible(self):
        width = self.ui.right_column_frame.width()
        if width == 0:
            return False
        else:
            return True

    # SET RIGHT COLUMN PAGES
    # ///////////////////////////////////////////////////////////////
    def set_right_column_menu(self, menu):
        self.ui.right_column.menus.setCurrentWidget(menu)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_title_bar_btn(self, object_name):
        return self.ui.title_bar_frame.findChild(QPushButton, object_name)

    # GET TITLE BUTTON BY OBJECT NAME
    # ///////////////////////////////////////////////////////////////
    def get_left_menu_btn(self, object_name):
        return self.ui.left_menu.findChild(QPushButton, object_name)
    
    # LEDT AND RIGHT COLUMNS / SHOW / HIDE
    # ///////////////////////////////////////////////////////////////
    def toggle_left_column(self):
        # GET ACTUAL CLUMNS SIZE
        width = self.ui.left_column_frame.width()
        right_column_width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, width, right_column_width, "left")

    def toggle_right_column(self):
        # GET ACTUAL CLUMNS SIZE
        left_column_width = self.ui.left_column_frame.width()
        width = self.ui.right_column_frame.width()

        MainFunctions.start_box_animation(self, left_column_width, width, "right")

    def start_box_animation(self, left_box_width, right_box_width, direction):
        right_width = 0
        left_width = 0
        time_animation = self.ui.settings["time_animation"]
        minimum_left = self.ui.settings["left_column_size"]["minimum"]
        maximum_left = self.ui.settings["left_column_size"]["maximum"]
        minimum_right = self.ui.settings["right_column_size"]["minimum"]
        maximum_right = self.ui.settings["right_column_size"]["maximum"]

        # Check Left Values        
        if left_box_width == minimum_left and direction == "left":
            left_width = maximum_left
        else:
            left_width = minimum_left

        # Check Right values        
        if right_box_width == minimum_right and direction == "right":
            right_width = maximum_right
        else:
            right_width = minimum_right       

        # ANIMATION LEFT BOX        
        self.left_box = QPropertyAnimation(self.ui.left_column_frame, b"minimumWidth")
        self.left_box.setDuration(time_animation)
        self.left_box.setStartValue(left_box_width)
        self.left_box.setEndValue(left_width)
        self.left_box.setEasingCurve(QEasingCurve.InOutQuart)

        # ANIMATION RIGHT BOX        
        self.right_box = QPropertyAnimation(self.ui.right_column_frame, b"minimumWidth")
        self.right_box.setDuration(time_animation)
        self.right_box.setStartValue(right_box_width)
        self.right_box.setEndValue(right_width)
        self.right_box.setEasingCurve(QEasingCurve.InOutQuart)

        # GROUP ANIMATION
        self.group = QParallelAnimationGroup()
        self.group.stop()
        self.group.addAnimation(self.left_box)
        self.group.addAnimation(self.right_box)
        self.group.start()

        
    # Functions for Add, Remove
    def addRow(tableWidget: QTableWidget):
        rowCount = tableWidget.rowCount()
        tableWidget.setRowCount(rowCount + 1)
        tableWidget.setItem(rowCount + 1, 0, QTableWidgetItem())
        tableWidget.setItem(rowCount + 1, 1, QTableWidgetItem())
        tableWidget.setItem(rowCount + 1, 2, QTableWidgetItem())
        tableWidget.setItem(rowCount + 1, 3, QTableWidgetItem())
        
    def removeRow(tableWidget: QTableWidget):
        tableWidget.removeRow(tableWidget.currentRow())

    def createPDF(mainWindow):
        
        mainWindow.pdfCreateSignal.emit()

        # Create PDF
        diagnoses = []
        for diagnosisLineEdit in mainWindow.diagnosesLineEdits:
            diagnoses.append(diagnosisLineEdit.text())
        
        diagnosis = ', '.join(diagnoses)
        patients_name = mainWindow.patientsNameLineEdit.text()
        patients_date_of_birth = mainWindow.patientsDateOfBirth.date().toPython().strftime("%B %d, %Y")

        discountPlan1 = int(mainWindow.discountComboBoxBestTable.currentText().strip('%'))
        discountPlan2 = int(mainWindow.discountComboBoxBetterTable.currentText().strip('%'))
        discountPlan3 = int(mainWindow.discountComboBoxGoodTable.currentText().strip('%'))
        services_plan1 = []
        services_plan2 = []
        services_plan3 = []
        goodTable = mainWindow.goodTable
        betterTable = mainWindow.betterTable
        bestTable = mainWindow.bestTable

        for row in range(goodTable.rowCount()):
            title = goodTable.item(row, 0).text()
            cost = goodTable.item(row, 1).text()
            services_plan3.append([title, cost])

        for row in range(betterTable.rowCount()):
            title = betterTable.item(row, 0).text()
            cost = betterTable.item(row, 1).text()
            services_plan2.append([title, cost])

        for row in range(bestTable.rowCount()):
            title = bestTable.item(row, 0).text()
            cost = bestTable.item(row, 1).text()
            services_plan1.append([title, cost])

        if not all([mainWindow.image_plan1, mainWindow.image_plan2, mainWindow.image_plan3]):
            # User must provide all images
            QMessageBox.critical(mainWindow, "Error occured!", "Please provide images!")
            mainWindow.removeProgressBar.emit()
            return
            mainWindow.image_plan1, mainWindow.image_plan2, mainWindow.image_plan3 = ['images/consultation2.jpg', 
                                                                                      'images/financialconsultation.jpg',
                                                                                      'images/JENNWIDE2.jpg']
        
        for diagnosis_for_db in diagnoses:
            MainFunctions.add_diagnosis_in_db(diagnosis_for_db)

        diagnoses = MainFunctions.get_diagnosis_from_db()
        mainWindow.SetupMainWindow.removeCustomWidgetFromWindow(mainWindow)
        mainWindow.diagnosisLineEdit = AutocompleteSearchBox(
            text = "",
            place_holder_text = "Diagnosis Description",
            radius = 8,
            border_size = 2,
            color = mainWindow.themes["app_color"]["text_foreground"],
            selection_color = mainWindow.themes["app_color"]["white"],
            bg_color = mainWindow.themes["app_color"]["dark_one"],
            bg_color_active = mainWindow.themes["app_color"]["dark_three"],
            context_color = mainWindow.themes["app_color"]["context_color"],
            items=diagnoses
        )
        mainWindow.SetupMainWindow.addWidgetToWindow(mainWindow)

        def populateDataIntoPDF():
            if not os.path.exists('pdf-images'):
                os.mkdir('pdf-images')
            mainWindow.pdfCreateShowProgressSignal.emit('CROPPING IMAGE 1')
            image_plan1 = add_rounded_border(mainWindow.image_plan1)
            mainWindow.pdfCreateShowProgressSignal.emit('CROPPING IMAGE 2')
            image_plan2 = add_rounded_border(mainWindow.image_plan2)
            mainWindow.pdfCreateShowProgressSignal.emit('CROPPING IMAGE 3')
            image_plan3 = add_rounded_border(mainWindow.image_plan3)
            mainWindow.pdfCreateShowProgressSignal.emit('IMAGES CROPPED SUCCESSFULLY!')
            # Generate PDF File
            try:
                output_folder = MainFunctions.get_users_desktop_folder()
                pdf_path = os.path.join(output_folder, f'{patients_name} - {patients_date_of_birth}.pdf')
                generatePDF(patients_name, patients_date_of_birth,
                            diagnosis, image_plan1, image_plan2, image_plan3,
                            services_plan1, services_plan2, services_plan3,
                            discountPlan1, discountPlan2, discountPlan3,
                            output_pdf_path=pdf_path,
                            signal=mainWindow.pdfCreateShowProgressSignal)
                
                # Remove temporary images
                os.remove(image_plan1)
                os.remove(image_plan2)
                os.remove(image_plan3)

                # Add Patient into database
                MainFunctions.add_patient_to_database(patients_name, patients_date_of_birth,
                            diagnosis, services_plan1, services_plan2, services_plan3,
                            discountPlan1, discountPlan2, discountPlan3)
                
                mainWindow.patientAddedToDatabaseSignal.emit()

                

            except:
                pass
            
        thread = Thread(target=populateDataIntoPDF)
        thread.start()


    def add_patient_to_database(patient_name, date_of_birth, diagnosis,
                                services_plan1, services_plan2, services_plan3,
                                discountPlan1, discountPlan2, discountPlan3):
        try:
            from datetime import datetime

            # get current date and time
            current_date = datetime.now()

            # format current date as string in YYYY-MM-DD format
            date_added = current_date.strftime('%Y-%m-%d')

            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()
            
            # Start transaction
            cursor.execute('BEGIN')

            services_plan1_id = MainFunctions.add_service_plan(cursor, services_plan1, discountPlan1)
            services_plan2_id = MainFunctions.add_service_plan(cursor, services_plan2, discountPlan2)
            services_plan3_id = MainFunctions.add_service_plan(cursor, services_plan3, discountPlan3)

            cursor.execute("CREATE TABLE IF NOT EXISTS patientsTable (id INTEGER PRIMARY KEY, patients_name VARCHAR, \
                        patients_date_of_birth DATE, date_added DATE, diagnosis VARCHAR, \
                        services_plan1_id INTEGER REFERENCES ServicesPlan(id), \
                        services_plan2_id INTEGER REFERENCES ServicesPlan(id), \
                        services_plan3_id INTEGER REFERENCES ServicesPlan(id))")
            if diagnosis:
                cursor.execute("INSERT INTO patientsTable (patients_name, patients_date_of_birth, date_added,\
                                diagnosis, services_plan1_id, services_plan2_id, services_plan3_id) \
                                VALUES (?, ?, ?, ?, ?, ?, ?)", 
                (patient_name, date_of_birth, date_added, diagnosis, services_plan1_id, services_plan2_id, services_plan3_id))

                
            # cursor.execute('COMMIT')

            # End transaction
            connection.commit()

        except Exception as e:
            # Rollback transaction in case of errors
            cursor.execute("ROLLBACK")
            print(e)
            return False
        finally:
            connection.close()
        return True
    
    def add_service_plan(cursor, services, discount):

        
        cursor.execute("CREATE TABLE IF NOT EXISTS ServicesPlan (id INTEGER PRIMARY KEY, discount INTEGER)")
        cursor.execute("CREATE TABLE IF NOT EXISTS Services (id INTEGER PRIMARY KEY, service_plan_id INTEGER REFERENCES ServicesPlan(id), service VARCHAR, price INTEGER)")

        # Insert service plan into ServicesPlan table
        cursor.execute('INSERT INTO ServicesPlan (discount) VALUES (?)', (discount,)) 
        service_plan_id = cursor.lastrowid

        # Insert each service into Services table
        for service, price in services:
            cursor.execute('INSERT INTO Services (service_plan_id, service, price) VALUES (?, ?, ?)',
                            (service_plan_id, service, price))

        return service_plan_id
    

    def get_services():
        try:
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()

            # Fetch all service plans with their associated services
            cursor.execute('SELECT ServicesPlan.id, Services.service, Services.price, ServicesPlan.discount \
                            FROM ServicesPlan JOIN Services ON Services.service_plan_id = ServicesPlan.id')
            service_data = cursor.fetchall()

            # Transform data into a dictionary where each service plan is a key and its value is a list of associated services
            services = {}
            for row in service_data:
                service_plan_id, service, price, discount = row
                if service_plan_id not in services:
                    services[service_plan_id] = {'discount': discount, 'services': []}
                services[service_plan_id]['services'].append({'service': service, 'price': price})

            return services

        except Exception as e:
            print(e)
            return None
        finally:
            connection.close()


    def get_patients():
        try:
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()

            # Fetch all patients with their associated service plans
            cursor.execute('SELECT patientsTable.id, patientsTable.patients_name, patientsTable.patients_date_of_birth, \
                            patientsTable.date_added, patientsTable.diagnosis, \
                            ServicesPlan1.id, ServicesPlan1.discount, \
                            ServicesPlan2.id, ServicesPlan2.discount, \
                            ServicesPlan3.id, ServicesPlan3.discount \
                            FROM patientsTable \
                            JOIN ServicesPlan AS ServicesPlan1 ON patientsTable.services_plan1_id = ServicesPlan1.id \
                            JOIN ServicesPlan AS ServicesPlan2 ON patientsTable.services_plan2_id = ServicesPlan2.id \
                            JOIN ServicesPlan AS ServicesPlan3 ON patientsTable.services_plan3_id = ServicesPlan3.id')
            patient_data = cursor.fetchall()

            # Transform data into a list of dictionaries where each dictionary represents a patient
            patients = []
            for row in patient_data:
                patient_id, patient_name, date_of_birth, date_added, diagnosis, \
                service_plan1_id, discount1, service_plan2_id, discount2, service_plan3_id, discount3 = row

                patient = {'id': patient_id,
                        'name': patient_name,
                        'date_of_birth': date_of_birth,
                        'date_added': date_added,
                        'diagnosis': diagnosis,
                        'service_plans': [
                            {'services': MainFunctions.get_services_by_service_plan_id(service_plan1_id), 'discount': discount1},
                            {'services': MainFunctions.get_services_by_service_plan_id(service_plan2_id), 'discount': discount2},
                            {'services': MainFunctions.get_services_by_service_plan_id(service_plan3_id), 'discount': discount3}
                        ]
                        }

                patients.append(patient)

            return patients

        except Exception as e:
            print(e)
            return None
        finally:
            connection.close()


    def get_services_by_service_plan_id(service_plan_id):
        try:
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()

            # Select all services for the given service plan ID
            cursor.execute('SELECT service, price FROM Services WHERE service_plan_id = ?', (service_plan_id,))
            services = cursor.fetchall()

            return services

        except Exception as e:
            print(e)
            return None
        finally:
            connection.close()



    def get_users_desktop_folder():
        # Open the registry key for the desktop folder
        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Explorer\Shell Folders")

        # Get the value of the "Desktop" key
        desktop_path = winreg.QueryValueEx(key, "Desktop")[0]

        return desktop_path


    
    def get_services_from_excel(window):
        import openpyxl
        workbook = openpyxl.load_workbook(EXCEL_FILE_NAME)
        sheet = workbook.active
        
        # Read data from each row
        data = []
        header = []
        for row in sheet.iter_rows(max_row=1, values_only=True):
            try:
                header.extend([
                    str(row[0]),
                    str(row[1]),
                    str(row[2]),
                    str(row[3]),
                ])
            except IndexError:
                header.extend(['Category', 'Title', 'Cost', 'Description'])

        error_occured = False
        for row in sheet.iter_rows(min_row=2, values_only=True):
            try:
                row_data = [
                    str(row[0]),
                    str(row[1]),
                    str(row[2]),
                    str(row[3]),
                ]
                if str(row[2]).isdigit():
                    data.append(row_data)
            except IndexError:
                if len(data) < 1:
                    data.append(['', '', '', ''])
                    error_occured = True

        if error_occured:
            QMessageBox.critical(window, 'Error in Excel File', 
                            'The program couldn\'t read the Excel file. Make sure there are exactly 4 columns.')

        return data, header

    # Set Image and define the width/height for Pixmap        
    def setImageForPixmap(label, width, height, file=None):
        pixmap = QPixmap(file)
        pixmap = pixmap.scaledToWidth(width , Qt.SmoothTransformation)
        pixmap = pixmap.scaledToHeight(height, Qt.SmoothTransformation)
        label.setPixmap(pixmap)
        label.setMaximumSize(QSize(width, height))

    def get_diagnosis_from_db():
        try:
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS diagnosisTable (id INTEGER PRIMARY KEY, diagnosis VARCHAR UNIQUE)")
            cursor.execute("SELECT diagnosis FROM diagnosisTable")
            diagnoses = [item[0] for item in cursor.fetchall()]
            return diagnoses
        except Exception as e:
            print(e)

    def add_diagnosis_in_db(diagnosis: str):
        try:
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS diagnosisTable (id INTEGER PRIMARY KEY, diagnosis VARCHAR UNIQUE)")
            if diagnosis:
                cursor.execute("INSERT INTO diagnosisTable (diagnosis) VALUES (?)", (diagnosis,))
            connection.commit()
            connection.close()
        except Exception as e:
            print(e)
            return False
        return True
    

    def update_diagnoses_in_db(diagnoses):
        # diagnoses = MainFunctions.list_diagnosis_from_db()
        
        conn = sqlite3.connect('db.sqlite3')
        cursor = conn.cursor()
        # Begin transaction
        try:
            cursor.execute("BEGIN")

            cursor.execute("DELETE FROM diagnosisTable;")

            # Insert data into diagnosisTable
            cursor.executemany("INSERT INTO diagnosisTable (id, diagnosis) VALUES (?, ?)", diagnoses)

            # Commit transaction if all statements are successful
            conn.commit()
            print("Transaction completed successfully.")

        except:
            # Rollback transaction if any statement fails
            conn.rollback()
            MainFunctions.log_db_errors("Transaction failed. Rolled back changes.")

        finally:
            # Close cursor and connection
            cursor.close()
            conn.close()


    def list_diagnosis_from_db():
        try:
            connection = sqlite3.connect('db.sqlite3')
            cursor = connection.cursor()
            cursor.execute("CREATE TABLE IF NOT EXISTS diagnosisTable (id INTEGER PRIMARY KEY, diagnosis VARCHAR UNIQUE)")
            cursor.execute("SELECT id, diagnosis FROM diagnosisTable")
            diagnoses = [(item[0], item[1]) for item in cursor.fetchall()]
            return diagnoses
        except:
            MainFunctions.log_db_errors()

    def changeExcelFile(window):
        filename, _ = QFileDialog.getOpenFileName(window, 'Select Excel File', '', 'Excel Files (*.xlsx)')
        if filename:
            filecontent = open(filename, 'rb').read()
            open(EXCEL_FILE_NAME, 'wb').write(filecontent)

    def log_db_errors(message=None):
        import traceback, datetime
        # Get error message with traceback
        error_message = traceback.format_exc()
        # Format error message with timestamp
        log_message = f"{datetime.datetime.now()} - ERROR - {error_message}"
        with open('db.error.log', 'a') as error_log_file:
            error_log_file.write(log_message)
            if message:
                error_log_file.write(message + '\n')
                

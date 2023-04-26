from qt_core import *
from utils import *
from core.json_themes import Themes
from uis.windows.main_window.functions_main_window import Functions, Database

def setup_patients(self):
        
        themes = Themes().items

        # Set ScrollArea styles
        set_stylesheet(
                self.ui.load_pages.page_4_scrollArea, scrollBarStyle,
                scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
                scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
                context_color = self.themes["app_color"]["context_color"]
        )

        self.ui.load_pages.page_4_scrollArea.setStyleSheet(self.ui.load_pages.page_4_scrollArea.styleSheet() + ' QScrollArea {border: none;}')

        icon = QIcon()
        icon.addFile(r"gui/images/svg_icons/icon-user-male.png", QSize(), QIcon.Normal, QIcon.Off)
        self.ui.load_pages.logo_2.setIcon(icon)

        
        icon18 = QtGui.QIcon()
        icon18.addPixmap(QtGui.QPixmap(r"gui\images\svg_icons\down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon19 = QtGui.QIcon()
        icon19.addPixmap(QtGui.QPixmap(r"gui\images\svg_icons\down-arrow.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_patient_male = QtGui.QIcon()
        icon_patient_male.addPixmap(QtGui.QPixmap(r"gui\images\svg_icons\icon-user-male.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        icon_patient_female = QtGui.QIcon()
        icon_patient_female.addPixmap(QtGui.QPixmap(r"gui\images\svg_icons\icon-user-female.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)


        if self.ui.load_pages.patientsPageMainFrame:
                self.ui.load_pages.patientsPageMainFrame.close()
                self.ui.load_pages.patientsPageMainFrame = None
        else:
                self.patientsPageMainFrame.close()        


        self.patientsPageMainFrame = QtWidgets.QFrame()
        self.patientsPageMainFrame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.patientsPageMainFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.patientsPageMainFrame.setObjectName("patientsPageMainFrame")
        self.verticalLayout_27 = QtWidgets.QVBoxLayout(self.patientsPageMainFrame)
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_27.setSpacing(0)
        self.verticalLayout_27.setObjectName("verticalLayout_27")
        self.scrollArea_3 = QtWidgets.QScrollArea(self.patientsPageMainFrame)
        self.scrollArea_3.setStyleSheet("QScrollArea {\n"
"background: transparent;\n"
"border: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"background-color: transparent;\n"
"border: none;\n"
"border-top-left-radius: 10px;\n"
"border-bottom-left-radius: 10px;\n"
"}\n"
"\n"
"QLabel {\n"
"background-color: transparent;\n"
"font: 10pt \"Manrope\";\n"
"}\n"
"\n"
"#patients_name_label, #date_of_birth, #date_added_label {\n"
"background: transparent;\n"
"font: 12pt \"Manrope\";\n"
f"color: {themes['app_color']['context_color']};\n"
"}" + scrollBarStyle.format(scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"])
)
        self.scrollArea_3.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollArea_3.setObjectName("scrollArea_3")
        self.scrollAreaWidgetContents_3 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_3.setGeometry(QtCore.QRect(0, 0, 861, 233))
        self.scrollAreaWidgetContents_3.setObjectName("scrollAreaWidgetContents_3")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_4.setContentsMargins(30, 0, 0, 0)
        self.gridLayout_4.setHorizontalSpacing(0)
        self.gridLayout_4.setVerticalSpacing(20)
        self.gridLayout_4.setObjectName("gridLayout_4")
    
        # Headers
        self.patients_name_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.patients_name_label.setObjectName("patients_name_label")
        self.gridLayout_4.addWidget(self.patients_name_label, 0, 1, 1, 1)
        self.date_of_birth = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.date_of_birth.setObjectName("date_of_birth")
        self.gridLayout_4.addWidget(self.date_of_birth, 0, 2, 1, 1)
        self.date_added_label = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
        self.date_added_label.setAlignment(QtCore.Qt.AlignCenter)
        self.date_added_label.setObjectName("date_added_label")
        self.gridLayout_4.addWidget(self.date_added_label, 0, 4, 1, 1)


        # Patients
        patients = Database.get_patients()

        for idx, patient in enumerate(patients):

                self.patient_name = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
                self.patient_name.setObjectName("patient_name")
                self.gridLayout_4.addWidget(self.patient_name, 1 + (idx*1), 1, 1, 1)
                self.patient_name.setText(patient['name'])

                self.patient_avatar = QtWidgets.QPushButton(self.scrollAreaWidgetContents_3)
                self.patient_avatar.setMaximumSize(QtCore.QSize(70, 16777215))
                self.patient_avatar.setText("")
                self.patient_avatar.setIcon(icon_patient_male)
                self.patient_avatar.setIconSize(QSize(40,40))
                self.patient_avatar.setObjectName("patient_avatar")
                self.gridLayout_4.addWidget(self.patient_avatar, 1 + (idx*1), 0, 1, 1)

                self.patient_date_of_birth = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
                self.patient_date_of_birth.setObjectName("patient_date_of_birth")
                self.patient_date_of_birth.setText(patient['date_of_birth'])
                self.gridLayout_4.addWidget(self.patient_date_of_birth, 1 + (idx*1), 2, 1, 1)

                self.patient_date_added = QtWidgets.QLabel(self.scrollAreaWidgetContents_3)
                self.patient_date_added.setAlignment(QtCore.Qt.AlignCenter)
                self.patient_date_added.setObjectName("patient_date_added")
                self.patient_date_added.setText(patient['date_added'])
                self.gridLayout_4.addWidget(self.patient_date_added, 1 + (idx*1), 4, 1, 1)

                self.explore_button = QtWidgets.QPushButton()
                self.explore_button.setText("Explore")
                self.explore_button.setObjectName("explore_button")
                self.explore_button.clicked.connect(lambda x=None, patient=patient: self.showPatientsDetail(patient))
                set_stylesheet(self.explore_button, pushButtonStyle, 
                                radius=8,
                                color='#FFF',
                                bg_color=self.themes["app_color"]["dark_one"],
                                bg_color_hover=self.themes["app_color"]["dark_three"],
                                bg_color_pressed=self.themes["app_color"]["dark_four"]
                )
                self.explore_button.setMinimumSize(QSize(100, 30))
                self.explore_button.setMaximumSize(QSize(100, 30))

                self.gridLayout_4.addWidget(self.explore_button, 1 + (idx*1), 5, 1, 1)

                self.gridLayout_4.setColumnStretch(0, 2)
                self.scrollArea_3.setWidget(self.scrollAreaWidgetContents_3)
                self.verticalLayout_27.addWidget(self.scrollArea_3)
                self.ui.load_pages.page_3_layout.addWidget(self.patientsPageMainFrame, 1, Qt.AlignTop)

        _translate = QtCore.QCoreApplication.translate
        self.patients_name_label.setText(_translate("MainWindow", "Name"))
        self.date_of_birth.setText(_translate("MainWindow", "Date of Birth"))
        self.date_added_label.setText(_translate("MainWindow", "Date Added"))

        self.ui.load_pages.goBackToPatientstPageButton.clicked.connect(self.goBackToPatientsPage)
        icon = QIcon()
        icon.addFile(Functions.set_svg_icon('icon_arrow_left.svg'))
        self.ui.load_pages.goBackToPatientstPageButton.setIcon(icon)

        
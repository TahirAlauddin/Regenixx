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
from . functions_main_window import *
from widgets.py_table_widget_drag_rows import TableWidgetDragRows
from widgets.py_autocomplete_box import AutocompleteSearchBox

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT Utilities
# ///////////////////////////////////////////////////////////////
from utils import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import UI_MainWindow

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import MainFunctions


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:

    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)
        
    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon-diagnosis.svg",
            "btn_id" : "btn_diagnoses",
            "btn_text" : "Diagnoses",
            "btn_tooltip" : "Diagnoses",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon-patient.svg",
            "btn_id" : "btn_patients",
            "btn_text" : "Patients",
            "btn_tooltip" : "Patients",
            "show_top" : True,
            "is_active" : False
        },

    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_settings.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Settings",
            "is_active" : False
        },
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Settings Left Column",
            icon_path = Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # Main Page
        # ///////////////////////////////////////////////////////////////
        # Remove Image Allocation Limit
        QImageReader.setAllocationLimit(0)

        verticalScrollBar = self.ui.load_pages.scrollArea.verticalScrollBar()
        horizontalScrollBar = self.ui.load_pages.scrollArea.horizontalScrollBar()

        set_stylesheet(verticalScrollBar, scrollBarStyle,
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"])
        
        set_stylesheet(horizontalScrollBar, scrollBarStyle,
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"])
        
        self.mainTable = TableWidgetDragRows( 
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.goodTable = TableWidgetDragRows( 
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.goodTable.setColumnCount(2) #! Explicitly defining number of columns, may cause problem later
        self.goodTable.setHorizontalHeaderLabels(['Title', 'Cost',])
        header = self.goodTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

        self.discountLabelGoodTable = QLabel("Discount For Very Good Plan:")
        self.discountComboBoxGoodTable = QComboBox()
        discounts = ['5%', '10%', '15%', '20%']
        self.discountComboBoxGoodTable.addItems(discounts)
        set_stylesheet(self.discountComboBoxGoodTable, comboBoxStyle, 
                        radius = 8,
                        border_size = 2,
                        color = self.themes["app_color"]["text_foreground"],
                        selection_color = self.themes["app_color"]["white"],
                        bg_color = self.themes["app_color"]["dark_one"],
                        bg_color_active = self.themes["app_color"]["dark_three"],
                        context_color = self.themes["app_color"]["context_color"] )
        

        self.betterTable = TableWidgetDragRows( 
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.betterTable.setColumnCount(2) #! Explicitly defining number of columns, may cause problem later
        self.betterTable.setHorizontalHeaderLabels(['Title', 'Cost',])
        header = self.betterTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)


        self.discountLabelBetterTable = QLabel("Discount For Better Plan:")
        self.discountComboBoxBetterTable = QComboBox()
        discounts = ['5%', '10%', '15%', '20%']
        self.discountComboBoxBetterTable.addItems(discounts)
        set_stylesheet(self.discountComboBoxBetterTable, comboBoxStyle, 
                        radius = 8,
                        border_size = 2,
                        color = self.themes["app_color"]["text_foreground"],
                        selection_color = self.themes["app_color"]["white"],
                        bg_color = self.themes["app_color"]["dark_one"],
                        bg_color_active = self.themes["app_color"]["dark_three"],
                        context_color = self.themes["app_color"]["context_color"] )


        self.bestTable = TableWidgetDragRows( 
            radius = 8,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
        )
        self.bestTable.setColumnCount(2) #! Explicitly defining number of columns, may cause problem later
        self.bestTable.setHorizontalHeaderLabels(['Title', 'Cost',])
        header = self.bestTable.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeMode.ResizeToContents)

        
        self.discountLabelBestTable = QLabel("Discount For Best Plan:")
        self.discountComboBoxBestTable = QComboBox()
        discounts = ['5%', '10%', '15%', '20%']
        self.discountComboBoxBestTable.addItems(discounts)
        set_stylesheet(self.discountComboBoxBestTable, comboBoxStyle, 
                        radius = 8,
                        border_size = 2,
                        color = self.themes["app_color"]["text_foreground"],
                        selection_color = self.themes["app_color"]["white"],
                        bg_color = self.themes["app_color"]["dark_one"],
                        bg_color_active = self.themes["app_color"]["dark_three"],
                        context_color = self.themes["app_color"]["context_color"] )

        
        
        self.bestTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.betterTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.goodTable.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.bestTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.betterTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.goodTable.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)

        self.goodTableLabel = QLabel("Very Good")
        self.betterTableLabel = QLabel("Better")
        self.bestTableLabel = QLabel("Best")

        # Quotes
        self.goodTableLabel.setStyleSheet(f"font-size: 25px; color: #ddd")
        self.betterTableLabel.setStyleSheet(f"font-size: 25px; color: #ddd")
        self.bestTableLabel.setStyleSheet(f"font-size: 25px; color: #ddd")

        self.add_minus_btn_frame = QFrame()
        self.add_minus_btn_frame1 = QFrame()
        self.add_minus_btn_frame2 = QFrame()
        self.add_minus_btn_frame3 = QFrame()
        self.add_minus_btn_frame_layout1 = QHBoxLayout()
        self.add_minus_btn_frame_layout2 = QHBoxLayout()
        self.add_minus_btn_frame_layout3 = QHBoxLayout()
        self.add_minus_btn_frame1.setLayout(self.add_minus_btn_frame_layout1)
        self.add_minus_btn_frame2.setLayout(self.add_minus_btn_frame_layout2)
        self.add_minus_btn_frame3.setLayout(self.add_minus_btn_frame_layout3)
        self.add_minus_btn_out_layout = QHBoxLayout()

        self.add_minus_btn_out_layout.addWidget(self.add_minus_btn_frame1, 1, Qt.AlignRight)
        self.add_minus_btn_out_layout.addWidget(self.add_minus_btn_frame2, 1, Qt.AlignRight)
        self.add_minus_btn_out_layout.addWidget(self.add_minus_btn_frame3, 1, Qt.AlignRight)
        
        self.add_minus_btn_frame.setLayout(self.add_minus_btn_out_layout)

        # PLUS/MINUS Buttons
        self.addRowTableBtn = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-plus-yellow.png"))
        self.addRowTableBtn.setIcon(self.icon)
        self.addRowTableBtn.setIconSize(QSize(30,30))

        self.removeRowTableBtn = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-minus-yellow.png"))
        self.removeRowTableBtn.setIcon(self.icon)
        self.removeRowTableBtn.setIconSize(QSize(30,30))

        self.addRowTableBtn.clicked.connect   (lambda x: MainFunctions.addRow(self.bestTable))
        self.removeRowTableBtn.clicked.connect(lambda x: MainFunctions.removeRow(self.bestTable))


        self.addRowTableBtn2 = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-plus-yellow.png"))
        self.addRowTableBtn2.setIcon(self.icon)
        self.addRowTableBtn2.setIconSize(QSize(30,30))

        self.removeRowTableBtn2 = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-minus-yellow.png"))
        self.removeRowTableBtn2.setIcon(self.icon)
        self.removeRowTableBtn2.setIconSize(QSize(30,30))

        self.addRowTableBtn2.clicked.connect   (lambda x: MainFunctions.addRow(self.betterTable))
        self.removeRowTableBtn2.clicked.connect(lambda x: MainFunctions.removeRow(self.betterTable))

        self.addRowTableBtn3 = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-plus-yellow.png"))
        self.addRowTableBtn3.setIcon(self.icon)
        self.addRowTableBtn3.setIconSize(QSize(30,30))

        self.removeRowTableBtn3 = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-minus-yellow.png"))
        self.removeRowTableBtn3.setIcon(self.icon)
        self.removeRowTableBtn3.setIconSize(QSize(30,30))

        self.addRowTableBtn3.clicked.connect   (lambda x: MainFunctions.addRow(self.goodTable))
        self.removeRowTableBtn3.clicked.connect(lambda x: MainFunctions.removeRow(self.goodTable))

        self.add_minus_btn_frame_layout1.addWidget(self.addRowTableBtn)
        self.add_minus_btn_frame_layout1.addWidget(self.removeRowTableBtn)

        self.add_minus_btn_frame_layout2.addWidget(self.addRowTableBtn2)
        self.add_minus_btn_frame_layout2.addWidget(self.removeRowTableBtn2)

        self.add_minus_btn_frame_layout3.addWidget(self.addRowTableBtn3)
        self.add_minus_btn_frame_layout3.addWidget(self.removeRowTableBtn3)


        self.goodTableLabel.setAlignment(Qt.AlignCenter)
        self.betterTableLabel.setAlignment(Qt.AlignCenter)
        self.bestTableLabel.setAlignment(Qt.AlignCenter)
        self.goodTable.setMinimumHeight(250)
        self.mainTable.setMinimumSize(QSize(500,300))
        self.mainTable.setAcceptDrops(False)

        # Diagnosis section
        def addDiagnosisLineEdit():
            if len(self.diagnosesLineEdits) > 5:
                return
            diagnosisLineEdit = AutocompleteSearchBox(
                text = "",
                place_holder_text = "Diagnosis Description",
                radius = 8,
                border_size = 2,
                color = self.themes["app_color"]["text_foreground"],
                selection_color = self.themes["app_color"]["white"],
                bg_color = self.themes["app_color"]["dark_one"],
                bg_color_active = self.themes["app_color"]["dark_three"],
                context_color = self.themes["app_color"]["context_color"],
                items=MainFunctions.get_diagnosis_from_db()
            )
            self.diagnosisLayout.addWidget(diagnosisLineEdit)
            self.diagnosesLineEdits.append(diagnosisLineEdit)
        
        def removeDiagnosisLineEdit():
            if len(self.diagnosesLineEdits) > 1:
                diagnosisLineEdit = self.diagnosesLineEdits.pop()
                diagnosisLineEdit.close()
                self.diagnosisLayout.removeWidget(diagnosisLineEdit)
                
        self.diagnosisFrame = QFrame()
        self.diagnosisLayout = QHBoxLayout()
        self.diagnosisFrame.setLayout(self.diagnosisLayout)
        addDiagnosisLineEdit()

        self.diagnosisBtnFrame = QFrame()
        self.diagnosisBtnLayout = QHBoxLayout()
        self.diagnosisBtnFrame.setLayout(self.diagnosisBtnLayout)

        self.addDiagnosesBtn = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-plus-yellow.png"))
        self.addDiagnosesBtn.setIcon(self.icon)
        self.addDiagnosesBtn.setIconSize(QSize(30,30))
        self.addDiagnosesBtn.clicked.connect(addDiagnosisLineEdit)

        self.removeDiagnosesBtn = PyPushButton(
            text="",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color="transparent",
            bg_color_hover="transparent",
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.icon = QIcon(Functions.set_svg_icon("icon-minus-yellow.png"))
        self.removeDiagnosesBtn.setIcon(self.icon)
        self.removeDiagnosesBtn.setIconSize(QSize(30,30))
        self.removeDiagnosesBtn.clicked.connect(removeDiagnosisLineEdit)

        self.diagnosisBtnLayout.addWidget(self.addDiagnosesBtn)
        self.diagnosisBtnLayout.addWidget(self.removeDiagnosesBtn)
        # Diagnosis Section End

        self.patientsNameLineEdit = PyLineEdit(
            text = "",
            place_holder_text = "Patient's Name",
            radius = 8,
            border_size = 2,
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        )

        # Labels
        self.patientsDateOfBirthLabel = QLabel("Patient's Date of Birth:")
        self.uploadImagesLabel = QLabel("Upload Images")
        self.uploadImagesLabel.setAlignment(Qt.AlignCenter)
        self.uploadImagesLabel.setStyleSheet("font-size: 22px;")

        # Images Frame
        self.imagesFrame = QFrame()
        self.imagesFrame.setStyleSheet('QFrame { padding: 10px; }')
        self.imagesFrameLayout = QGridLayout()
        self.imagesFrameLayout.setColumnStretch(0, 1)
        self.imagesFrameLayout.setColumnStretch(1, 1)
        self.imagesFrameLayout.setColumnStretch(2, 1)
        self.imagesFrame.setLayout(self.imagesFrameLayout)

       
        def selectImage(self, label):
            file, _ = QFileDialog.getOpenFileName(self, 'Pdf Images', '.', 'Images (*.jpg;*.png;*jpeg)' )
            if file:
                MainFunctions.setImageForPixmap(label, 350, 280, file)

            if label == self.image1LabelPixmap:
                self.image_plan1 = file
            elif label == self.image2LabelPixmap:
                self.image_plan2 = file
            elif label == self.image3LabelPixmap:
                self.image_plan3 = file

        self.image1LabelPixmap = QLabel()
        self.image1Label = QLabel()
        self.image1Label.setText("Upload Image 1")
        self.image1LabelPixmap.setPixmap(QPixmap(Functions.set_svg_icon('icon-image-file-add')))
        self.imagesFrameLayout.addWidget(self.image1LabelPixmap, 0, 0, Qt.AlignHCenter)
        self.imagesFrameLayout.addWidget(self.image1Label, 1, 0, Qt.AlignHCenter)
        self.image1LabelPixmap.mousePressEvent = lambda x: selectImage(self, self.image1LabelPixmap)


        self.image2LabelPixmap = QLabel()
        self.image2Label = QLabel()
        self.image2Label.setText("Upload Image 2")
        self.image2LabelPixmap.setPixmap(QPixmap(Functions.set_svg_icon('icon-image-file-add')))
        self.imagesFrameLayout.addWidget(self.image2LabelPixmap, 0, 1, Qt.AlignHCenter)
        self.imagesFrameLayout.addWidget(self.image2Label, 1, 1, Qt.AlignHCenter)
        self.image2LabelPixmap.mousePressEvent = lambda x: selectImage(self, self.image2LabelPixmap)


        self.image3LabelPixmap = QLabel()
        self.image3Label = QLabel()
        self.image3Label.setText("Upload Image 3")
        self.image3LabelPixmap.setPixmap(QPixmap(Functions.set_svg_icon('icon-image-file-add')))
        self.imagesFrameLayout.addWidget(self.image3LabelPixmap, 0, 2, Qt.AlignHCenter)
        self.imagesFrameLayout.addWidget(self.image3Label, 1, 2, Qt.AlignHCenter)
        self.image3LabelPixmap.mousePressEvent = lambda x: selectImage(self, self.image3LabelPixmap)

        # DateEdit
        self.patientsDateOfBirth = QDateEdit()
        self.patientsDateOfBirth.setMaximumWidth(250)
        set_stylesheet(self.patientsDateOfBirth, dateEditStyle,
            border_size=2,
            radius=9,           
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["white"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_active = self.themes["app_color"]["dark_three"],
            context_color = self.themes["app_color"]["context_color"]
        
        )
        services, header = MainFunctions.get_services_from_excel(self)
        
        self.mainTable.setRowCount(len(services))
        self.mainTable.setColumnCount(len(services[0]))
        self.mainTable.setHorizontalHeaderLabels(header)


        mainTableHeader = self.mainTable.horizontalHeader()
        mainTableHeader.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
        mainTableHeader.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
        mainTableHeader.setSectionResizeMode(2, QHeaderView.ResizeMode.ResizeToContents)
        mainTableHeader.setSectionResizeMode(3, QHeaderView.ResizeMode.Stretch)

        for idx, service in enumerate(services):
            self.mainTable.setItem(idx, 0, QTableWidgetItem(service[0]))
            self.mainTable.setItem(idx, 1, QTableWidgetItem(service[1]))
            self.mainTable.setItem(idx, 2, QTableWidgetItem(service[2]))


        # Create PDF Button
        self.createPDFBtn = PyPushButton(
            text="Download Plan",
            radius=8,
            color='#FFF',
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.createPDFBtn.setMinimumSize(QSize(150,50))
        self.createPDFBtn.setMaximumWidth(200)
        self.createPDFBtn.clicked.connect(lambda x: MainFunctions.createPDF(self))

        # ADD WIDGETS
        SetupMainWindow.addWidgetToWindow(self)

        

        # RIGHT COLUMN
        self.changeExcelFileButton = PyPushButton(
            text="Change Excel File",
            radius=8,
            color='#FFF',
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        
        self.changeExcelFileButton.setMinimumSize(QSize(150,50))
        self.changeExcelFileButton.setMaximumWidth(200)
        self.changeExcelFileButton.clicked.connect(lambda x: MainFunctions.changeExcelFile(self))
        
        self.ui.right_column.verticalLayout.addWidget(self.changeExcelFileButton, 1, Qt.AlignBottom)



        from setup_patients_ui import setup_patients
        setup_patients(self)

        #//////////////////////////////////////////////////////////////////////////////////
        # UI SETUP END


    
    def removeCustomWidgetFromWindow(self):
        self.ui.load_pages.row_1_layout.removeWidget(self.mainTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.bestTableLabel)
        self.ui.load_pages.row_2_layout.removeWidget(self.betterTableLabel)
        self.ui.load_pages.row_2_layout.removeWidget(self.goodTableLabel)
        self.ui.load_pages.row_2_layout.removeWidget(self.bestTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.betterTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.goodTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.add_minus_btn_frame)
        for diagnosisLineEdit in self.diagnosesLineEdits:
            self.ui.load_pages.row_2_layout.removeWidget(diagnosisLineEdit)
        self.ui.load_pages.row_2_layout.removeWidget(self.patientsNameLineEdit)
        self.ui.load_pages.row_2_layout.removeWidget(self.discountComboBoxBestTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.discountComboBoxBetterTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.discountComboBoxGoodTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.discountLabelBestTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.discountLabelBetterTable)
        self.ui.load_pages.row_2_layout.removeWidget(self.discountLabelGoodTable)
        self.ui.load_pages.row_3_layout.removeWidget(self.patientsDateOfBirthLabel)
        self.ui.load_pages.row_3_layout.removeWidget(self.patientsDateOfBirth)
        self.ui.load_pages.row_3_layout.removeWidget(self.uploadImagesLabel)
        self.ui.load_pages.row_3_layout.removeWidget(self.imagesFrame)
        self.ui.load_pages.row_3_layout.removeWidget(self.createPDFBtn)


    def addWidgetToWindow(self):
        self.ui.load_pages.row_1_layout.addWidget(self.mainTable, 0)
        self.ui.load_pages.row_2_layout.addWidget(self.bestTableLabel, 0, 0)
        self.ui.load_pages.row_2_layout.addWidget(self.betterTableLabel, 0, 1)
        self.ui.load_pages.row_2_layout.addWidget(self.goodTableLabel, 0, 2)
        self.ui.load_pages.row_2_layout.addWidget(self.bestTable, 1, 0)
        self.ui.load_pages.row_2_layout.addWidget(self.betterTable, 1, 1)
        self.ui.load_pages.row_2_layout.addWidget(self.goodTable, 1, 2)

        self.ui.load_pages.row_2_layout.addWidget(self.discountComboBoxBestTable, 4, 0)
        self.ui.load_pages.row_2_layout.addWidget(self.discountComboBoxBetterTable, 4, 1)
        self.ui.load_pages.row_2_layout.addWidget(self.discountComboBoxGoodTable, 4, 2)

        self.ui.load_pages.row_2_layout.addWidget(self.discountLabelBestTable, 3, 0)
        self.ui.load_pages.row_2_layout.addWidget(self.discountLabelBetterTable, 3, 1)
        self.ui.load_pages.row_2_layout.addWidget(self.discountLabelGoodTable, 3, 2)
        
        self.ui.load_pages.row_2_layout.addWidget(self.add_minus_btn_frame, 2, 0, 1, 3)

    

        self.ui.load_pages.row_3_layout.addWidget(self.diagnosisFrame)
        self.ui.load_pages.row_3_layout.addWidget(self.diagnosisBtnFrame, 1, Qt.AlignRight)
        self.ui.load_pages.row_3_layout.addWidget(self.patientsNameLineEdit)
        self.ui.load_pages.row_3_layout.addWidget(self.patientsDateOfBirthLabel)
        self.ui.load_pages.row_3_layout.addWidget(self.patientsDateOfBirth)
        self.ui.load_pages.row_3_layout.addWidget(self.uploadImagesLabel)
        self.ui.load_pages.row_3_layout.addWidget(self.imagesFrame)
        self.ui.load_pages.row_3_layout.addWidget(self.createPDFBtn, 1, Qt.AlignHCenter)

        # Diagnosis Page 
        set_stylesheet(self.ui.load_pages.tableWidget, tableWidgetStyle + scrollBarStyle,
            radius=9,           
            color = self.themes["app_color"]["text_foreground"],
            selection_color = self.themes["app_color"]["context_color"],
            bg_color = self.themes["app_color"]["bg_two"],
            header_horizontal_color = self.themes["app_color"]["dark_two"],
            header_vertical_color = self.themes["app_color"]["bg_three"],
            bottom_line_color = self.themes["app_color"]["bg_three"],
            grid_line_color = self.themes["app_color"]["bg_one"],
            scroll_bar_bg_color = self.themes["app_color"]["bg_one"],
            scroll_bar_btn_color = self.themes["app_color"]["dark_four"],
            context_color = self.themes["app_color"]["context_color"]
            )

        set_stylesheet(self.ui.load_pages.addRowDiagnosisBtn, pushButtonStyle,
                    radius=8,
                    color=self.themes["app_color"]["text_foreground"],
                    bg_color="transparent",
                    bg_color_hover="transparent",
                    bg_color_pressed=self.themes["app_color"]["dark_four"],
        )
        
        set_stylesheet(self.ui.load_pages.removeRowDiagnosisBtn, pushButtonStyle,
                    radius=8,
                    color=self.themes["app_color"]["text_foreground"],
                    bg_color="transparent",
                    bg_color_hover="transparent",
                    bg_color_pressed=self.themes["app_color"]["dark_four"],
        )

        set_stylesheet(self.ui.load_pages.saveDiagnosisBtn, pushButtonStyle,
                    radius=8,
                    color=self.themes["app_color"]["text_foreground"],
                    bg_color=self.themes["app_color"]["dark_one"],
                    bg_color_hover=self.themes["app_color"]["dark_three"],
                    bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.ui.load_pages.saveDiagnosisBtn.setMinimumSize(QSize(100, 40))

        def addRowDiagnosis():
            rowCount = self.ui.load_pages.tableWidget.rowCount()
            self.ui.load_pages.tableWidget.setRowCount(rowCount + 1)
            lineEditId = QLineEdit()
            linedEditDiagnosis = QLineEdit()
            lineEditId.setStyleSheet("QLineEdit { color: white; }")
            linedEditDiagnosis.setStyleSheet("QLineEdit { color: white; }")

            self.ui.load_pages.tableWidget.setCellWidget(rowCount, 0, lineEditId)
            self.ui.load_pages.tableWidget.setCellWidget(rowCount, 1, linedEditDiagnosis)
        
        def removeRowDiagnosis():
            rows = [index.row() for index in self.ui.load_pages.tableWidget.selectedIndexes()]
            rows.sort()
            for idx, row in enumerate(rows):
                self.ui.load_pages.tableWidget.removeRow(row-idx)

            
        def saveDiagnosis():
            diagnoses = []
            for row in range(self.ui.load_pages.tableWidget.rowCount()):
                id = self.ui.load_pages.tableWidget.cellWidget(row, 0).text()
                diagnosis = self.ui.load_pages.tableWidget.cellWidget(row, 1).text()
                diagnoses.append([id, diagnosis])
            print(diagnoses)
            MainFunctions.update_diagnoses_in_db(diagnoses)

        self.icon = QIcon(Functions.set_svg_icon("icon-plus-yellow.png"))
        self.ui.load_pages.addRowDiagnosisBtn.setIcon(self.icon)
        self.ui.load_pages.addRowDiagnosisBtn.setIconSize(QSize(30,30))
        self.ui.load_pages.addRowDiagnosisBtn.clicked.connect(addRowDiagnosis)

        self.icon = QIcon(Functions.set_svg_icon("icon-minus-yellow.png"))
        self.ui.load_pages.removeRowDiagnosisBtn.setIcon(self.icon)
        self.ui.load_pages.removeRowDiagnosisBtn.setIconSize(QSize(30,30))
        self.ui.load_pages.removeRowDiagnosisBtn.clicked.connect(removeRowDiagnosis)

        self.ui.load_pages.tableWidget.setColumnCount(2)
        self.ui.load_pages.saveDiagnosisBtn.clicked.connect(saveDiagnosis)

        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////

        diagnoses = MainFunctions.list_diagnosis_from_db()

        if not diagnoses:
            diagnoses = []
        else:
            self.ui.load_pages.tableWidget.setRowCount(len(diagnoses))
            self.ui.load_pages.tableWidget.setColumnCount(len(diagnoses[0]))

            tableWidgetHeader = self.ui.load_pages.tableWidget.horizontalHeader()
            tableWidgetHeader.setSectionResizeMode(0, QHeaderView.ResizeMode.ResizeToContents)
            tableWidgetHeader.setSectionResizeMode(1, QHeaderView.ResizeMode.Stretch)
            self.ui.load_pages.tableWidget.setHorizontalHeaderLabels(['id', 'Diagnoses'])
        
        for idx, diagnosis in enumerate(diagnoses):
            lineEditId = QLineEdit(str(diagnosis[0]))
            linedEditDiagnosis = QLineEdit(diagnosis[1])
            lineEditId.setStyleSheet("QLineEdit { color: white; }")
            linedEditDiagnosis.setStyleSheet("QLineEdit { color: white; }")
            self.ui.load_pages.tableWidget.setCellWidget(idx, 0, lineEditId)
            self.ui.load_pages.tableWidget.setCellWidget(idx, 1, linedEditDiagnosis)


    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
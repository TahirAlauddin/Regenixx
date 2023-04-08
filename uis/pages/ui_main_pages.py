# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages2.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QPushButton, QScrollArea, QSizePolicy,
    QStackedWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        MainPages.setStyleSheet(u"* {\n"
"background: transparent;\n"
"}")
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.scrollArea = QScrollArea(self.page_1)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setStyleSheet(u"QScrollArea {\n"
"border: none;\n"
"}")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 832, 572))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_4.setSpacing(20)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.row_1_layout = QVBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout_4.addLayout(self.row_1_layout)

        self.row_2_layout = QGridLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout_4.addLayout(self.row_2_layout)

        self.row_3_layout = QVBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout_4.addLayout(self.row_3_layout)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.page_1_layout.addWidget(self.scrollArea)

        self.pages.addWidget(self.page_1)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.tableWidget = QTableWidget(self.page_2)
        self.tableWidget.setObjectName(u"tableWidget")

        self.page_2_layout.addWidget(self.tableWidget)

        self.frame = QFrame(self.page_2)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.addRowDiagnosisBtn = QPushButton(self.frame)
        self.addRowDiagnosisBtn.setObjectName(u"addRowDiagnosisBtn")

        self.horizontalLayout.addWidget(self.addRowDiagnosisBtn)

        self.removeRowDiagnosisBtn = QPushButton(self.frame)
        self.removeRowDiagnosisBtn.setObjectName(u"removeRowDiagnosisBtn")

        self.horizontalLayout.addWidget(self.removeRowDiagnosisBtn)

        self.saveDiagnosisBtn = QPushButton(self.frame)
        self.saveDiagnosisBtn.setObjectName(u"saveDiagnosisBtn")

        self.horizontalLayout.addWidget(self.saveDiagnosisBtn)


        self.page_2_layout.addWidget(self.frame, 0, Qt.AlignRight)

        self.pages.addWidget(self.page_2)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.addRowDiagnosisBtn.setText("")
        self.removeRowDiagnosisBtn.setText("")
        self.saveDiagnosisBtn.setText(QCoreApplication.translate("MainPages", u"SAVE", None))
    # retranslateUi


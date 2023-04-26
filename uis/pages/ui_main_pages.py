# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_pages.ui'
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
    QHeaderView, QLabel, QPushButton, QScrollArea,
    QSizePolicy, QSpacerItem, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 885)
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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 98, 64))
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
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.patientsPageMainFrame = QFrame(self.page_3)
        self.patientsPageMainFrame.setObjectName(u"patientsPageMainFrame")
        self.patientsPageMainFrame.setFrameShape(QFrame.StyledPanel)
        self.patientsPageMainFrame.setFrameShadow(QFrame.Raised)

        self.page_3_layout.addWidget(self.patientsPageMainFrame)

        self.pages.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.page_4.setStyleSheet(u"font: 75 12pt \"Manrope\";")
        self.verticalLayout = QVBoxLayout(self.page_4)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.goBackToPatientstPageButton = QPushButton(self.page_4)
        self.goBackToPatientstPageButton.setObjectName(u"goBackToPatientstPageButton")
        self.goBackToPatientstPageButton.setStyleSheet(u"font: 75 15pt \"Manrope\";\n"
"margin-left: 10px;")

        self.verticalLayout.addWidget(self.goBackToPatientstPageButton, 0, Qt.AlignLeft)

        self.page_4_scrollArea = QScrollArea(self.page_4)
        self.page_4_scrollArea.setObjectName(u"page_4_scrollArea")
        self.page_4_scrollArea.setStyleSheet(u"")
        self.page_4_scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 813, 849))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMaximumSize(QSize(16777215, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.logo_2 = QPushButton(self.frame_2)
        self.logo_2.setObjectName(u"logo_2")
        sizePolicy = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.logo_2.sizePolicy().hasHeightForWidth())
        self.logo_2.setSizePolicy(sizePolicy)
        icon = QIcon()
        icon.addFile(u"../../gui/images/svg_icons/icon-user-male.png", QSize(), QIcon.Normal, QIcon.Off)
        self.logo_2.setIcon(icon)
        self.logo_2.setIconSize(QSize(96, 90))

        self.horizontalLayout_2.addWidget(self.logo_2)

        self.patientNameLabel = QLabel(self.frame_2)
        self.patientNameLabel.setObjectName(u"patientNameLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.patientNameLabel.sizePolicy().hasHeightForWidth())
        self.patientNameLabel.setSizePolicy(sizePolicy1)
        self.patientNameLabel.setStyleSheet(u"font: 75 28pt \"Manrope\";")

        self.horizontalLayout_2.addWidget(self.patientNameLabel)

        self.patientDateAddedLabel = QPushButton(self.frame_2)
        self.patientDateAddedLabel.setObjectName(u"patientDateAddedLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.patientDateAddedLabel.sizePolicy().hasHeightForWidth())
        self.patientDateAddedLabel.setSizePolicy(sizePolicy2)
        icon1 = QIcon()
        icon1.addFile(u"../../../../../../Downloads/icons8-clock-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.patientDateAddedLabel.setIcon(icon1)

        self.horizontalLayout_2.addWidget(self.patientDateAddedLabel, 0, Qt.AlignLeft)

        self.deletePatientButton = QPushButton(self.frame_2)
        self.deletePatientButton.setObjectName(u"deletePatientButton")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.deletePatientButton.sizePolicy().hasHeightForWidth())
        self.deletePatientButton.setSizePolicy(sizePolicy3)
        self.deletePatientButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.deletePatientButton.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u"../../gui/images/svg_icons/icon-delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.deletePatientButton.setIcon(icon2)
        self.deletePatientButton.setIconSize(QSize(35, 35))

        self.horizontalLayout_2.addWidget(self.deletePatientButton)


        self.verticalLayout_2.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.scrollAreaWidgetContents_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_3)
        self.verticalLayout_3.setSpacing(30)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, -1, 0)
        self.patientDateOfBirthFrame = QFrame(self.frame_3)
        self.patientDateOfBirthFrame.setObjectName(u"patientDateOfBirthFrame")
        self.patientDateOfBirthFrame.setMaximumSize(QSize(16777215, 50))
        self.patientDateOfBirthFrame.setFrameShape(QFrame.StyledPanel)
        self.patientDateOfBirthFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.patientDateOfBirthFrame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(10, 0, 0, 20)
        self.patientDateOfBirthTagLabel = QLabel(self.patientDateOfBirthFrame)
        self.patientDateOfBirthTagLabel.setObjectName(u"patientDateOfBirthTagLabel")
        sizePolicy1.setHeightForWidth(self.patientDateOfBirthTagLabel.sizePolicy().hasHeightForWidth())
        self.patientDateOfBirthTagLabel.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setFamilies([u"Manrope"])
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        self.patientDateOfBirthTagLabel.setFont(font)
        self.patientDateOfBirthTagLabel.setStyleSheet(u"font: 75 14pt \"Manrope\";")

        self.horizontalLayout_3.addWidget(self.patientDateOfBirthTagLabel)

        self.patientDateOfBirth = QLabel(self.patientDateOfBirthFrame)
        self.patientDateOfBirth.setObjectName(u"patientDateOfBirth")

        self.horizontalLayout_3.addWidget(self.patientDateOfBirth)


        self.verticalLayout_3.addWidget(self.patientDateOfBirthFrame)

        self.plan1Frame = QFrame(self.frame_3)
        self.plan1Frame.setObjectName(u"plan1Frame")
        self.plan1Frame.setFrameShape(QFrame.StyledPanel)
        self.plan1Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.plan1Frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.plan1TagFrame = QFrame(self.plan1Frame)
        self.plan1TagFrame.setObjectName(u"plan1TagFrame")
        self.plan1TagFrame.setFrameShape(QFrame.StyledPanel)
        self.plan1TagFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.plan1TagFrame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.plan1TagLabel = QLabel(self.plan1TagFrame)
        self.plan1TagLabel.setObjectName(u"plan1TagLabel")
        sizePolicy1.setHeightForWidth(self.plan1TagLabel.sizePolicy().hasHeightForWidth())
        self.plan1TagLabel.setSizePolicy(sizePolicy1)
        self.plan1TagLabel.setStyleSheet(u"font: 18pt \"Manrope\";")

        self.horizontalLayout_4.addWidget(self.plan1TagLabel)

        self.plan1Discount = QLabel(self.plan1TagFrame)
        self.plan1Discount.setObjectName(u"plan1Discount")

        self.horizontalLayout_4.addWidget(self.plan1Discount, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.plan1TagFrame)

        self.plan1ServicesFrame = QFrame(self.plan1Frame)
        self.plan1ServicesFrame.setObjectName(u"plan1ServicesFrame")
        self.plan1ServicesFrame.setFrameShape(QFrame.StyledPanel)
        self.plan1ServicesFrame.setFrameShadow(QFrame.Raised)
        self.plan1ServicesVerticalLayout = QVBoxLayout(self.plan1ServicesFrame)
        self.plan1ServicesVerticalLayout.setObjectName(u"plan1ServicesVerticalLayout")

        self.verticalLayout_5.addWidget(self.plan1ServicesFrame)

        self.plan1PricingFrame = QFrame(self.plan1Frame)
        self.plan1PricingFrame.setObjectName(u"plan1PricingFrame")
        self.plan1PricingFrame.setFrameShape(QFrame.StyledPanel)
        self.plan1PricingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.plan1PricingFrame)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(-1, 0, -1, 0)
        self.plan1SubtotalFrame = QFrame(self.plan1PricingFrame)
        self.plan1SubtotalFrame.setObjectName(u"plan1SubtotalFrame")
        self.plan1SubtotalFrame.setFrameShape(QFrame.StyledPanel)
        self.plan1SubtotalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.plan1SubtotalFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(9, -1, -1, -1)
        self.label_4 = QLabel(self.plan1SubtotalFrame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_8.addWidget(self.label_4)

        self.plan1SubtotalAmount = QLabel(self.plan1SubtotalFrame)
        self.plan1SubtotalAmount.setObjectName(u"plan1SubtotalAmount")
        self.plan1SubtotalAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_8.addWidget(self.plan1SubtotalAmount)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer)


        self.verticalLayout_8.addWidget(self.plan1SubtotalFrame)

        self.plan1DiscountFrame = QFrame(self.plan1PricingFrame)
        self.plan1DiscountFrame.setObjectName(u"plan1DiscountFrame")
        self.plan1DiscountFrame.setFrameShape(QFrame.StyledPanel)
        self.plan1DiscountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.plan1DiscountFrame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_2 = QLabel(self.plan1DiscountFrame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_7.addWidget(self.label_2)

        self.plan1DiscountAmount = QLabel(self.plan1DiscountFrame)
        self.plan1DiscountAmount.setObjectName(u"plan1DiscountAmount")
        self.plan1DiscountAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_7.addWidget(self.plan1DiscountAmount)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_2)


        self.verticalLayout_8.addWidget(self.plan1DiscountFrame)

        self.plan1TotalFrame = QFrame(self.plan1PricingFrame)
        self.plan1TotalFrame.setObjectName(u"plan1TotalFrame")
        self.plan1TotalFrame.setFrameShape(QFrame.StyledPanel)
        self.plan1TotalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.plan1TotalFrame)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_6 = QLabel(self.plan1TotalFrame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_9.addWidget(self.label_6)

        self.plan1TotalAmount = QLabel(self.plan1TotalFrame)
        self.plan1TotalAmount.setObjectName(u"plan1TotalAmount")
        self.plan1TotalAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_9.addWidget(self.plan1TotalAmount)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_8.addWidget(self.plan1TotalFrame)


        self.verticalLayout_5.addWidget(self.plan1PricingFrame)


        self.verticalLayout_3.addWidget(self.plan1Frame)

        self.plan2Frame = QFrame(self.frame_3)
        self.plan2Frame.setObjectName(u"plan2Frame")
        self.plan2Frame.setFrameShape(QFrame.StyledPanel)
        self.plan2Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.plan2Frame)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.plan2TagFrame = QFrame(self.plan2Frame)
        self.plan2TagFrame.setObjectName(u"plan2TagFrame")
        self.plan2TagFrame.setFrameShape(QFrame.StyledPanel)
        self.plan2TagFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.plan2TagFrame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.plan2TagLabel = QLabel(self.plan2TagFrame)
        self.plan2TagLabel.setObjectName(u"plan2TagLabel")
        sizePolicy1.setHeightForWidth(self.plan2TagLabel.sizePolicy().hasHeightForWidth())
        self.plan2TagLabel.setSizePolicy(sizePolicy1)
        self.plan2TagLabel.setStyleSheet(u"font: 18pt \"Manrope\";")

        self.horizontalLayout_5.addWidget(self.plan2TagLabel)

        self.plan2Discount = QLabel(self.plan2TagFrame)
        self.plan2Discount.setObjectName(u"plan2Discount")

        self.horizontalLayout_5.addWidget(self.plan2Discount, 0, Qt.AlignTop)


        self.verticalLayout_6.addWidget(self.plan2TagFrame)

        self.plan2ServicesFrame = QFrame(self.plan2Frame)
        self.plan2ServicesFrame.setObjectName(u"plan2ServicesFrame")
        self.plan2ServicesFrame.setFrameShape(QFrame.StyledPanel)
        self.plan2ServicesFrame.setFrameShadow(QFrame.Raised)
        self.plan2ServicesVerticalLayout = QVBoxLayout(self.plan2ServicesFrame)
        self.plan2ServicesVerticalLayout.setObjectName(u"plan2ServicesVerticalLayout")

        self.verticalLayout_6.addWidget(self.plan2ServicesFrame)

        self.plan2PricingFrame = QFrame(self.plan2Frame)
        self.plan2PricingFrame.setObjectName(u"plan2PricingFrame")
        self.plan2PricingFrame.setFrameShape(QFrame.StyledPanel)
        self.plan2PricingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.plan2PricingFrame)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(-1, 0, -1, 0)
        self.plan2SubtotalFrame = QFrame(self.plan2PricingFrame)
        self.plan2SubtotalFrame.setObjectName(u"plan2SubtotalFrame")
        self.plan2SubtotalFrame.setFrameShape(QFrame.StyledPanel)
        self.plan2SubtotalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.plan2SubtotalFrame)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_8 = QLabel(self.plan2SubtotalFrame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_10.addWidget(self.label_8)

        self.plan2SubtotalAmount = QLabel(self.plan2SubtotalFrame)
        self.plan2SubtotalAmount.setObjectName(u"plan2SubtotalAmount")
        self.plan2SubtotalAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_10.addWidget(self.plan2SubtotalAmount)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_4)


        self.verticalLayout_9.addWidget(self.plan2SubtotalFrame)

        self.plan2DiscountFrame = QFrame(self.plan2PricingFrame)
        self.plan2DiscountFrame.setObjectName(u"plan2DiscountFrame")
        self.plan2DiscountFrame.setFrameShape(QFrame.StyledPanel)
        self.plan2DiscountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.plan2DiscountFrame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_12 = QLabel(self.plan2DiscountFrame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_12.addWidget(self.label_12)

        self.plan2DiscountAmount = QLabel(self.plan2DiscountFrame)
        self.plan2DiscountAmount.setObjectName(u"plan2DiscountAmount")
        self.plan2DiscountAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_12.addWidget(self.plan2DiscountAmount)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_12.addItem(self.horizontalSpacer_5)


        self.verticalLayout_9.addWidget(self.plan2DiscountFrame)

        self.plan2TotalFrame = QFrame(self.plan2PricingFrame)
        self.plan2TotalFrame.setObjectName(u"plan2TotalFrame")
        self.plan2TotalFrame.setFrameShape(QFrame.StyledPanel)
        self.plan2TotalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.plan2TotalFrame)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_10 = QLabel(self.plan2TotalFrame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_11.addWidget(self.label_10)

        self.plan2TotalAmount = QLabel(self.plan2TotalFrame)
        self.plan2TotalAmount.setObjectName(u"plan2TotalAmount")
        self.plan2TotalAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_11.addWidget(self.plan2TotalAmount)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_6)


        self.verticalLayout_9.addWidget(self.plan2TotalFrame)


        self.verticalLayout_6.addWidget(self.plan2PricingFrame)


        self.verticalLayout_3.addWidget(self.plan2Frame)

        self.plan3Frame = QFrame(self.frame_3)
        self.plan3Frame.setObjectName(u"plan3Frame")
        self.plan3Frame.setFrameShape(QFrame.StyledPanel)
        self.plan3Frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.plan3Frame)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.plan3TagFrame = QFrame(self.plan3Frame)
        self.plan3TagFrame.setObjectName(u"plan3TagFrame")
        self.plan3TagFrame.setFrameShape(QFrame.StyledPanel)
        self.plan3TagFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.plan3TagFrame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.plan3TagLabel = QLabel(self.plan3TagFrame)
        self.plan3TagLabel.setObjectName(u"plan3TagLabel")
        sizePolicy1.setHeightForWidth(self.plan3TagLabel.sizePolicy().hasHeightForWidth())
        self.plan3TagLabel.setSizePolicy(sizePolicy1)
        self.plan3TagLabel.setStyleSheet(u"font: 18pt \"Manrope\";")

        self.horizontalLayout_6.addWidget(self.plan3TagLabel)

        self.plan3Discount = QLabel(self.plan3TagFrame)
        self.plan3Discount.setObjectName(u"plan3Discount")

        self.horizontalLayout_6.addWidget(self.plan3Discount, 0, Qt.AlignTop)


        self.verticalLayout_7.addWidget(self.plan3TagFrame)

        self.plan3ServicesFrame = QFrame(self.plan3Frame)
        self.plan3ServicesFrame.setObjectName(u"plan3ServicesFrame")
        self.plan3ServicesFrame.setFrameShape(QFrame.StyledPanel)
        self.plan3ServicesFrame.setFrameShadow(QFrame.Raised)
        self.plan3ServicesVerticalLayout = QVBoxLayout(self.plan3ServicesFrame)
        self.plan3ServicesVerticalLayout.setObjectName(u"plan3ServicesVerticalLayout")

        self.verticalLayout_7.addWidget(self.plan3ServicesFrame)

        self.plan3PricingFrame = QFrame(self.plan3Frame)
        self.plan3PricingFrame.setObjectName(u"plan3PricingFrame")
        self.plan3PricingFrame.setFrameShape(QFrame.StyledPanel)
        self.plan3PricingFrame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.plan3PricingFrame)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(-1, 0, -1, 0)
        self.plan3SubtotalFrame = QFrame(self.plan3PricingFrame)
        self.plan3SubtotalFrame.setObjectName(u"plan3SubtotalFrame")
        self.plan3SubtotalFrame.setFrameShape(QFrame.StyledPanel)
        self.plan3SubtotalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.plan3SubtotalFrame)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_14 = QLabel(self.plan3SubtotalFrame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_13.addWidget(self.label_14)

        self.plan3SubtotalAmount = QLabel(self.plan3SubtotalFrame)
        self.plan3SubtotalAmount.setObjectName(u"plan3SubtotalAmount")
        self.plan3SubtotalAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_13.addWidget(self.plan3SubtotalAmount)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_13.addItem(self.horizontalSpacer_7)


        self.verticalLayout_10.addWidget(self.plan3SubtotalFrame)

        self.plan3DiscountFrame = QFrame(self.plan3PricingFrame)
        self.plan3DiscountFrame.setObjectName(u"plan3DiscountFrame")
        self.plan3DiscountFrame.setFrameShape(QFrame.StyledPanel)
        self.plan3DiscountFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.plan3DiscountFrame)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.label_18 = QLabel(self.plan3DiscountFrame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_15.addWidget(self.label_18)

        self.plan3DiscountAmount = QLabel(self.plan3DiscountFrame)
        self.plan3DiscountAmount.setObjectName(u"plan3DiscountAmount")
        self.plan3DiscountAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_15.addWidget(self.plan3DiscountAmount)

        self.horizontalSpacer_9 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_15.addItem(self.horizontalSpacer_9)


        self.verticalLayout_10.addWidget(self.plan3DiscountFrame)

        self.plan3TotalFrame = QFrame(self.plan3PricingFrame)
        self.plan3TotalFrame.setObjectName(u"plan3TotalFrame")
        self.plan3TotalFrame.setFrameShape(QFrame.StyledPanel)
        self.plan3TotalFrame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.plan3TotalFrame)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.label_16 = QLabel(self.plan3TotalFrame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setMinimumSize(QSize(700, 0))

        self.horizontalLayout_14.addWidget(self.label_16)

        self.plan3TotalAmount = QLabel(self.plan3TotalFrame)
        self.plan3TotalAmount.setObjectName(u"plan3TotalAmount")
        self.plan3TotalAmount.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_14.addWidget(self.plan3TotalAmount)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_14.addItem(self.horizontalSpacer_8)


        self.verticalLayout_10.addWidget(self.plan3TotalFrame)


        self.verticalLayout_7.addWidget(self.plan3PricingFrame)


        self.verticalLayout_3.addWidget(self.plan3Frame)


        self.verticalLayout_2.addWidget(self.frame_3)

        self.page_4_scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout.addWidget(self.page_4_scrollArea)

        self.pages.addWidget(self.page_4)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.addRowDiagnosisBtn.setText("")
        self.removeRowDiagnosisBtn.setText("")
        self.saveDiagnosisBtn.setText(QCoreApplication.translate("MainPages", u"SAVE", None))
        self.goBackToPatientstPageButton.setText(QCoreApplication.translate("MainPages", u"Back", None))
        self.logo_2.setText("")
        self.patientNameLabel.setText(QCoreApplication.translate("MainPages", u"John Doe", None))
        self.patientDateAddedLabel.setText(QCoreApplication.translate("MainPages", u"22/12/2001", None))
        self.deletePatientButton.setText("")
        self.patientDateOfBirthTagLabel.setText(QCoreApplication.translate("MainPages", u"Date of Birth: ", None))
        self.patientDateOfBirth.setText(QCoreApplication.translate("MainPages", u"22/12/2001", None))
        self.plan1TagLabel.setText(QCoreApplication.translate("MainPages", u"Plan1", None))
        self.plan1Discount.setText(QCoreApplication.translate("MainPages", u"20%", None))
        self.label_4.setText(QCoreApplication.translate("MainPages", u"Subtotal", None))
        self.plan1SubtotalAmount.setText(QCoreApplication.translate("MainPages", u"$5000", None))
        self.label_2.setText(QCoreApplication.translate("MainPages", u"Discount: ", None))
        self.plan1DiscountAmount.setText(QCoreApplication.translate("MainPages", u"$200", None))
        self.label_6.setText(QCoreApplication.translate("MainPages", u"Total:", None))
        self.plan1TotalAmount.setText(QCoreApplication.translate("MainPages", u"$4800", None))
        self.plan2TagLabel.setText(QCoreApplication.translate("MainPages", u"Plan2", None))
        self.plan2Discount.setText(QCoreApplication.translate("MainPages", u"20%", None))
        self.label_8.setText(QCoreApplication.translate("MainPages", u"Subtotal", None))
        self.plan2SubtotalAmount.setText(QCoreApplication.translate("MainPages", u"$5000", None))
        self.label_12.setText(QCoreApplication.translate("MainPages", u"Discount: ", None))
        self.plan2DiscountAmount.setText(QCoreApplication.translate("MainPages", u"$200", None))
        self.label_10.setText(QCoreApplication.translate("MainPages", u"Total:", None))
        self.plan2TotalAmount.setText(QCoreApplication.translate("MainPages", u"$4800", None))
        self.plan3TagLabel.setText(QCoreApplication.translate("MainPages", u"Plan3", None))
        self.plan3Discount.setText(QCoreApplication.translate("MainPages", u"20%", None))
        self.label_14.setText(QCoreApplication.translate("MainPages", u"Subtotal", None))
        self.plan3SubtotalAmount.setText(QCoreApplication.translate("MainPages", u"$5000", None))
        self.label_18.setText(QCoreApplication.translate("MainPages", u"Discount: ", None))
        self.plan3DiscountAmount.setText(QCoreApplication.translate("MainPages", u"$200", None))
        self.label_16.setText(QCoreApplication.translate("MainPages", u"Total:", None))
        self.plan3TotalAmount.setText(QCoreApplication.translate("MainPages", u"$4800", None))
    # retranslateUi


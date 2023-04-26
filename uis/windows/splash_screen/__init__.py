from qt_core import *
from uis.pages.ui_splash_screen import Ui_SplashScreen
from utils import *
from core.json_themes import Themes

themes = Themes().items

## ==> GLOBALS

# SPLASH SCREEN
class SplashScreen(QMainWindow):
    counter = 0
    smoothCounter = 0
    
    def __init__(self, parent):
        QMainWindow.__init__(self, parent=parent)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## REMOVE TITLE BAR
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO THE APPLICATION")

        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##


    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self, message):
        
        ## QTIMER ==> START
        self.timer = QTimer()
        self.timer.timeout.connect(self.progressSmooth)
        # # TIMER IN MILLISECONDS
        self.ui.progressBar.setValue(self.counter)
        self.timer.start(100)

        # SET DESCRIPTION
        if message:
            self.ui.label_description.setText(f"<strong>{message}</strong>")


        # CLOSE SPLASH SCREEN AND OPEN APP
        if self.counter >= 100:
            # RESET COUNTER
            self.counter = 0

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        self.counter += 10

    
    def progressSmooth(self):
        # SET VALUE TO PROGRESS BAR
        oldValue = self.ui.progressBar.value()
        self.ui.progressBar.setValue(oldValue + 1)

        # CLOSE SPLASH SCREEN AND OPEN APP
        if self.smoothCounter >= 10:
            # RESET COUNTER
            self.timer.stop()
            self.smoothCounter = 0

        # INCREASE COUNTER
        self.smoothCounter += 1

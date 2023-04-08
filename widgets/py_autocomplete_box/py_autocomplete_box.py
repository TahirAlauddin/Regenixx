from qt_core import *
import sys
from core.json_themes import Themes
sys.path.append(r'gui')
from widgets.py_line_edit import PyLineEdit


class CompleterStyle(QProxyStyle):
    def drawControl(self, element, option, painter, widget=None):
        if element == QProxyStyle.CE_ItemViewItem:
            # customize the background color and text color of the completer item
            if option.state & QProxyStyle.State_Selected:
                painter.fillRect(option.rect, QColor("#0078d7"))
                painter.setPen(QColor("#ffffff"))
            else:
                painter.fillRect(option.rect, QPalette().base())
                painter.setPen(QColor("#000000"))
        QProxyStyle.drawControl(self, element, option, painter, widget)


class AutocompleteSearchBox(PyLineEdit):
    
    def __init__(self, *args, items=None, **kwargs):
        super().__init__(*args, **kwargs)
        self.items = items
        if not self.items:
            self.items = []
        self.model = QStringListModel()
        self.model.setStringList(self.items)
        self.completer = QCompleter(self.model, self)
        self.setCompleter(self.completer)
        self.completer.setCaseSensitivity(Qt.CaseSensitivity.CaseInsensitive)
        self.completer.setFilterMode(Qt.MatchContains)
        
        self.themes = Themes().items

        # set the style on the completer
        completer_style_view = self.completer.popup()
        completer_style = f'font-size: 20px; background-color: {self.themes["app_color"]["dark_three"]};\
            color: {self.themes["app_color"]["text_foreground"]};'
        completer_style_view.setStyleSheet(completer_style)



if __name__ == '__main__':
    app = QApplication([])
    w = AutocompleteSearchBox()
    w.show()
    app.exec_()

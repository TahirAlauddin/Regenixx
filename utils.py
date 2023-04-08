pushButtonStyle = '''
QPushButton {{
	border: none;
    padding-left: 5px;
    padding-right: 5px;
    color: {color};
	border-radius: {radius};	
	background-color: {bg_color};
}}
QPushButton:hover {{
	background-color: {bg_color_hover};
}}
QPushButton:pressed {{	
	background-color: {bg_color_pressed};
}}
'''

scrollBarStyle = """

/* /////////////////////////////////////////////////////////////////////////////////////////////////
ScrollBars */
QScrollBar:horizontal {{
    border: none;
    background: {scroll_bar_bg_color};
    height: 8px;
    margin: 0px 21px 0 21px;
	border-radius: 0px;
}}
QScrollBar::handle:horizontal {{
    background: {context_color};
    min-width: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:horizontal {{
    border: none;
    background: {scroll_bar_btn_color};
    width: 20px;
	border-top-right-radius: 4px;
    border-bottom-right-radius: 4px;
    subcontrol-position: right;
    subcontrol-origin: margin;
}}
QScrollBar::sub-line:horizontal {{
    border: none;
    background: {scroll_bar_btn_color};
    width: 20px;
	border-top-left-radius: 4px;
    border-bottom-left-radius: 4px;
    subcontrol-position: left;
    subcontrol-origin: margin;
}}
QScrollBar::up-arrow:horizontal, QScrollBar::down-arrow:horizontal
{{
     background: none;
}}
QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal
{{
     background: none;
}}
QScrollBar:vertical {{
	border: none;
    background: {scroll_bar_bg_color};
    width: 8px;
    margin: 21px 0 21px 0;
	border-radius: 0px;
}}
QScrollBar::handle:vertical {{	
	background: {context_color};
    min-height: 25px;
	border-radius: 4px
}}
QScrollBar::add-line:vertical {{
     border: none;
    background: {scroll_bar_btn_color};
     height: 20px;
	border-bottom-left-radius: 4px;
    border-bottom-right-radius: 4px;
     subcontrol-position: bottom;
     subcontrol-origin: margin;
}}
QScrollBar::sub-line:vertical {{
	border: none;
    background: {scroll_bar_btn_color};
     height: 20px;
	border-top-left-radius: 4px;
    border-top-right-radius: 4px;
     subcontrol-position: top;
     subcontrol-origin: margin;
}}
QScrollBar::up-arrow:vertical, QScrollBar::down-arrow:vertical {{
     background: none;
}}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
     background: none;
}}
"""

lineEditStyle = '''
QLineEdit {{
	background-color: {bg_color};
	border-radius: {radius}px;
	border: {border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {selection_color};
	selection-background-color: {context_color};
    color: {color};
}}
QLineEdit:focus {{
	border: {border_size}px solid {context_color};
    background-color: {bg_color_active};
}}
'''

dateEditStyle = '''
QDateEdit {{
	background-color: {bg_color};
	border-radius: {radius}px;
	border: {border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {selection_color};
	selection-background-color: {context_color};
    color: {color};
}}
QDateEdit:focus {{
	border: {border_size}px solid {context_color};
    background-color: {bg_color_active};
}}

QDateEdit::up-button {{
    image: url('gui/images/svg_icons/collapse-arrow.png');
    padding-right: 5px;
}}
QDateEdit::down-button {{
    image: url('gui/images/svg_icons/expand-arrow.png');
	padding-right: 5px;
}}
'''

comboBoxStyle = '''
QComboBox {{
	background-color: {bg_color};
	border-radius: {radius}px;
	border: {border_size}px solid transparent;
	padding-left: 10px;
    padding-right: 10px;
	selection-color: {selection_color};
	selection-background-color: {context_color};
    color: {color};
}}
QComboBox:focus {{
	border: {border_size}px solid {context_color};
    background-color: {bg_color_active};
}}

QComboBox::down-arrow {{
image: url('gui/images/svg_icons/down-arrow.png');
padding-right: 20px;
width: 35px;
height: 20px;
}}

QComboBox::drop-down {{
border: none;
}}

'''

tableWidgetStyle = """
/* /////////////////////////////////////////////////////////////////////////////////////////////////
QTableWidget */

QTableWidget {{	
	background-color: {bg_color};
	padding: 5px;
	border-radius: {radius}px;
	gridline-color: {grid_line_color};
    color: {color};
}}
QTableWidget::item{{
	border-color: none;
	padding-left: 5px;
	padding-right: 5px;
	gridline-color: rgb(44, 49, 60);
    border-bottom: 1px solid {bottom_line_color};
}}
QTableWidget::item:selected{{
	background-color: {selection_color};
}}
QHeaderView::section{{
	background-color: rgb(33, 37, 43);
	max-width: 30px;
	border: 1px solid rgb(44, 49, 58);
	border-style: none;
    border-bottom: 1px solid rgb(44, 49, 60);
    border-right: 1px solid rgb(44, 49, 60);
}}
QTableWidget::horizontalHeader {{	
	background-color: rgb(33, 37, 43);
}}
QTableWidget QTableCornerButton::section {{
    border: none;
	background-color: {header_horizontal_color};
	padding: 3px;
    border-top-left-radius: {radius}px;
}}
QHeaderView::section:horizontal
{{
    border: none;
	background-color: {header_horizontal_color};
	padding: 3px;
}}
QHeaderView::section:vertical
{{
    border: none;
	background-color: {header_vertical_color};
	padding-left: 5px;
    padding-right: 5px;
    border-bottom: 1px solid {bottom_line_color};
    margin-bottom: 1px;
}}

"""


progressBarStyles = """QProgressBar {{\n"
	font: 10pt \"Roboto\";\n
	background-color: {bg_color};\n
	color: rgb(200, 200, 200);\n
	border-style: none;\n
	border-radius: 10px;\n
	text-align: center;\n
}}
QProgressBar::chunk{{
	border-radius: 10px;\n
	background-color: qlineargradient(spread:pad, x1:0, y1:0.511364, x2:1, y2:0.523, stop:0 {gradient_color_start}, stop:1 {gradient_color_stop});
}}"""

# SET STYLESHEET
def set_stylesheet(self, style='', **kwargs):
    # APPLY STYLESHEET
    style_format = style.format(**kwargs)
    self.setStyleSheet(style_format)
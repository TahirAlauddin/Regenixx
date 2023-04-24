import pickle
import sys
from qt_core import *
from widgets.py_table_widget import PyTableWidget

class MyMimeData(QMimeData):
    def __init__(self, row_data):
        super().__init__()
        self.row_data = row_data

    def formats(self):
        return ['text/plain']

    def hasFormat(self, mime_type):
        return mime_type in self.formats()

class TableWidgetDragRows(PyTableWidget):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.moving = False
        self.start_pos = None
        self.setDragEnabled(True)
        self.setAcceptDrops(True)
        self.setSelectionBehavior(QAbstractItemView.SelectRows)
        # self.setDragDropOverwriteMode(False)
        # self.setSelectionMode(QAbstractItemView.SingleSelection)

        self.last_drop_row = None

    def get_row_data(self, row_index):
        """
        Get the data for the given row index.

        Args:
            row_index (int): The index of the row to get data for.

        Returns:
            list: The data for the row as a list of strings.
        """
        data = []
        for col_index in range(self.columnCount()):
            item = self.item(row_index, col_index)
            if item is not None:
                data.append(item.text())
            else:
                data.append('')
        return data


    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton):
            return
        
        # Get the selected row
        selected_row = self.currentRow()
        selected_rows = self.selectedIndexes()
        selected_rows = list(set([model.row() for model in selected_rows]))
        mime_data = QMimeData()
        encoded_data = QByteArray()
        stream = QDataStream(encoded_data, QIODevice.WriteOnly)
        rows = []
        for selected_row in selected_rows:
            row = self.get_row_data(selected_row)
            rows.append(row)

        stream.writeBytes(pickle.dumps(rows))
        # Create the mime data for the drag-and-drop operation
        mime_data = QMimeData()
        mime_data.setData('application/x-qabstractitemmodeldatalist', encoded_data)
        drag = QDrag(self)
        drag.setMimeData(mime_data)
        drag.exec_()


    def dropEvent(self, event):
        if event.mimeData().hasFormat('application/x-qabstractitemmodeldatalist'):
            mime_data = event.mimeData()
            encoded_data = mime_data.data('application/x-qabstractitemmodeldatalist')
            stream = QDataStream(encoded_data, QIODevice.ReadOnly)
            while not stream.atEnd():
                rows = pickle.loads(stream.readBytes(0))
                old_row_count = self.rowCount()
                self.setRowCount(old_row_count + len(rows))
                self.setColumnCount(2) #! Hardcoding column count

                sender = event.source()
                self.setHorizontalHeaderLabels(['Title', 'Cost'])

                for row_idx, row in enumerate(rows):
                    column = self.columnCount()
                    row = row[1:3]
                    for column_idx, column in enumerate(row):
                        item = QTableWidgetItem(column)
                        self.setItem(row_idx+old_row_count, column_idx, item)
            event.accept()
        else:
            event.ignore()


    def getselectedRowsFast(self):
        selectedRows = []
        for item in self.selectedItems():
            if item.row() not in selectedRows:
                selectedRows.append(item.row())
        selectedRows.sort()
        return selectedRows


class ExampleDragDropTableWidgetWindow(QWidget):
    def __init__(self):
        super().__init__()

        layout = QHBoxLayout()
        self.setLayout(layout)

        self.table_widgets = []
        for _ in range(3):
            tw = TableWidgetDragRows()
            tw.setColumnCount(2)
            tw.setHorizontalHeaderLabels(['Colour', 'Model'])

            self.table_widgets.append(tw)
            layout.addWidget(tw)

        filled_widget = self.table_widgets[0]
        items = [('Red', 'Toyota'), ('Blue', 'RV'), ('Green', 'Beetle')]
        for i, (colour, model) in enumerate(items):
            c = QTableWidgetItem(colour)
            m = QTableWidgetItem(model)

            filled_widget.insertRow(filled_widget.rowCount())
            filled_widget.setItem(i, 0, c)
            filled_widget.setItem(i, 1, m)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ExampleDragDropTableWidgetWindow()
    window.show()
    sys.exit(app.exec_())


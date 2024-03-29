from PyQt5.QtWidgets import QApplication, QInputDialog
from PyQt5.QtWidgets import QMainWindow
from ui import Ui_MainWindow
import os

class Widget(QMainWindow):
    def   __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.add_note)

        if os.path.exists("note.json") and os.path.getsize("note.json"):
        with open("note.json", 'r') as file:
            self.notes = json.load(file)
            self.ui.listWidget.addItem(self.notes.keys())


    def add_note(self):
        text, ok = QInputDialog.getText(self, 'Додати замітку', 'введіть текст')
        if ok:
            self.ui.listWidget.addItem(text)


app = QApplication([])
ex = Widget()
ex.show()
app.exec_()
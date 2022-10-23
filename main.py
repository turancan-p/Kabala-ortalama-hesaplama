from PyQt5.QtWidgets import QApplication
from main_menu import MainMenu

app = QApplication([])

window = MainMenu()
window.show()
app.exec_()
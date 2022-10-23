from PyQt5.QtWidgets import *
from design.main_menu_design import Ui_MainWindow


class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

        self.main_menu.calculate_button.clicked.connect(self.calculate)


    def calculate(self):
        print(self.main_menu.first_kg_textbox.text())
        print(self.main_menu.second_kg_textbox.text())
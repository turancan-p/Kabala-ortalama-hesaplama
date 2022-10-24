from PyQt5.QtWidgets import *
from PyQt5.QtGui import QValidator, QIntValidator
from design.main_menu_design import Ui_MainWindow


class MainMenu(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.main_menu = Ui_MainWindow()
        self.main_menu.setupUi(self)

        self.onlyint = QIntValidator()
        self.onlyint.setRange(0, 99999)

        self.main_menu.calculate_button.clicked.connect(self.calculate)

        self.main_menu.first_kg_textbox.setValidator(self.onlyint)
        self.main_menu.second_kg_textbox.setValidator(self.onlyint)

        self.main_menu.first_kg_textbox.textChanged.connect(self.subtraction)
        self.main_menu.second_kg_textbox.textChanged.connect(self.subtraction)

        self.main_menu.first_customer_case_amount_textbox.setValidator(self.onlyint)
        self.main_menu.second_customer_case_amount_textbox.setValidator(self.onlyint)
        self.main_menu.third_customer_case_amount_textbox.setValidator(self.onlyint)
        self.main_menu.fourth_customer_case_amount_textbox.setValidator(self.onlyint)
        self.main_menu.fifth_customer_case_amount_textbox.setValidator(self.onlyint)

        self.main_menu.first_customer_case_amount_textbox.textChanged.connect(self.sum_case)
        self.main_menu.second_customer_case_amount_textbox.textChanged.connect(self.sum_case)
        self.main_menu.third_customer_case_amount_textbox.textChanged.connect(self.sum_case)
        self.main_menu.fourth_customer_case_amount_textbox.textChanged.connect(self.sum_case)
        self.main_menu.fifth_customer_case_amount_textbox.textChanged.connect(self.sum_case)

    def calculate(self):
        self.average_first_kg()
        self.average_second_kg()
        self.average_gross_kg()

        temp_first_kg = int(self.main_menu.first_kg_textbox.text())

        if int(self.main_menu.first_customer_case_amount_textbox.text()) > 0:
            self.first_customer_gross_kg = self.round_selected(self.multiple_kg(self.main_menu.per_case_average_textbox.text(), self.main_menu.first_customer_case_amount_textbox.text()))
            self.main_menu.first_customer_gross_kg_textbox.setText(str(self.first_customer_gross_kg))
            self.main_menu.first_customer_first_kg_textbox.setText(str(temp_first_kg))
            temp_second_kg = str(temp_first_kg - self.first_customer_gross_kg)
            self.main_menu.first_customer_second_kg_textbox.setText(temp_second_kg)

        if int(self.main_menu.second_customer_case_amount_textbox.text()) > 0:
            self.second_customer_gross_kg = self.round_selected(self.multiple_kg(self.main_menu.per_case_average_textbox.text(), self.main_menu.second_customer_case_amount_textbox.text()))
            self.main_menu.second_customer_gross_kg_textbox.setText(str(self.second_customer_gross_kg))
            temp_first_kg -= self.first_customer_gross_kg
            self.main_menu.second_customer_first_kg_textbox.setText(str(temp_first_kg))
            temp_second_kg = str(temp_first_kg - self.second_customer_gross_kg)
            self.main_menu.second_customer_second_kg_textbox.setText(temp_second_kg)

        if int(self.main_menu.third_customer_case_amount_textbox.text()) > 0:
            self.third_customer_gross_kg = self.round_selected(self.multiple_kg(self.main_menu.per_case_average_textbox.text(), self.main_menu.third_customer_case_amount_textbox.text()))
            self.main_menu.third_customer_gross_kg_textbox.setText(str(self.third_customer_gross_kg))
            temp_first_kg -= self.second_customer_gross_kg
            self.main_menu.third_customer_first_kg_textbox.setText(str(temp_first_kg))
            temp_second_kg = str(temp_first_kg - self.third_customer_gross_kg)
            self.main_menu.third_customer_second_kg_textbox.setText(temp_second_kg)

        if int(self.main_menu.fourth_customer_case_amount_textbox.text()) > 0:
            self.fourth_customer_gross_kg = self.round_selected(self.multiple_kg(self.main_menu.per_case_average_textbox.text(), self.main_menu.fourth_customer_case_amount_textbox.text()))
            self.main_menu.fourth_customer_gross_kg_textbox.setText(str(self.fourth_customer_gross_kg))
            temp_first_kg -= self.third_customer_gross_kg
            self.main_menu.fourth_customer_first_kg_textbox.setText(str(temp_first_kg))
            temp_second_kg = str(temp_first_kg - self.fourth_customer_gross_kg)
            self.main_menu.fourth_customer_second_kg_textbox.setText(temp_second_kg)

        if int(self.main_menu.fifth_customer_case_amount_textbox.text()) > 0:
            self.fifth_customer_gross_kg = self.round_selected(self.multiple_kg(self.main_menu.per_case_average_textbox.text(), self.main_menu.fifth_customer_case_amount_textbox.text()))
            self.main_menu.fifth_customer_gross_kg_textbox.setText(str(self.fifth_customer_gross_kg))
            temp_first_kg -= self.fourth_customer_gross_kg
            self.main_menu.fifth_customer_first_kg_textbox.setText(str(temp_first_kg))
            temp_second_kg = str(temp_first_kg - self.fifth_customer_gross_kg)
            self.main_menu.fifth_customer_second_kg_textbox.setText(temp_second_kg)

        self.sum_grosskg()


    def sum_grosskg(self):
        self.total_secondkg = (int(self.main_menu.first_customer_gross_kg_textbox.text()) +
                               int(self.main_menu.second_customer_gross_kg_textbox.text()) +
                               int(self.main_menu.third_customer_gross_kg_textbox.text()) +
                               int(self.main_menu.fourth_customer_gross_kg_textbox.text()) +
                               int(self.main_menu.fifth_customer_gross_kg_textbox.text()))

        self.main_menu.total_customer_gross_kg_textbox.setText(str(self.total_secondkg))

    def sum_case(self):
        self.total_case = (int(self.main_menu.first_customer_case_amount_textbox.text()) +
                           int(self.main_menu.second_customer_case_amount_textbox.text()) +
                           int(self.main_menu.third_customer_case_amount_textbox.text()) +
                           int(self.main_menu.fourth_customer_case_amount_textbox.text()) +
                           int(self.main_menu.fifth_customer_case_amount_textbox.text()))

        self.main_menu.total_customer_case_amount_textbox.setText(str(self.total_case))

    def subtraction(self):
        if self.main_menu.first_kg_textbox.text() == "":
            self.main_menu.first_kg_textbox.setText("0")
        elif self.main_menu.second_kg_textbox.text() == "":
            self.main_menu.second_kg_textbox.setText("0")
        else:
            self.gross_kg = (int(self.main_menu.first_kg_textbox.text()) - int(self.main_menu.second_kg_textbox.text()))
            self.main_menu.total_gross_kg_textbox.setText(str(self.gross_kg))

    def average_gross_kg(self):
        self.gross_average_kg = (int(self.main_menu.total_gross_kg_textbox.text()) /
                                 int(self.main_menu.total_customer_case_amount_textbox.text()))
        self.main_menu.per_case_average_textbox.setText(str(round(self.gross_average_kg, 4)))

    def average_first_kg(self):
        self.first_average_kg = (int(self.main_menu.first_kg_textbox.text()) /
                                 int(self.main_menu.total_customer_case_amount_textbox.text()))

    def average_second_kg(self):
        self.second_average_kg = (int(self.main_menu.second_kg_textbox.text()) /
                                  int(self.main_menu.total_customer_case_amount_textbox.text()))

    def round_selected(self, number):
        base = int(self.main_menu.comboBox.currentText())
        return int(base * round(float(number) / base))

    def multiple_kg(self, kg, case_amount):
        return float(float(kg) * int(case_amount))

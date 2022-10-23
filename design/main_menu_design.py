# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(812, 370)
        MainWindow.setMinimumSize(QtCore.QSize(812, 370))
        MainWindow.setMaximumSize(QtCore.QSize(812, 370))
        font = QtGui.QFont()
        font.setFamily("Microsoft JhengHei UI Light")
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icon.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(10, 10, 191, 91))
        self.groupBox_2.setObjectName("groupBox_2")
        self.formLayoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.formLayoutWidget.setGeometry(QtCore.QRect(9, 19, 171, 67))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 10, 0)
        self.formLayout.setSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.first_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.first_kg_textbox.setObjectName("first_kg_textbox")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.first_kg_textbox)
        self.second_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.second_kg_textbox.setObjectName("second_kg_textbox")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second_kg_textbox)
        self.groupBox_3 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_3.setGeometry(QtCore.QRect(10, 110, 191, 231))
        self.groupBox_3.setObjectName("groupBox_3")
        self.formLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_3)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 171, 201))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 10, 0)
        self.formLayout_2.setHorizontalSpacing(18)
        self.formLayout_2.setVerticalSpacing(10)
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.first_customer_case_amount_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.first_customer_case_amount_textbox.setObjectName("first_customer_case_amount_textbox")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.first_customer_case_amount_textbox)
        self.label_9 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.second_customer_case_amount_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.second_customer_case_amount_textbox.setObjectName("second_customer_case_amount_textbox")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second_customer_case_amount_textbox)
        self.label_10 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.third_customer_case_amount_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.third_customer_case_amount_textbox.setObjectName("third_customer_case_amount_textbox")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.third_customer_case_amount_textbox)
        self.label_11 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_11.setObjectName("label_11")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.fourth_customer_case_amount_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.fourth_customer_case_amount_textbox.setObjectName("fourth_customer_case_amount_textbox")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fourth_customer_case_amount_textbox)
        self.label_12 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.fifth_customer_case_amount_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.fifth_customer_case_amount_textbox.setObjectName("fifth_customer_case_amount_textbox")
        self.formLayout_2.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fifth_customer_case_amount_textbox)
        self.total_customer_case_amount_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_2)
        self.total_customer_case_amount_textbox.setReadOnly(True)
        self.total_customer_case_amount_textbox.setObjectName("total_customer_case_amount_textbox")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.total_customer_case_amount_textbox)
        self.label_18 = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_18.setObjectName("label_18")
        self.formLayout_2.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_18)
        self.groupBox_4 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_4.setGeometry(QtCore.QRect(210, 110, 191, 231))
        self.groupBox_4.setObjectName("groupBox_4")
        self.formLayoutWidget_3 = QtWidgets.QWidget(self.groupBox_4)
        self.formLayoutWidget_3.setGeometry(QtCore.QRect(10, 20, 171, 201))
        self.formLayoutWidget_3.setObjectName("formLayoutWidget_3")
        self.formLayout_3 = QtWidgets.QFormLayout(self.formLayoutWidget_3)
        self.formLayout_3.setContentsMargins(0, 0, 10, 0)
        self.formLayout_3.setHorizontalSpacing(18)
        self.formLayout_3.setVerticalSpacing(10)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_13 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.first_customer_first_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.first_customer_first_kg_textbox.setReadOnly(True)
        self.first_customer_first_kg_textbox.setObjectName("first_customer_first_kg_textbox")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.first_customer_first_kg_textbox)
        self.label_14 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.second_customer_first_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.second_customer_first_kg_textbox.setReadOnly(True)
        self.second_customer_first_kg_textbox.setObjectName("second_customer_first_kg_textbox")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second_customer_first_kg_textbox)
        self.label_15 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_15.setObjectName("label_15")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.third_customer_first_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.third_customer_first_kg_textbox.setReadOnly(True)
        self.third_customer_first_kg_textbox.setObjectName("third_customer_first_kg_textbox")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.third_customer_first_kg_textbox)
        self.label_16 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_16.setObjectName("label_16")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.fourth_customer_first_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.fourth_customer_first_kg_textbox.setReadOnly(True)
        self.fourth_customer_first_kg_textbox.setObjectName("fourth_customer_first_kg_textbox")
        self.formLayout_3.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fourth_customer_first_kg_textbox)
        self.label_17 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_17.setObjectName("label_17")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_17)
        self.fifth_customer_first_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.fifth_customer_first_kg_textbox.setReadOnly(True)
        self.fifth_customer_first_kg_textbox.setObjectName("fifth_customer_first_kg_textbox")
        self.formLayout_3.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fifth_customer_first_kg_textbox)
        self.total_customer_first_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_3)
        self.total_customer_first_kg_textbox.setReadOnly(True)
        self.total_customer_first_kg_textbox.setObjectName("total_customer_first_kg_textbox")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.total_customer_first_kg_textbox)
        self.label_19 = QtWidgets.QLabel(self.formLayoutWidget_3)
        self.label_19.setObjectName("label_19")
        self.formLayout_3.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_19)
        self.groupBox_5 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_5.setGeometry(QtCore.QRect(410, 110, 191, 231))
        self.groupBox_5.setObjectName("groupBox_5")
        self.formLayoutWidget_4 = QtWidgets.QWidget(self.groupBox_5)
        self.formLayoutWidget_4.setGeometry(QtCore.QRect(10, 20, 171, 201))
        self.formLayoutWidget_4.setObjectName("formLayoutWidget_4")
        self.formLayout_4 = QtWidgets.QFormLayout(self.formLayoutWidget_4)
        self.formLayout_4.setContentsMargins(0, 0, 10, 0)
        self.formLayout_4.setHorizontalSpacing(18)
        self.formLayout_4.setVerticalSpacing(10)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_20 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_20.setObjectName("label_20")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_20)
        self.first_customer_second_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.first_customer_second_kg_textbox.setReadOnly(True)
        self.first_customer_second_kg_textbox.setObjectName("first_customer_second_kg_textbox")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.first_customer_second_kg_textbox)
        self.label_21 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_21.setObjectName("label_21")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_21)
        self.second_customer_second_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.second_customer_second_kg_textbox.setReadOnly(True)
        self.second_customer_second_kg_textbox.setObjectName("second_customer_second_kg_textbox")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second_customer_second_kg_textbox)
        self.label_22 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_22.setObjectName("label_22")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_22)
        self.third_customer_second_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.third_customer_second_kg_textbox.setReadOnly(True)
        self.third_customer_second_kg_textbox.setObjectName("third_customer_second_kg_textbox")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.third_customer_second_kg_textbox)
        self.label_23 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_23.setObjectName("label_23")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_23)
        self.fourth_customer_second_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.fourth_customer_second_kg_textbox.setReadOnly(True)
        self.fourth_customer_second_kg_textbox.setObjectName("fourth_customer_second_kg_textbox")
        self.formLayout_4.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fourth_customer_second_kg_textbox)
        self.label_24 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_24.setObjectName("label_24")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_24)
        self.fifth_customer_second_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.fifth_customer_second_kg_textbox.setReadOnly(True)
        self.fifth_customer_second_kg_textbox.setObjectName("fifth_customer_second_kg_textbox")
        self.formLayout_4.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fifth_customer_second_kg_textbox)
        self.total_customer_second_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_4)
        self.total_customer_second_kg_textbox.setReadOnly(True)
        self.total_customer_second_kg_textbox.setObjectName("total_customer_second_kg_textbox")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.total_customer_second_kg_textbox)
        self.label_25 = QtWidgets.QLabel(self.formLayoutWidget_4)
        self.label_25.setObjectName("label_25")
        self.formLayout_4.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_25)
        self.groupBox_6 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_6.setGeometry(QtCore.QRect(610, 110, 191, 231))
        self.groupBox_6.setObjectName("groupBox_6")
        self.formLayoutWidget_5 = QtWidgets.QWidget(self.groupBox_6)
        self.formLayoutWidget_5.setGeometry(QtCore.QRect(10, 20, 171, 201))
        self.formLayoutWidget_5.setObjectName("formLayoutWidget_5")
        self.formLayout_5 = QtWidgets.QFormLayout(self.formLayoutWidget_5)
        self.formLayout_5.setContentsMargins(0, 0, 10, 0)
        self.formLayout_5.setHorizontalSpacing(18)
        self.formLayout_5.setVerticalSpacing(10)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_26 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_26.setObjectName("label_26")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_26)
        self.first_customer_gross_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.first_customer_gross_kg_textbox.setReadOnly(True)
        self.first_customer_gross_kg_textbox.setObjectName("first_customer_gross_kg_textbox")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.first_customer_gross_kg_textbox)
        self.label_27 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_27.setObjectName("label_27")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_27)
        self.second_customer_gross_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.second_customer_gross_kg_textbox.setReadOnly(True)
        self.second_customer_gross_kg_textbox.setObjectName("second_customer_gross_kg_textbox")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.second_customer_gross_kg_textbox)
        self.label_28 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_28.setObjectName("label_28")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_28)
        self.third_customer_gross_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.third_customer_gross_kg_textbox.setReadOnly(True)
        self.third_customer_gross_kg_textbox.setObjectName("third_customer_gross_kg_textbox")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.third_customer_gross_kg_textbox)
        self.label_29 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_29.setObjectName("label_29")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_29)
        self.fourth_customer_gross_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.fourth_customer_gross_kg_textbox.setReadOnly(True)
        self.fourth_customer_gross_kg_textbox.setObjectName("fourth_customer_gross_kg_textbox")
        self.formLayout_5.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.fourth_customer_gross_kg_textbox)
        self.label_30 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_30.setObjectName("label_30")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_30)
        self.fifth_customer_gross_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.fifth_customer_gross_kg_textbox.setReadOnly(True)
        self.fifth_customer_gross_kg_textbox.setObjectName("fifth_customer_gross_kg_textbox")
        self.formLayout_5.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fifth_customer_gross_kg_textbox)
        self.total_customer_gross_kg_textbox = QtWidgets.QLineEdit(self.formLayoutWidget_5)
        self.total_customer_gross_kg_textbox.setReadOnly(True)
        self.total_customer_gross_kg_textbox.setObjectName("total_customer_gross_kg_textbox")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.total_customer_gross_kg_textbox)
        self.label_31 = QtWidgets.QLabel(self.formLayoutWidget_5)
        self.label_31.setObjectName("label_31")
        self.formLayout_5.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_31)
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(210, 9, 191, 91))
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 171, 61))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.label_32 = QtWidgets.QLabel(self.gridLayoutWidget)
        self.label_32.setObjectName("label_32")
        self.gridLayout.addWidget(self.label_32, 0, 0, 1, 1)
        self.per_case_average_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget)
        self.per_case_average_textbox.setDragEnabled(False)
        self.per_case_average_textbox.setReadOnly(True)
        self.per_case_average_textbox.setObjectName("per_case_average_textbox")
        self.gridLayout.addWidget(self.per_case_average_textbox, 0, 1, 1, 1)
        self.groupBox_7 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_7.setGeometry(QtCore.QRect(410, 10, 191, 91))
        self.groupBox_7.setObjectName("groupBox_7")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox_7)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(10, 20, 171, 61))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_33 = QtWidgets.QLabel(self.gridLayoutWidget_2)
        self.label_33.setObjectName("label_33")
        self.gridLayout_2.addWidget(self.label_33, 0, 0, 1, 1)
        self.scale_precision_textbox = QtWidgets.QLineEdit(self.gridLayoutWidget_2)
        self.scale_precision_textbox.setObjectName("scale_precision_textbox")
        self.gridLayout_2.addWidget(self.scale_precision_textbox, 0, 1, 1, 1)
        self.calculate_button = QtWidgets.QPushButton(self.centralwidget)
        self.calculate_button.setGeometry(QtCore.QRect(610, 20, 191, 81))
        self.calculate_button.setObjectName("calculate_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 812, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ortalama Hesaplama"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Giriş / Çıkış Kiloları"))
        self.label_6.setText(_translate("MainWindow", "1. Tartım"))
        self.label_7.setText(_translate("MainWindow", "2. Tartım"))
        self.first_kg_textbox.setText(_translate("MainWindow", "0"))
        self.first_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.second_kg_textbox.setText(_translate("MainWindow", "0"))
        self.second_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Müstahsil Kasa Adetleri"))
        self.label_8.setText(_translate("MainWindow", "1. Kişi"))
        self.first_customer_case_amount_textbox.setText(_translate("MainWindow", "0"))
        self.first_customer_case_amount_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_9.setText(_translate("MainWindow", "2. Kişi"))
        self.second_customer_case_amount_textbox.setText(_translate("MainWindow", "0"))
        self.second_customer_case_amount_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_10.setText(_translate("MainWindow", "3. Kişi"))
        self.third_customer_case_amount_textbox.setText(_translate("MainWindow", "0"))
        self.third_customer_case_amount_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_11.setText(_translate("MainWindow", "4. Kişi"))
        self.fourth_customer_case_amount_textbox.setText(_translate("MainWindow", "0"))
        self.fourth_customer_case_amount_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_12.setText(_translate("MainWindow", "5. Kişi"))
        self.fifth_customer_case_amount_textbox.setText(_translate("MainWindow", "0"))
        self.fifth_customer_case_amount_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.total_customer_case_amount_textbox.setText(_translate("MainWindow", "0"))
        self.label_18.setText(_translate("MainWindow", "Toplam"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Kişilerin Giriş Kiloları"))
        self.label_13.setText(_translate("MainWindow", "1. Kişi"))
        self.first_customer_first_kg_textbox.setText(_translate("MainWindow", "0"))
        self.first_customer_first_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_14.setText(_translate("MainWindow", "2. Kişi"))
        self.second_customer_first_kg_textbox.setText(_translate("MainWindow", "0"))
        self.second_customer_first_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_15.setText(_translate("MainWindow", "3. Kişi"))
        self.third_customer_first_kg_textbox.setText(_translate("MainWindow", "0"))
        self.third_customer_first_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_16.setText(_translate("MainWindow", "4. Kişi"))
        self.fourth_customer_first_kg_textbox.setText(_translate("MainWindow", "0"))
        self.fourth_customer_first_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_17.setText(_translate("MainWindow", "5. Kişi"))
        self.fifth_customer_first_kg_textbox.setText(_translate("MainWindow", "0"))
        self.fifth_customer_first_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.total_customer_first_kg_textbox.setText(_translate("MainWindow", "0"))
        self.label_19.setText(_translate("MainWindow", "Toplam"))
        self.groupBox_5.setTitle(_translate("MainWindow", "Kişilerin Çıkış Kiloları"))
        self.label_20.setText(_translate("MainWindow", "1. Kişi"))
        self.first_customer_second_kg_textbox.setText(_translate("MainWindow", "0"))
        self.first_customer_second_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_21.setText(_translate("MainWindow", "2. Kişi"))
        self.second_customer_second_kg_textbox.setText(_translate("MainWindow", "0"))
        self.second_customer_second_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_22.setText(_translate("MainWindow", "3. Kişi"))
        self.third_customer_second_kg_textbox.setText(_translate("MainWindow", "0"))
        self.third_customer_second_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_23.setText(_translate("MainWindow", "4. Kişi"))
        self.fourth_customer_second_kg_textbox.setText(_translate("MainWindow", "0"))
        self.fourth_customer_second_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_24.setText(_translate("MainWindow", "5. Kişi"))
        self.fifth_customer_second_kg_textbox.setText(_translate("MainWindow", "0"))
        self.fifth_customer_second_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.total_customer_second_kg_textbox.setText(_translate("MainWindow", "0"))
        self.label_25.setText(_translate("MainWindow", "Toplam"))
        self.groupBox_6.setTitle(_translate("MainWindow", "Kişilerin Brüt Kiloları"))
        self.label_26.setText(_translate("MainWindow", "1. Kişi"))
        self.first_customer_gross_kg_textbox.setText(_translate("MainWindow", "0"))
        self.first_customer_gross_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_27.setText(_translate("MainWindow", "2. Kişi"))
        self.second_customer_gross_kg_textbox.setText(_translate("MainWindow", "0"))
        self.second_customer_gross_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_28.setText(_translate("MainWindow", "3. Kişi"))
        self.third_customer_gross_kg_textbox.setText(_translate("MainWindow", "0"))
        self.third_customer_gross_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_29.setText(_translate("MainWindow", "4. Kişi"))
        self.fourth_customer_gross_kg_textbox.setText(_translate("MainWindow", "0"))
        self.fourth_customer_gross_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.label_30.setText(_translate("MainWindow", "5. Kişi"))
        self.fifth_customer_gross_kg_textbox.setText(_translate("MainWindow", "0"))
        self.fifth_customer_gross_kg_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.total_customer_gross_kg_textbox.setText(_translate("MainWindow", "0"))
        self.label_31.setText(_translate("MainWindow", "Toplam"))
        self.groupBox.setTitle(_translate("MainWindow", "Detay"))
        self.label_32.setText(_translate("MainWindow", "Kasa Ortalaması"))
        self.per_case_average_textbox.setText(_translate("MainWindow", "0"))
        self.per_case_average_textbox.setPlaceholderText(_translate("MainWindow", "0"))
        self.groupBox_7.setTitle(_translate("MainWindow", "Kilo Ayarı"))
        self.label_33.setText(_translate("MainWindow", "Kantar Hassasiyeti"))
        self.scale_precision_textbox.setText(_translate("MainWindow", "20"))
        self.scale_precision_textbox.setPlaceholderText(_translate("MainWindow", "20"))
        self.calculate_button.setText(_translate("MainWindow", "Hesapla"))
from icons import icons_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_management.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(550, 435)
        font = QFont()
        font.setPointSize(12)
        Form.setFont(font)
        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 180, 111, 31))
        self.tableWidget = QTableWidget(Form)
        if (self.tableWidget.columnCount() < 5):
            self.tableWidget.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        font1 = QFont()
        font1.setPointSize(9)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(20, 220, 511, 192))
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 50, 141, 21))
        self.label_2.setFont(font)
        self.lineEdit_Username = QLineEdit(Form)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setGeometry(QRect(170, 50, 231, 21))
        self.lineEdit_Username.setFont(font)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 80, 141, 21))
        self.label_3.setFont(font)
        self.lineEdit_Pass = QLineEdit(Form)
        self.lineEdit_Pass.setObjectName(u"lineEdit_Pass")
        self.lineEdit_Pass.setGeometry(QRect(170, 80, 231, 21))
        self.lineEdit_Pass.setFont(font)
        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 140, 141, 16))
        self.label_4.setFont(font)
        self.checkBox_Activo = QCheckBox(Form)
        self.checkBox_Activo.setObjectName(u"checkBox_Activo")
        self.checkBox_Activo.setGeometry(QRect(170, 140, 21, 21))
        self.checkBox_Activo.setLayoutDirection(Qt.LeftToRight)
        self.checkBox_Activo.setIconSize(QSize(20, 20))
        self.pushButton_Guardar = QPushButton(Form)
        self.pushButton_Guardar.setObjectName(u"pushButton_Guardar")
        self.pushButton_Guardar.setGeometry(QRect(140, 180, 111, 31))
        self.lineEdit_Id = QLineEdit(Form)
        self.lineEdit_Id.setObjectName(u"lineEdit_Id")
        self.lineEdit_Id.setGeometry(QRect(170, 20, 231, 21))
        self.lineEdit_Id.setFont(font)
        self.lineEdit_Id.setReadOnly(True)
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 20, 141, 21))
        self.label_5.setFont(font)
        self.pushButton_Eliminar = QPushButton(Form)
        self.pushButton_Eliminar.setObjectName(u"pushButton_Eliminar")
        self.pushButton_Eliminar.setGeometry(QRect(260, 180, 111, 31))
        self.label_6 = QLabel(Form)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(20, 110, 141, 21))
        self.label_6.setFont(font)
        self.comboBox_Privilegio = QComboBox(Form)
        self.comboBox_Privilegio.addItem("")
        self.comboBox_Privilegio.addItem("")
        self.comboBox_Privilegio.setObjectName(u"comboBox_Privilegio")
        self.comboBox_Privilegio.setGeometry(QRect(170, 110, 231, 21))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Ver Usuarios", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Nombre de Usuario", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Privilegio", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Activo", None));
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre de Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"Activo", None))
        self.checkBox_Activo.setText("")
        self.pushButton_Guardar.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"ID", None))
        self.pushButton_Eliminar.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"Privilegio", None))
        self.comboBox_Privilegio.setItemText(0, QCoreApplication.translate("Form", u"Administrador", None))
        self.comboBox_Privilegio.setItemText(1, QCoreApplication.translate("Form", u"Usuario", None))

    # retranslateUi


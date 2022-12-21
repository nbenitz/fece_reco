# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 185)
        Form.setStyleSheet(u"background-color: rgb(64, 65, 66);\n"
"color: rgb(255, 255, 255);")
        self.lineEdit_Username = QLineEdit(Form)
        self.lineEdit_Username.setObjectName(u"lineEdit_Username")
        self.lineEdit_Username.setGeometry(QRect(180, 40, 181, 22))
        font = QFont()
        font.setPointSize(12)
        self.lineEdit_Username.setFont(font)
        self.lineEdit_Username.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 40, 141, 16))
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_Pass = QLineEdit(Form)
        self.lineEdit_Pass.setObjectName(u"lineEdit_Pass")
        self.lineEdit_Pass.setGeometry(QRect(180, 80, 181, 22))
        self.lineEdit_Pass.setFont(font)
        self.lineEdit_Pass.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.lineEdit_Pass.setEchoMode(QLineEdit.Password)
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(30, 80, 141, 16))
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.pushButton_Login = QPushButton(Form)
        self.pushButton_Login.setObjectName(u"pushButton_Login")
        self.pushButton_Login.setGeometry(QRect(240, 120, 121, 31))
        self.pushButton_Login.setFont(font)
        self.pushButton_Login.setStyleSheet(u"background-color: rgb(67, 134, 0);\n"
"color: rgb(255, 255, 255);")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Nombre de Usuario", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"Contrase\u00f1a", None))
        self.pushButton_Login.setText(QCoreApplication.translate("Form", u"Iniciar Sesi\u00f3n", None))
    # retranslateUi


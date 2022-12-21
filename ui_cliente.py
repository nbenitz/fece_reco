# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cliente.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QCheckBox, QHeaderView,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(658, 413)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 661, 411))
        self.tabBuscarCliente = QWidget()
        self.tabBuscarCliente.setObjectName(u"tabBuscarCliente")
        self.tableWidget = QTableWidget(self.tabBuscarCliente)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        font = QFont()
        font.setPointSize(9)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 50, 631, 281))
        self.tableWidget.setSelectionMode(QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.verticalHeader().setVisible(False)
        self.btnEliminar = QPushButton(self.tabBuscarCliente)
        self.btnEliminar.setObjectName(u"btnEliminar")
        self.btnEliminar.setGeometry(QRect(130, 340, 111, 31))
        self.btnEditar = QPushButton(self.tabBuscarCliente)
        self.btnEditar.setObjectName(u"btnEditar")
        self.btnEditar.setGeometry(QRect(10, 340, 111, 31))
        self.txtBuscar = QLineEdit(self.tabBuscarCliente)
        self.txtBuscar.setObjectName(u"txtBuscar")
        self.txtBuscar.setGeometry(QRect(10, 10, 201, 31))
        font1 = QFont()
        font1.setPointSize(12)
        self.txtBuscar.setFont(font1)
        self.txtBuscar.setReadOnly(False)
        self.btnBuscar = QPushButton(self.tabBuscarCliente)
        self.btnBuscar.setObjectName(u"btnBuscar")
        self.btnBuscar.setGeometry(QRect(220, 10, 111, 31))
        self.tabWidget.addTab(self.tabBuscarCliente, "")
        self.tabNuevoCliente = QWidget()
        self.tabNuevoCliente.setObjectName(u"tabNuevoCliente")
        self.lblActivo = QLabel(self.tabNuevoCliente)
        self.lblActivo.setObjectName(u"lblActivo")
        self.lblActivo.setGeometry(QRect(130, 250, 61, 16))
        self.lblActivo.setFont(font1)
        self.label_3 = QLabel(self.tabNuevoCliente)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(130, 130, 71, 21))
        self.label_3.setFont(font1)
        self.label_6 = QLabel(self.tabNuevoCliente)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(130, 160, 71, 21))
        self.label_6.setFont(font1)
        self.lblId = QLabel(self.tabNuevoCliente)
        self.lblId.setObjectName(u"lblId")
        self.lblId.setGeometry(QRect(130, 70, 81, 21))
        self.lblId.setFont(font1)
        self.txtNombre = QLineEdit(self.tabNuevoCliente)
        self.txtNombre.setObjectName(u"txtNombre")
        self.txtNombre.setGeometry(QRect(220, 130, 231, 21))
        self.txtNombre.setFont(font1)
        self.txtCI = QLineEdit(self.tabNuevoCliente)
        self.txtCI.setObjectName(u"txtCI")
        self.txtCI.setGeometry(QRect(220, 100, 231, 21))
        self.txtCI.setFont(font1)
        self.txtId = QLineEdit(self.tabNuevoCliente)
        self.txtId.setObjectName(u"txtId")
        self.txtId.setGeometry(QRect(220, 70, 231, 21))
        self.txtId.setFont(font1)
        self.txtId.setReadOnly(True)
        self.label_2 = QLabel(self.tabNuevoCliente)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 100, 71, 21))
        self.label_2.setFont(font1)
        self.chkActivo = QCheckBox(self.tabNuevoCliente)
        self.chkActivo.setObjectName(u"chkActivo")
        self.chkActivo.setGeometry(QRect(220, 250, 21, 21))
        self.chkActivo.setLayoutDirection(Qt.LeftToRight)
        self.chkActivo.setIconSize(QSize(20, 20))
        self.txtApellido = QLineEdit(self.tabNuevoCliente)
        self.txtApellido.setObjectName(u"txtApellido")
        self.txtApellido.setGeometry(QRect(220, 160, 231, 21))
        self.txtApellido.setFont(font1)
        self.txtTelefono = QLineEdit(self.tabNuevoCliente)
        self.txtTelefono.setObjectName(u"txtTelefono")
        self.txtTelefono.setGeometry(QRect(220, 190, 231, 21))
        self.txtTelefono.setFont(font1)
        self.label_7 = QLabel(self.tabNuevoCliente)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(130, 190, 71, 21))
        self.label_7.setFont(font1)
        self.txtDireccion = QLineEdit(self.tabNuevoCliente)
        self.txtDireccion.setObjectName(u"txtDireccion")
        self.txtDireccion.setGeometry(QRect(220, 220, 231, 21))
        self.txtDireccion.setFont(font1)
        self.label_8 = QLabel(self.tabNuevoCliente)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(130, 220, 81, 21))
        self.label_8.setFont(font1)
        self.btnGuardar = QPushButton(self.tabNuevoCliente)
        self.btnGuardar.setObjectName(u"btnGuardar")
        self.btnGuardar.setGeometry(QRect(220, 290, 111, 31))
        self.btnCancelar = QPushButton(self.tabNuevoCliente)
        self.btnCancelar.setObjectName(u"btnCancelar")
        self.btnCancelar.setGeometry(QRect(340, 290, 111, 31))
        self.tabWidget.addTab(self.tabNuevoCliente, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"CI", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Nombre", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Apellido", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"Tel\u00e9fono", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"Direcci\u00f3n", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"Activo", None));
        self.btnEliminar.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.btnEditar.setText(QCoreApplication.translate("Form", u"Editar", None))
        self.btnBuscar.setText(QCoreApplication.translate("Form", u"Buscar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabBuscarCliente), QCoreApplication.translate("Form", u"Buscar Clientes", None))
        self.lblActivo.setText(QCoreApplication.translate("Form", u"Activo", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Nombre</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Apellido</p></body></html>", None))
        self.lblId.setText(QCoreApplication.translate("Form", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>C.I. Nro.</p></body></html>", None))
        self.chkActivo.setText("")
        self.label_7.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Tel\u00e9fono</p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"<html><head/><body><p>Direcci\u00f3n</p></body></html>", None))
        self.btnGuardar.setText(QCoreApplication.translate("Form", u"Guardar", None))
        self.btnCancelar.setText(QCoreApplication.translate("Form", u"Cancelar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNuevoCliente), QCoreApplication.translate("Form", u"Nuevo Cliente", None))
    # retranslateUi


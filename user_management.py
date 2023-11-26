# This Python file uses the following encoding: utf-8
#from PyQt5 import QtCore
from PyQt5 import QtWidgets, uic
import conndb


class UserManagement(QtWidgets.QWidget):

    def __init__(self):
        super(UserManagement, self).__init__()
        uic.loadUi("user_management.ui", self)
        self.setWindowTitle("Gestión de Usuarios")

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)

        self.pushButton.clicked.connect(self.load_data)
        self.pushButton_Guardar.clicked.connect(self.save_data)
        self.pushButton_Eliminar.clicked.connect(self.delet_data)
        self.tableWidget.clicked.connect(self.get_item)
        self.load_data()

    def load_data(self):
        """ función para cargar los datos del uruario en la tabla """
        conn = conndb.conndb()
        strsql = "SELECT * FROM usuario"
        result = conn.queryResult(strsql)
        row = 0
        self.tableWidget.setRowCount(len(result))
        for user in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(user[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(user[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(user[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(user[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(str(user[4])))
            row = row + 1

    def save_data(self):
        """ función para actualizar los datos del usuario seleccionado """
        id = self.lineEdit_Id.text()
        username = self.lineEdit_Username.text()
        password = self.lineEdit_Pass.text()
        privilegio = self.comboBox_Privilegio.currentText()
        activo = int(self.checkBox_Activo.isChecked())
        strsql = "UPDATE usuario SET nombre='{}', pass='{}', privilegio='{}', activo='{}' WHERE id='{}'".format(
            username,
            password,
            privilegio,
            activo,
            id)

        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.load_data()

    def delet_data(self):
        """ funcion para eliminar los datos del usuario seleccionado """
        id = self.lineEdit_Id.text()
        strsql = "DELETE FROM usuario WHERE id='"+id+"'"
        conn = conndb.conndb()
        conn.queryExecute(strsql)
        self.load_data()

    def get_item(self):
        """ funcion para mostrar en las cajas de texto los datos del usuario seleccionado de la tabla """
        row = self.tableWidget.currentRow()

        rowItemId = self.tableWidget.item(row, 0).text()
        rowItemUsername = self.tableWidget.item(row, 1).text()
        rowItemPass = self.tableWidget.item(row, 2).text()
        rowItemPriv = self.tableWidget.item(row, 3).text()
        rowItemActivo = self.tableWidget.item(row, 4).text()

        self.lineEdit_Id.setText(str(rowItemId))
        self.lineEdit_Username.setText(rowItemUsername)
        self.lineEdit_Pass.setText(rowItemPass)
        self.comboBox_Privilegio.setCurrentText(rowItemPriv)
        self.checkBox_Activo.setChecked(int(rowItemActivo))



# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox
import conndb


class cliente(QtWidgets.QWidget):
    def __init__(self):
        super(cliente, self).__init__()
        uic.loadUi("cliente.ui", self)
        self.setWindowTitle("Gestión de Clientes")

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        self.btnEditar.clicked.connect(self.getItem)
        self.btnGuardar.clicked.connect(self.updateData)
        self.btnEliminar.clicked.connect(self.deleteData)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tabWidget.tabBarClicked.connect(self.tab_clicked)

        self.loadData()
        self.tabWidget.setCurrentIndex(0)



    def loadData(self):     # función para cargar los datos del uruario en la tabla
        conn = conndb.conndb()
        strsql = "SELECT * FROM cliente"
        result = conn.queryResult(strsql)
        row = 0
        self.tableWidget.setRowCount(len(result))
        for r in result:
            self.tableWidget.setItem(row, 0, QtWidgets.QTableWidgetItem(str(r[0])))
            self.tableWidget.setItem(row, 1, QtWidgets.QTableWidgetItem(r[1]))
            self.tableWidget.setItem(row, 2, QtWidgets.QTableWidgetItem(r[2]))
            self.tableWidget.setItem(row, 3, QtWidgets.QTableWidgetItem(r[3]))
            self.tableWidget.setItem(row, 4, QtWidgets.QTableWidgetItem(r[4]))
            self.tableWidget.setItem(row, 5, QtWidgets.QTableWidgetItem(r[5]))
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(str(r[6])))
            row = row + 1

    # función para actualizar los datos del usuario seleccionado
    def updateData(self):
        if self.tabWidget.tabText(1) == "Editar Cliente":
            id = self.txtId.text()
            ci = self.txtCI.text()
            nombre = self.txtNombre.text()
            apellido = self.txtApellido.text()
            telefono = self.txtTelefono.text()
            direccion = self.txtDireccion.text()
            activo = int(self.chkActivo.isChecked())
            strsql = "UPDATE cliente SET ci='{}', nombre='{}', apellido='{}', telefono='{}', direccion='{}', activo='{}' WHERE id='{}'".format(
                ci,
                nombre,
                apellido,
                telefono,
                direccion,
                activo,
                id)

            conn = conndb.conndb()
            try:
                conn.queryExecute(strsql)
                QMessageBox.about(self, "Editar Cliente", "Los datos del cliente se actualizaron correctamente")
                self.tabWidget.setTabText(1, "Nuevo Cliente")
                # mostrar la pestaña 0 (lista de clientes)
                self.tabWidget.setCurrentIndex(0)
                self.loadData()
            except:
                QMessageBox.about(self, "Error", "Hubo un error al actualizar los datos del cliente")


    # función para actualizar los datos del usuario seleccionado
    def saveData(self):
        if self.tabWidget.tabText(1) == "Nuevo Cliente":
            ci = self.txtCI.text()
            nombre = self.txtNombre.text()
            apellido = self.txtApellido.text()
            telefono = self.txtTelefono.text()
            direccion = self.txtDireccion.text()
            strsql = "INSERT INTO cliente (ci, nombre, apellido, telefono, direccion) VALUES('{}', '{}', '{}', '{}', '{}')".format(
                ci,
                nombre,
                apellido,
                telefono,
                direccion)

            conn = conndb.conndb()
            try:
                conn.queryExecute(strsql)
                QMessageBox.about(self, "Nuevo Cliente", "Los datos del cliente se guardaron correctamente")
                # mostrar la pestaña 0 (lista de clientes)
                self.tabWidget.setCurrentIndex(0)
                self.loadData()
            except:
                QMessageBox.about(self, "Error", "Hubo un error al guardar los datos del cliente")


    def deleteData(self):    # funcion para eliminar los datos del usuario seleccionado
        # capturar la fila seleccionada
        row = self.tableWidget.currentRow()

        if row >= 0:
        # capturar los datos de cada celda de la fila seleccionada y guardar en varuables
            id = self.tableWidget.item(row, 0).text()
            strsql = "DELETE FROM cliente WHERE id='"+id+"'"
            conn = conndb.conndb()
            conn.queryExecute(strsql)
            QMessageBox.about(self, "Eliminar Cliente", "Cliente eliminado correctamente")
            self.loadData()


    # funcion para mostrar en las cajas de texto los datos del usuario seleccionado de la tabla
    def getItem(self):
        # capturar la fila seleccionada
        row = self.tableWidget.currentRow()

        # si se seleccionó alguna fila de la tabla
        if row >= 0:
        # capturar los datos de cada celda de la fila seleccionada y guardar en varuables
            id = self.tableWidget.item(row, 0).text()
            ci = self.tableWidget.item(row, 1).text()
            nombre = self.tableWidget.item(row, 2).text()
            apellido = self.tableWidget.item(row, 3).text()
            telefono = self.tableWidget.item(row, 4).text()
            direccion = self.tableWidget.item(row, 5).text()
            activo = self.tableWidget.item(row, 6).text()

            # cargar las cajas de texto con los datos del cliente
            self.txtId.setText(str(id))
            self.txtCI.setText(ci)
            self.txtNombre.setText(nombre)
            self.txtApellido.setText(apellido)
            self.txtTelefono.setText(telefono)
            self.txtDireccion.setText(direccion)
            self.chkActivo.setChecked(int(activo))

            # mostrar caja de texto para ID y CheckBox para Activo
            self.lblId.setVisible(True)
            self.lblActivo.setVisible(True)
            self.txtId.setVisible(True)
            self.chkActivo.setVisible(True)

            self.tabWidget.setTabText(1, "Editar Cliente")
            # mostrar la pestaña 1 (editar cliente)
            self.tabWidget.setCurrentIndex(1)
        else:
            QMessageBox.about(self, "Editar Cliente", "Seleccione un cliente de la lista")

    def tab_clicked(self, index):
        if index == 1 and self.tabWidget.tabText(index) == "Nuevo Cliente":
            # cargar las cajas de texto con los datos del cliente
            self.txtId.setText("")
            self.txtCI.setText("")
            self.txtNombre.setText("")
            self.txtApellido.setText("")
            self.txtTelefono.setText("")
            self.txtDireccion.setText("")
            self.chkActivo.setChecked(True)

            self.lblId.setVisible(False)
            self.lblActivo.setVisible(False)
            self.txtId.setVisible(False)
            self.chkActivo.setVisible(False)

        if index == 0:
            self.tabWidget.setTabText(1, "Nuevo Cliente")


    def cancelar(self):
        self.tabWidget.setTabText(1, "Nuevo Cliente")
        # mostrar la pestaña 0 (lista de clientes)
        self.tabWidget.setCurrentIndex(0)

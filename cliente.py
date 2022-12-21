# This Python file uses the following encoding: utf-8
from PyQt5 import QtWidgets, uic, QtGui
from PyQt5.QtWidgets import QMessageBox, QFileDialog, QAction
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import pyqtSignal, pyqtSlot, Qt, QThread
from PIL import ImageQt
import cv2
import imutils
import numpy as np
import conndb


class VideoThread(QThread):
    change_pixmap_signal = pyqtSignal(np.ndarray)

    def __init__(self):
        super().__init__()
        self._run_flag = True

    def run(self):
        self._run_flag = True

        cascPath = "haarcascade_frontalface_default.xml"
        faceClassif = cv2.CascadeClassifier(cascPath)
        # LEYENDO VIDEO
        cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        print("_run_flag 1:", self._run_flag)
        while self._run_flag:
            ret, frame = cap.read()

            faces = faceClassif.detectMultiScale(
                frame,
                scaleFactor=1.1,
                minNeighbors=10,
                minSize=(70, 70)
            )
            print("Found {0} faces!".format(len(faces)))

            # Draw a rectangle around the faces
            for (x, y, w, h) in faces:
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)

            if ret:
                self.change_pixmap_signal.emit(frame)

        '''When stop'''
        print("_run_flag 2:", self._run_flag)
        ret, frame = cap.read()
        faces = faceClassif.detectMultiScale(
            frame,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(70, 70)
        )
        print("Found {0} faces!".format(len(faces)))
        face = frame
        for (x, y, w, h) in faces:
            face = frame[y:y + h, x:x + w]
            face = cv2.resize(face, (320, 320))

        if len(faces) < 1:
            face = cv2.resize(face, (50, 50))

        self.change_pixmap_signal.emit(face)
        # shut down capture system
        cap.release()


    def stop(self):
        """Sets run flag to False and waits for thread to finish"""
        self._run_flag = False
        self.wait()


class cliente(QtWidgets.QWidget):
    def __init__(self):
        super(cliente, self).__init__()
        uic.loadUi("cliente.ui", self)
        self.setWindowTitle("Gestión de Clientes")

        style = "::section {""background-color: rgb(33, 34, 34); }"
        header = self.tableWidget.horizontalHeader()
        header.setStyleSheet(style)
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(5, QtWidgets.QHeaderView.Stretch)
        self.tableWidget.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)

        # create the video capture thread
        self.thread = VideoThread()
        # connect its signal to the update_image slot
        self.thread.change_pixmap_signal.connect(self.update_image)

        self.btnEditar.clicked.connect(self.getItem)
        self.btnGuardar.clicked.connect(self.updateData)
        self.btnCamara.clicked.connect(self.runCamera)
        self.btnSubir.clicked.connect(self.openImage)
        self.btnEliminar.clicked.connect(self.deleteData)
        self.btnCancelar.clicked.connect(self.cancelar)
        self.tabWidget.tabBarClicked.connect(self.tab_clicked)

        self.loadData()
        self.tabWidget.setCurrentIndex(0)


    def openImage(self):
        if self.btnCamara.text() == "Capturar":
            self.thread.stop()
            self.btnCamara.setText("Iniciar Cámara")
        imagePath, _ = QFileDialog.getOpenFileName(self, 'Abrir Imagen', 'C:\\', 'Image files (*.jpg *.jpeg)')
        if len(imagePath) > 0:
            self.recortarRostro(imagePath)


    def recortarRostro(self, imagePath):
        faceClassif = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")
        image = cv2.imread(imagePath)
        image = imutils.resize(image, width=800)
        faces = faceClassif.detectMultiScale(
            image,
            scaleFactor=1.1,
            minNeighbors=10,
            minSize=(70, 70)
        )
        face = image
        for (x, y, w, h) in faces:
            face = image[y:y + h, x:x + w]
            face = cv2.resize(face, (320, 320))

        if len(faces) < 1:
            face = cv2.resize(face, (50, 50))

        self.update_image(face)
            #cv2.imwrite("images/faces/" + str(count) + ".jpg", face)
            #count += 1


    def runCamera(self):
        if self.btnCamara.text() == "Iniciar Cámara":
            self.thread.start()
            self.btnCamara.setText("Capturar")
        else:
            self.thread.stop()
            self.btnCamara.setText("Iniciar Cámara")


    @pyqtSlot(np.ndarray)
    def update_image(self, cv_img):
        if cv_img.shape[0] == 50:
            QMessageBox.about(self, "Cámara", "No se han detectado rostros en la foto")

        """Updates the image_label with a new opencv image"""
        qt_img = self.convert_cv_qt(cv_img)
        self.lblFoto.setPixmap(qt_img)


    def convert_cv_qt(self, cv_img):
        """Convert from an opencv image to QPixmap"""
        rgb_image = cv2.cvtColor(cv_img, cv2.COLOR_BGR2RGB)
        h, w, ch = rgb_image.shape
        bytes_per_line = ch * w
        convert_to_Qt_format = QtGui.QImage(rgb_image.data, w, h, bytes_per_line, QtGui.QImage.Format_RGB888)
        p = convert_to_Qt_format.scaled(320, 320, Qt.KeepAspectRatio)
        return QPixmap.fromImage(p)


    def saveImage(self, name):
        image = ImageQt.fromqpixmap(self.lblFoto.pixmap())
        image.save('images/faces/'+name+'.jpg')


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
            self.tableWidget.setItem(row, 6, QtWidgets.QTableWidgetItem(r[6]))
            self.tableWidget.setItem(row, 7, QtWidgets.QTableWidgetItem(str(r[7])))
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
            image_path = 'images/faces/' + nombre.split()[0] + '_' + ci + '.jpg'
            activo = int(self.chkActivo.isChecked())
            strsql = "UPDATE cliente SET ci='{}', nombre='{}', apellido='{}', telefono='{}', direccion='{}', foto='{}', activo='{}' WHERE id='{}'".format(
                ci,
                nombre,
                apellido,
                telefono,
                direccion,
                image_path,
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
                # guardar foto
                self.saveImage(nombre.split()[0] + '_' + ci)
            except:
                QMessageBox.about(self, "Error", "Hubo un error al actualizar los datos del cliente")
        else:
            self.saveData()


    # función para actualizar los datos del usuario seleccionado
    def saveData(self):
        if self.tabWidget.tabText(1) == "Nuevo Cliente":
            ci = self.txtCI.text()
            nombre = self.txtNombre.text()
            apellido = self.txtApellido.text()
            telefono = self.txtTelefono.text()
            direccion = self.txtDireccion.text()
            image_path = 'images/faces/' + nombre.split()[0] + '_' + ci + '.jpg'
            strsql = "INSERT INTO cliente (ci, nombre, apellido, telefono, direccion, foto) VALUES('{}', '{}', '{}', '{}', '{}', '{}')".format(
                ci,
                nombre,
                apellido,
                telefono,
                direccion,
                image_path)

            conn = conndb.conndb()
            try:
                conn.queryExecute(strsql)
                QMessageBox.about(self, "Nuevo Cliente", "Los datos del cliente se guardaron correctamente")
                # guardar foto
                self.saveImage(nombre.split()[0] + '_' + ci)
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
            imagePath =self.tableWidget.item(row, 6).text()
            activo = self.tableWidget.item(row, 7).text()

            # cargar las cajas de texto con los datos del cliente
            self.txtId.setText(str(id))
            self.txtCI.setText(ci)
            self.txtNombre.setText(nombre)
            self.txtApellido.setText(apellido)
            self.txtTelefono.setText(telefono)
            self.txtDireccion.setText(direccion)
            self.lblFoto.setPixmap(QPixmap(imagePath))
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
            self.lblFoto.clear()

            self.lblId.setVisible(False)
            self.lblActivo.setVisible(False)
            self.txtId.setVisible(False)
            self.chkActivo.setVisible(False)

        if index == 0:
            self.tabWidget.setTabText(1, "Nuevo Cliente")
            if self.btnCamara.text() == "Capturar":
                self.thread.stop()
                self.btnCamara.setText("Iniciar Cámara")



    def cancelar(self):
        self.tabWidget.setTabText(1, "Nuevo Cliente")
        # mostrar la pestaña 0 (lista de clientes)
        self.tabWidget.setCurrentIndex(0)

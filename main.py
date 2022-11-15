# This Python file uses the following encoding: utf-8
import sys

from PyQt5 import QtWidgets, uic, QtCore

import user_management as usr_mgt
import login
import live_cam

class main(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Identificación de Antecedentes")
        #self.mdiArea.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.logout()
        self.actionLogin.triggered.connect(self.login)
        self.actionLogout.triggered.connect(self.logout)
        self.actionIniciar_Camara.triggered.connect(self.l_cam)
        self.actionGestion_de_Usuarios.triggered.connect(self.user_mgt)


    def login(self):
        self.lg = login.login()
        self.lg.exec()
        result = self.lg.result
        try:
            if len(result)==1:
                self.menuAdmin.setEnabled(True)
                self.menuCamara.setEnabled(True)
                self.menuClientes.setEnabled(True)
                self.menuConfiguracion.setEnabled(True)
                self.menuReportes.setEnabled(True)
        except:
            pass

    def logout(self):
        self.menuAdmin.setEnabled(False)
        self.menuCamara.setEnabled(False)
        self.menuClientes.setEnabled(False)
        self.menuAdmin.setEnabled(False)
        self.menuReportes.setEnabled(False)

    def user_mgt(self):
        self.usr_mgt_w = usr_mgt.user_management()
        #self.mdiArea.addSubWindow(self.usr_mgt_w)
        self.usr_mgt_w.show()

    def l_cam(self):
        for w in self.mdiArea.subWindowList():
            self.mdiArea.removeSubWindow(w)

        self.live_cam = live_cam.live_cam()

        mdi = self.mdiArea.addSubWindow(self.live_cam, QtCore.Qt.FramelessWindowHint)
        self.live_cam.setGeometry(0, 0, 660, 500)
        self.live_cam.show()
        mdi.resize(640, 480)

app = QtWidgets.QApplication(sys.argv)
widget = main()
widget.show()
app.exec()

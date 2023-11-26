# This Python file uses the following encoding: utf-8
import sys
import os

from PyQt5 import QtWidgets, uic, QtCore
from PyQt5.QtWidgets import QMessageBox

from user_management import UserManagement
from login import Login
from live_cam import LiveCam
from cliente import Cliente


class main(QtWidgets.QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        os.environ["QT_QPA_PLATFORM"] = "xcb"
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Identificación de Antecedentes")
        self.showMaximized()

        #self.logout()
        self.actionLogin.triggered.connect(self.login)
        self.actionLogout.triggered.connect(self.logout)
        self.actionIniciar_Camara.triggered.connect(self.l_cam)
        self.actionGestion_de_Usuarios.triggered.connect(self.user_mgt)
        self.actionClientes.triggered.connect(self.clientes_show)

    def login(self):
        self.lg = Login()
        self.lg.exec()
        result = self.lg.result
        try:
            if len(result) == 1:
                self.menuAdmin.setEnabled(True)
                self.menuCamara.setEnabled(True)
                self.menuClientes.setEnabled(True)
                self.menuReportes.setEnabled(True)

        except:
            pass

    def logout(self):
        self.menuAdmin.setEnabled(False)
        self.menuCamara.setEnabled(False)
        self.menuClientes.setEnabled(False)
        self.menuReportes.setEnabled(False)

    def user_mgt(self):
        self.usr_mgt_frm = UserManagement()
        # self.mdiArea.addSubWindow(self.usr_mgt_frm)
        self.usr_mgt_frm.show()

    def clientes_show(self):
        self.clientes_frm = Cliente()
        # self.mdiArea.addSubWindow(self.clientes_frm)
        self.clientes_frm.show()

    def l_cam(self):
        for w in self.mdiArea.subWindowList():
            self.mdiArea.removeSubWindow(w)

        self.live_cam = LiveCam()

        mdi = self.mdiArea.addSubWindow(self.live_cam, QtCore.Qt.FramelessWindowHint)
        self.live_cam.setGeometry(0, 0, 660, 500)
        self.live_cam.show()
        mdi.resize(640, 480)


app = QtWidgets.QApplication(sys.argv)

screen = app.primaryScreen()
# print('Screen: %s' % screen.name())
# size = screen.size()
# print('Size: %d x %d' % (size.width(), size.height()))
rect = screen.availableGeometry()
# print('Available: %d x %d' % (rect.width(), rect.height()))

widget = main()
widget.mdiArea.resize(rect.width() - 30, rect.height() - 70)
widget.show()
app.exec()

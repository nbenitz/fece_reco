# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.4.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QMainWindow, QMdiArea, QMenu,
    QMenuBar, QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(951, 572)
        self.actionLogin = QAction(main)
        self.actionLogin.setObjectName(u"actionLogin")
        self.actionLogout = QAction(main)
        self.actionLogout.setObjectName(u"actionLogout")
        self.actionGestion_de_Usuarios = QAction(main)
        self.actionGestion_de_Usuarios.setObjectName(u"actionGestion_de_Usuarios")
        self.actionCuenta = QAction(main)
        self.actionCuenta.setObjectName(u"actionCuenta")
        self.actionDeposito = QAction(main)
        self.actionDeposito.setObjectName(u"actionDeposito")
        self.actionExtraccion = QAction(main)
        self.actionExtraccion.setObjectName(u"actionExtraccion")
        self.actionClientes = QAction(main)
        self.actionClientes.setObjectName(u"actionClientes")
        self.actionAntecedentes = QAction(main)
        self.actionAntecedentes.setObjectName(u"actionAntecedentes")
        self.actionReporte_de_Entrada_de_Clientes = QAction(main)
        self.actionReporte_de_Entrada_de_Clientes.setObjectName(u"actionReporte_de_Entrada_de_Clientes")
        self.actionReporte_de_Clientes = QAction(main)
        self.actionReporte_de_Clientes.setObjectName(u"actionReporte_de_Clientes")
        self.actionReporte_de_Usuarios = QAction(main)
        self.actionReporte_de_Usuarios.setObjectName(u"actionReporte_de_Usuarios")
        self.actionGestion_de_Usuarios_2 = QAction(main)
        self.actionGestion_de_Usuarios_2.setObjectName(u"actionGestion_de_Usuarios_2")
        self.actionIniciar_Camara = QAction(main)
        self.actionIniciar_Camara.setObjectName(u"actionIniciar_Camara")
        self.actionCerrar_Camara = QAction(main)
        self.actionCerrar_Camara.setObjectName(u"actionCerrar_Camara")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setGeometry(QRect(10, 10, 931, 481))
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 951, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAdmin = QMenu(self.menubar)
        self.menuAdmin.setObjectName(u"menuAdmin")
        self.menuCamara = QMenu(self.menubar)
        self.menuCamara.setObjectName(u"menuCamara")
        self.menuClientes = QMenu(self.menubar)
        self.menuClientes.setObjectName(u"menuClientes")
        self.menuReportes = QMenu(self.menubar)
        self.menuReportes.setObjectName(u"menuReportes")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuCamara.menuAction())
        self.menubar.addAction(self.menuClientes.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionLogin)
        self.menuArchivo.addAction(self.actionLogout)
        self.menuAdmin.addAction(self.actionGestion_de_Usuarios)
        self.menuCamara.addAction(self.actionIniciar_Camara)
        self.menuCamara.addAction(self.actionCerrar_Camara)
        self.menuClientes.addAction(self.actionClientes)
        self.menuClientes.addAction(self.actionAntecedentes)
        self.menuReportes.addSeparator()
        self.menuReportes.addAction(self.actionReporte_de_Entrada_de_Clientes)
        self.menuReportes.addAction(self.actionReporte_de_Clientes)
        self.menuReportes.addAction(self.actionReporte_de_Usuarios)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionLogin.setText(QCoreApplication.translate("main", u"Iniciar Sesi\u00f3n", None))
        self.actionLogout.setText(QCoreApplication.translate("main", u"Cerrar Sesi\u00f3n", None))
        self.actionGestion_de_Usuarios.setText(QCoreApplication.translate("main", u"Gesti\u00f3n de Usuarios", None))
        self.actionCuenta.setText(QCoreApplication.translate("main", u"Cuenta", None))
        self.actionDeposito.setText(QCoreApplication.translate("main", u"Dep\u00f3sito", None))
        self.actionExtraccion.setText(QCoreApplication.translate("main", u"Extracci\u00f3n", None))
        self.actionClientes.setText(QCoreApplication.translate("main", u"Gestionar Clientes", None))
        self.actionAntecedentes.setText(QCoreApplication.translate("main", u"Antecedentes", None))
        self.actionReporte_de_Entrada_de_Clientes.setText(QCoreApplication.translate("main", u"Reporte de Entrada de Clientes", None))
        self.actionReporte_de_Clientes.setText(QCoreApplication.translate("main", u"Reporte de Clientes", None))
        self.actionReporte_de_Usuarios.setText(QCoreApplication.translate("main", u"Reporte de Usuarios", None))
        self.actionGestion_de_Usuarios_2.setText(QCoreApplication.translate("main", u"Gesti\u00f3n de Usuarios", None))
        self.actionIniciar_Camara.setText(QCoreApplication.translate("main", u"Iniciar C\u00e1mara", None))
        self.actionCerrar_Camara.setText(QCoreApplication.translate("main", u"Cerrar C\u00e1mara", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("main", u"Archivo", None))
        self.menuAdmin.setTitle(QCoreApplication.translate("main", u"Admin", None))
        self.menuCamara.setTitle(QCoreApplication.translate("main", u"C\u00e1mara", None))
        self.menuClientes.setTitle(QCoreApplication.translate("main", u"Clientes", None))
        self.menuReportes.setTitle(QCoreApplication.translate("main", u"Reportes", None))
    # retranslateUi


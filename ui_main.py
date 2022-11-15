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
from PySide6.QtWidgets import (QApplication, QMainWindow, QMenu, QMenuBar,
    QSizePolicy, QStatusBar, QWidget)

class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(800, 600)
        self.actionIniciar_Sesi_n = QAction(main)
        self.actionIniciar_Sesi_n.setObjectName(u"actionIniciar_Sesi_n")
        self.actionCerrar_Sesi_n = QAction(main)
        self.actionCerrar_Sesi_n.setObjectName(u"actionCerrar_Sesi_n")
        self.actionGesti_n_de_Usuarios = QAction(main)
        self.actionGesti_n_de_Usuarios.setObjectName(u"actionGesti_n_de_Usuarios")
        self.actionCuenta = QAction(main)
        self.actionCuenta.setObjectName(u"actionCuenta")
        self.actionDep_sito = QAction(main)
        self.actionDep_sito.setObjectName(u"actionDep_sito")
        self.actionExtracci_n = QAction(main)
        self.actionExtracci_n.setObjectName(u"actionExtracci_n")
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
        self.actionGesti_n_de_Usuarios_2 = QAction(main)
        self.actionGesti_n_de_Usuarios_2.setObjectName(u"actionGesti_n_de_Usuarios_2")
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 22))
        self.menuArchivo = QMenu(self.menubar)
        self.menuArchivo.setObjectName(u"menuArchivo")
        self.menuAdmin = QMenu(self.menubar)
        self.menuAdmin.setObjectName(u"menuAdmin")
        self.menuCS = QMenu(self.menubar)
        self.menuCS.setObjectName(u"menuCS")
        self.menuTeller = QMenu(self.menubar)
        self.menuTeller.setObjectName(u"menuTeller")
        self.menuC_mara = QMenu(self.menubar)
        self.menuC_mara.setObjectName(u"menuC_mara")
        self.menuClientes = QMenu(self.menubar)
        self.menuClientes.setObjectName(u"menuClientes")
        self.menuReportes = QMenu(self.menubar)
        self.menuReportes.setObjectName(u"menuReportes")
        self.menuConfiguraci_n = QMenu(self.menubar)
        self.menuConfiguraci_n.setObjectName(u"menuConfiguraci_n")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menuArchivo.menuAction())
        self.menubar.addAction(self.menuAdmin.menuAction())
        self.menubar.addAction(self.menuCS.menuAction())
        self.menubar.addAction(self.menuTeller.menuAction())
        self.menubar.addAction(self.menuC_mara.menuAction())
        self.menubar.addAction(self.menuClientes.menuAction())
        self.menubar.addAction(self.menuReportes.menuAction())
        self.menubar.addAction(self.menuConfiguraci_n.menuAction())
        self.menuArchivo.addSeparator()
        self.menuArchivo.addAction(self.actionIniciar_Sesi_n)
        self.menuArchivo.addAction(self.actionCerrar_Sesi_n)
        self.menuAdmin.addAction(self.actionGesti_n_de_Usuarios)
        self.menuCS.addAction(self.actionCuenta)
        self.menuTeller.addAction(self.actionDep_sito)
        self.menuTeller.addAction(self.actionExtracci_n)
        self.menuClientes.addAction(self.actionClientes)
        self.menuClientes.addAction(self.actionAntecedentes)
        self.menuReportes.addSeparator()
        self.menuReportes.addAction(self.actionReporte_de_Entrada_de_Clientes)
        self.menuReportes.addAction(self.actionReporte_de_Clientes)
        self.menuReportes.addAction(self.actionReporte_de_Usuarios)
        self.menuConfiguraci_n.addAction(self.actionGesti_n_de_Usuarios_2)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"main", None))
        self.actionIniciar_Sesi_n.setText(QCoreApplication.translate("main", u"Iniciar Sesi\u00f3n", None))
        self.actionCerrar_Sesi_n.setText(QCoreApplication.translate("main", u"Cerrar Sesi\u00f3n", None))
        self.actionGesti_n_de_Usuarios.setText(QCoreApplication.translate("main", u"Gesti\u00f3n de Usuarios", None))
        self.actionCuenta.setText(QCoreApplication.translate("main", u"Cuenta", None))
        self.actionDep_sito.setText(QCoreApplication.translate("main", u"Dep\u00f3sito", None))
        self.actionExtracci_n.setText(QCoreApplication.translate("main", u"Extracci\u00f3n", None))
        self.actionClientes.setText(QCoreApplication.translate("main", u"Clientes", None))
        self.actionAntecedentes.setText(QCoreApplication.translate("main", u"Antecedentes", None))
        self.actionReporte_de_Entrada_de_Clientes.setText(QCoreApplication.translate("main", u"Reporte de Entrada de Clientes", None))
        self.actionReporte_de_Clientes.setText(QCoreApplication.translate("main", u"Reporte de Clientes", None))
        self.actionReporte_de_Usuarios.setText(QCoreApplication.translate("main", u"Reporte de Usuarios", None))
        self.actionGesti_n_de_Usuarios_2.setText(QCoreApplication.translate("main", u"Gesti\u00f3n de Usuarios", None))
        self.menuArchivo.setTitle(QCoreApplication.translate("main", u"Archivo", None))
        self.menuAdmin.setTitle(QCoreApplication.translate("main", u"Admin", None))
        self.menuCS.setTitle(QCoreApplication.translate("main", u"CS", None))
        self.menuTeller.setTitle(QCoreApplication.translate("main", u"Teller", None))
        self.menuC_mara.setTitle(QCoreApplication.translate("main", u"C\u00e1mara", None))
        self.menuClientes.setTitle(QCoreApplication.translate("main", u"Clientes", None))
        self.menuReportes.setTitle(QCoreApplication.translate("main", u"Reportes", None))
        self.menuConfiguraci_n.setTitle(QCoreApplication.translate("main", u"Configuraci\u00f3n", None))
    # retranslateUi


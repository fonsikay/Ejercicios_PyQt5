# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BuscadorWeb.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class frmBuscadorWeb(object):
    def setupUi(self, frmBuscadorWeb):
        frmBuscadorWeb.setObjectName("frmBuscadorWeb")
        frmBuscadorWeb.resize(640, 500)
        self.webContenido = QtWebEngineWidgets.QWebEngineView(frmBuscadorWeb)
        self.webContenido.setGeometry(QtCore.QRect(20, 60, 601, 421))
        self.webContenido.setObjectName("webContenido")
        self.widget = QtWidgets.QWidget(frmBuscadorWeb)
        self.widget.setGeometry(QtCore.QRect(20, 19, 601, 25))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lblDireccion = QtWidgets.QLabel(self.widget)
        self.lblDireccion.setObjectName("lblDireccion")
        self.horizontalLayout.addWidget(self.lblDireccion)
        self.txtDireccion = QtWidgets.QLineEdit(self.widget)
        self.txtDireccion.setObjectName("txtDireccion")
        self.horizontalLayout.addWidget(self.txtDireccion)
        self.btnIr = QtWidgets.QPushButton(self.widget)
        self.btnIr.setObjectName("btnIr")
        self.horizontalLayout.addWidget(self.btnIr)

        self.retranslateUi(frmBuscadorWeb)
        QtCore.QMetaObject.connectSlotsByName(frmBuscadorWeb)

    def retranslateUi(self, frmBuscadorWeb):
        _translate = QtCore.QCoreApplication.translate
        frmBuscadorWeb.setWindowTitle(_translate("frmBuscadorWeb", "Navegador Web Básico "))
        self.lblDireccion.setText(_translate("frmBuscadorWeb", "Dirección:"))
        self.btnIr.setText(_translate("frmBuscadorWeb", "Ir"))
from PyQt5 import QtWebEngineWidgets

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EventosSlot.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class frmEventos(object):
    def setupUi(self, frmEventos: object) -> object:
        frmEventos.setObjectName("frmEventos")
        frmEventos.resize(223, 160)
        self.txtTexto = QtWidgets.QLineEdit(frmEventos)
        self.txtTexto.setGeometry(QtCore.QRect(50, 30, 113, 20))
        self.txtTexto.setObjectName("txtTexto")
        self.btnCambiar = QtWidgets.QPushButton(frmEventos)
        self.btnCambiar.setGeometry(QtCore.QRect(70, 100, 75, 23))
        self.btnCambiar.setObjectName("btnCambiar")

        self.retranslateUi(frmEventos)
        self.btnCambiar.clicked.connect(self.txtTexto.clear)
        QtCore.QMetaObject.connectSlotsByName(frmEventos)

    def retranslateUi(self, frmEventos):
        _translate = QtCore.QCoreApplication.translate
        frmEventos.setWindowTitle(_translate("frmEventos", "Señales y Slots"))
        self.btnCambiar.setText(_translate("frmEventos", "Botón"))

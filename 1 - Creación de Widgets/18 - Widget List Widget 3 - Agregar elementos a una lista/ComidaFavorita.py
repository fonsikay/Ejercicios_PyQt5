# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ComidaFavorita.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class frmComidaFavorita(object):
    def setupUi(self, frmComidaFavorita):
        frmComidaFavorita.setObjectName("frmComidaFavorita")
        frmComidaFavorita.resize(493, 221)
        self.lblComida = QtWidgets.QLabel(frmComidaFavorita)
        self.lblComida.setGeometry(QtCore.QRect(20, 30, 181, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblComida.setFont(font)
        self.lblComida.setObjectName("lblComida")
        self.txtComida = QtWidgets.QLineEdit(frmComidaFavorita)
        self.txtComida.setGeometry(QtCore.QRect(210, 30, 171, 20))
        self.txtComida.setObjectName("txtComida")
        self.btnAnadir = QtWidgets.QPushButton(frmComidaFavorita)
        self.btnAnadir.setGeometry(QtCore.QRect(390, 30, 81, 23))
        self.btnAnadir.setObjectName("btnAnadir")
        self.listComida = QtWidgets.QListWidget(frmComidaFavorita)
        self.listComida.setGeometry(QtCore.QRect(210, 70, 261, 121))
        self.listComida.setObjectName("listComida")

        self.retranslateUi(frmComidaFavorita)
        QtCore.QMetaObject.connectSlotsByName(frmComidaFavorita)

    def retranslateUi(self, frmComidaFavorita):
        _translate = QtCore.QCoreApplication.translate
        frmComidaFavorita.setWindowTitle(_translate("frmComidaFavorita", "Listado comidas favoritas"))
        self.lblComida.setText(_translate("frmComidaFavorita", "Especifique su comida favorita:"))
        self.btnAnadir.setText(_translate("frmComidaFavorita", "Añadir"))

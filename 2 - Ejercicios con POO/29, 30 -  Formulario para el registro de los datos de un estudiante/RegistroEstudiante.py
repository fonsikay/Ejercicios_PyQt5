# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'RegistroEstudiante.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class frmRegistroEstudiante(object):
    def setupUi(self, frmRegistroEstudiante):
        frmRegistroEstudiante.setObjectName("frmRegistroEstudiante")
        frmRegistroEstudiante.resize(314, 243)
        self.lblIdentidad = QtWidgets.QLabel(frmRegistroEstudiante)
        self.lblIdentidad.setGeometry(QtCore.QRect(20, 32, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblIdentidad.setFont(font)
        self.lblIdentidad.setObjectName("lblIdentidad")
        self.lblNombre = QtWidgets.QLabel(frmRegistroEstudiante)
        self.lblNombre.setGeometry(QtCore.QRect(20, 62, 111, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblTelefono = QtWidgets.QLabel(frmRegistroEstudiante)
        self.lblTelefono.setGeometry(QtCore.QRect(20, 92, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTelefono.setFont(font)
        self.lblTelefono.setObjectName("lblTelefono")
        self.lblCarnet = QtWidgets.QLabel(frmRegistroEstudiante)
        self.lblCarnet.setGeometry(QtCore.QRect(20, 124, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCarnet.setFont(font)
        self.lblCarnet.setObjectName("lblCarnet")
        self.lblCarrera = QtWidgets.QLabel(frmRegistroEstudiante)
        self.lblCarrera.setGeometry(QtCore.QRect(20, 153, 47, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblCarrera.setFont(font)
        self.lblCarrera.setObjectName("lblCarrera")
        self.txtIdentidad = QtWidgets.QLineEdit(frmRegistroEstudiante)
        self.txtIdentidad.setGeometry(QtCore.QRect(140, 30, 151, 20))
        self.txtIdentidad.setObjectName("txtIdentidad")
        self.txtNombre = QtWidgets.QLineEdit(frmRegistroEstudiante)
        self.txtNombre.setGeometry(QtCore.QRect(140, 60, 151, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.txtTelefono = QtWidgets.QLineEdit(frmRegistroEstudiante)
        self.txtTelefono.setGeometry(QtCore.QRect(140, 90, 151, 20))
        self.txtTelefono.setObjectName("txtTelefono")
        self.txtCarnet = QtWidgets.QLineEdit(frmRegistroEstudiante)
        self.txtCarnet.setGeometry(QtCore.QRect(140, 120, 151, 20))
        self.txtCarnet.setObjectName("txtCarnet")
        self.txtCarrera = QtWidgets.QLineEdit(frmRegistroEstudiante)
        self.txtCarrera.setGeometry(QtCore.QRect(140, 150, 151, 20))
        self.txtCarrera.setObjectName("txtCarrera")
        self.btnRegistro = QtWidgets.QPushButton(frmRegistroEstudiante)
        self.btnRegistro.setGeometry(QtCore.QRect(140, 190, 151, 23))
        self.btnRegistro.setObjectName("pushButton")

        self.retranslateUi(frmRegistroEstudiante)
        QtCore.QMetaObject.connectSlotsByName(frmRegistroEstudiante)

    def retranslateUi(self, frmRegistroEstudiante):
        _translate = QtCore.QCoreApplication.translate
        frmRegistroEstudiante.setWindowTitle(_translate("frmRegistroEstudiante", "Estudiante: Registro"))
        self.lblIdentidad.setText(_translate("frmRegistroEstudiante", "Identidad:"))
        self.lblNombre.setText(_translate("frmRegistroEstudiante", "Nombre completo:"))
        self.lblTelefono.setText(_translate("frmRegistroEstudiante", "Teléfono:"))
        self.lblCarnet.setText(_translate("frmRegistroEstudiante", "Carnet:"))
        self.lblCarrera.setText(_translate("frmRegistroEstudiante", "Carrera:"))
        self.btnRegistro.setText(_translate("frmRegistroEstudiante", "Registrar"))

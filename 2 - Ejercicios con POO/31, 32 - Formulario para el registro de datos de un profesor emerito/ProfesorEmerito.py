# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ProfesorEmerito.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class frmProfesorEmerito(object):
    def setupUi(self, frmProfesorEmerito):
        frmProfesorEmerito.setObjectName("frmProfesorEmerito")
        frmProfesorEmerito.resize(380, 251)
        self.lblIdentidad = QtWidgets.QLabel(frmProfesorEmerito)
        self.lblIdentidad.setGeometry(QtCore.QRect(30, 32, 61, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblIdentidad.setFont(font)
        self.lblIdentidad.setObjectName("lblIdentidad")
        self.lblNombre = QtWidgets.QLabel(frmProfesorEmerito)
        self.lblNombre.setGeometry(QtCore.QRect(30, 62, 110, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNombre.setFont(font)
        self.lblNombre.setObjectName("lblNombre")
        self.lblTelefono = QtWidgets.QLabel(frmProfesorEmerito)
        self.lblTelefono.setGeometry(QtCore.QRect(30, 93, 60, 13))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblTelefono.setFont(font)
        self.lblTelefono.setObjectName("lblTelefono")
        self.lblEspecialidad = QtWidgets.QLabel(frmProfesorEmerito)
        self.lblEspecialidad.setGeometry(QtCore.QRect(30, 122, 80, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblEspecialidad.setFont(font)
        self.lblEspecialidad.setObjectName("lblEspecialidad")
        self.lblReconocimiento = QtWidgets.QLabel(frmProfesorEmerito)
        self.lblReconocimiento.setGeometry(QtCore.QRect(30, 152, 100, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblReconocimiento.setFont(font)
        self.lblReconocimiento.setObjectName("lblReconocimiento")
        self.txtIdentidad = QtWidgets.QLineEdit(frmProfesorEmerito)
        self.txtIdentidad.setGeometry(QtCore.QRect(150, 30, 201, 20))
        self.txtIdentidad.setObjectName("txtIdentidad")
        self.txtNombre = QtWidgets.QLineEdit(frmProfesorEmerito)
        self.txtNombre.setGeometry(QtCore.QRect(150, 60, 201, 20))
        self.txtNombre.setObjectName("txtNombre")
        self.txtTelefono = QtWidgets.QLineEdit(frmProfesorEmerito)
        self.txtTelefono.setGeometry(QtCore.QRect(150, 90, 201, 20))
        self.txtTelefono.setObjectName("txtTelefono")
        self.txtReconocimiento = QtWidgets.QLineEdit(frmProfesorEmerito)
        self.txtReconocimiento.setGeometry(QtCore.QRect(150, 150, 201, 20))
        self.txtReconocimiento.setObjectName("txtReconocimiento")
        self.cmbEspecialidad = QtWidgets.QComboBox(frmProfesorEmerito)
        self.cmbEspecialidad.setGeometry(QtCore.QRect(150, 120, 201, 20))
        self.cmbEspecialidad.setObjectName("cmbEsoecialidad")
        self.cmbEspecialidad.addItem("")
        self.cmbEspecialidad.addItem("")
        self.cmbEspecialidad.addItem("")
        self.btnRegistrar = QtWidgets.QPushButton(frmProfesorEmerito)
        self.btnRegistrar.setGeometry(QtCore.QRect(150, 200, 201, 23))
        self.btnRegistrar.setObjectName("btnRegistrar")
        self.lblIdentidad.setBuddy(self.txtIdentidad)
        self.lblNombre.setBuddy(self.txtNombre)
        self.lblTelefono.setBuddy(self.txtTelefono)
        self.lblEspecialidad.setBuddy(self.cmbEspecialidad)
        self.lblReconocimiento.setBuddy(self.txtReconocimiento)

        self.retranslateUi(frmProfesorEmerito)
        QtCore.QMetaObject.connectSlotsByName(frmProfesorEmerito)
        frmProfesorEmerito.setTabOrder(self.txtIdentidad, self.txtNombre)
        frmProfesorEmerito.setTabOrder(self.txtNombre, self.txtTelefono)
        frmProfesorEmerito.setTabOrder(self.txtTelefono, self.cmbEspecialidad)
        frmProfesorEmerito.setTabOrder(self.cmbEspecialidad, self.txtReconocimiento)
        frmProfesorEmerito.setTabOrder(self.txtReconocimiento, self.btnRegistrar)

    def retranslateUi(self, frmProfesorEmerito):
        _translate = QtCore.QCoreApplication.translate
        frmProfesorEmerito.setWindowTitle(_translate("frmProfesorEmerito", "Profesor Emérito: Registro"))
        self.lblIdentidad.setText(_translate("frmProfesorEmerito", "Identidad:"))
        self.lblNombre.setText(_translate("frmProfesorEmerito", "Nombre Completo:"))
        self.lblTelefono.setText(_translate("frmProfesorEmerito", "Teléfono:"))
        self.lblEspecialidad.setText(_translate("frmProfesorEmerito", "Especialidad:"))
        self.lblReconocimiento.setText(_translate("frmProfesorEmerito", "Reconocimiento:"))
        self.cmbEspecialidad.setItemText(0, _translate("frmProfesorEmerito", "Informática"))
        self.cmbEspecialidad.setItemText(1, _translate("frmProfesorEmerito", "Ingeniería"))
        self.cmbEspecialidad.setItemText(2, _translate("frmProfesorEmerito", "Literatura"))
        self.btnRegistrar.setText(_translate("frmProfesorEmerito", "Registrar"))

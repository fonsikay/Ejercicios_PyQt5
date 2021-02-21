# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'CreacionTablas.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class frmCreacionTablas(object):
    def setupUi(self, frmCreacionTablas):
        frmCreacionTablas.setObjectName("frmCreacionTablas")
        frmCreacionTablas.resize(491, 312)
        self.lblNombreBBDD = QtWidgets.QLabel(frmCreacionTablas)
        self.lblNombreBBDD.setGeometry(QtCore.QRect(20, 22, 171, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNombreBBDD.setFont(font)
        self.lblNombreBBDD.setObjectName("lblNombreBBDD")
        self.lblNombreTabla = QtWidgets.QLabel(frmCreacionTablas)
        self.lblNombreTabla.setGeometry(QtCore.QRect(20, 61, 121, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblNombreTabla.setFont(font)
        self.lblNombreTabla.setObjectName("lblNombreTabla")
        self.txtNombreBBDD = QtWidgets.QLineEdit(frmCreacionTablas)
        self.txtNombreBBDD.setGeometry(QtCore.QRect(190, 20, 121, 20))
        self.txtNombreBBDD.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.txtNombreBBDD.setAlignment(QtCore.Qt.AlignCenter)
        self.txtNombreBBDD.setObjectName("txtNombreBBDD")
        self.txtNombreTabla = QtWidgets.QLineEdit(frmCreacionTablas)
        self.txtNombreTabla.setGeometry(QtCore.QRect(190, 60, 281, 20))
        self.txtNombreTabla.setObjectName("txtNombreTabla")
        self.grbColumnas = QtWidgets.QGroupBox(frmCreacionTablas)
        self.grbColumnas.setGeometry(QtCore.QRect(20, 110, 451, 101))
        self.grbColumnas.setObjectName("grbColumnas")
        self.lblNombreColumna = QtWidgets.QLabel(self.grbColumnas)
        self.lblNombreColumna.setGeometry(QtCore.QRect(47, 28, 81, 16))
        self.lblNombreColumna.setObjectName("lblNombreColumna")
        self.txtNombreColumna = QtWidgets.QLineEdit(self.grbColumnas)
        self.txtNombreColumna.setGeometry(QtCore.QRect(21, 51, 131, 20))
        self.txtNombreColumna.setObjectName("txtNombreColumna")
        self.lblTipoDato = QtWidgets.QLabel(self.grbColumnas)
        self.lblTipoDato.setGeometry(QtCore.QRect(200, 28, 61, 16))
        self.lblTipoDato.setObjectName("lblTipoDato")
        self.cmbTipoDato = QtWidgets.QComboBox(self.grbColumnas)
        self.cmbTipoDato.setGeometry(QtCore.QRect(161, 51, 140, 20))
        self.cmbTipoDato.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.cmbTipoDato.setObjectName("cmbTipoDato")
        self.cmbTipoDato.addItem("")
        self.cmbTipoDato.addItem("")
        self.cmbTipoDato.addItem("")
        self.btnAgregarColumna = QtWidgets.QPushButton(self.grbColumnas)
        self.btnAgregarColumna.setGeometry(QtCore.QRect(310, 49, 121, 23))
        self.btnAgregarColumna.setObjectName("btnAgregarColumna")
        self.btnCrearBBDD = QtWidgets.QPushButton(frmCreacionTablas)
        self.btnCrearBBDD.setGeometry(QtCore.QRect(251, 230, 221, 23))
        self.btnCrearBBDD.setObjectName("btnCrearBBDD")
        self.lblInformacion = QtWidgets.QLabel(frmCreacionTablas)
        self.lblInformacion.setGeometry(QtCore.QRect(20, 274, 81, 16))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.lblInformacion.setFont(font)
        self.lblInformacion.setObjectName("lblInformacion")
        self.txtInformacion = QtWidgets.QLineEdit(frmCreacionTablas)
        self.txtInformacion.setGeometry(QtCore.QRect(110, 272, 361, 20))
        self.txtInformacion.setReadOnly(True)
        self.txtInformacion.setObjectName("txtInformacion")

        self.retranslateUi(frmCreacionTablas)
        QtCore.QMetaObject.connectSlotsByName(frmCreacionTablas)
        frmCreacionTablas.setTabOrder(self.txtNombreBBDD, self.txtNombreTabla)
        frmCreacionTablas.setTabOrder(self.txtNombreTabla, self.txtNombreColumna)
        frmCreacionTablas.setTabOrder(self.txtNombreColumna, self.cmbTipoDato)
        frmCreacionTablas.setTabOrder(self.cmbTipoDato, self.btnAgregarColumna)
        frmCreacionTablas.setTabOrder(self.btnAgregarColumna, self.btnCrearBBDD)
        frmCreacionTablas.setTabOrder(self.btnCrearBBDD, self.txtInformacion)
        frmCreacionTablas.setTabOrder(self.txtInformacion, self.txtNombreBBDD)

    def retranslateUi(self, frmCreacionTablas):
        _translate = QtCore.QCoreApplication.translate
        frmCreacionTablas.setWindowTitle(_translate("frmCreacionTablas", "Creación de Tablas"))
        self.lblNombreBBDD.setText(_translate("frmCreacionTablas", "Nombre de la Base de datos:"))
        self.lblNombreTabla.setText(_translate("frmCreacionTablas", "Nombre de la Tabla:"))
        self.grbColumnas.setTitle(_translate("frmCreacionTablas", " Columnas "))
        self.lblNombreColumna.setText(_translate("frmCreacionTablas", "Nombre columna"))
        self.lblTipoDato.setText(_translate("frmCreacionTablas", "Tipo de dato"))
        self.cmbTipoDato.setItemText(0, _translate("frmCreacionTablas", "INT"))
        self.cmbTipoDato.setItemText(1, _translate("frmCreacionTablas", "VARCHAR"))
        self.cmbTipoDato.setItemText(2, _translate("frmCreacionTablas", "FLOAT"))
        self.btnAgregarColumna.setText(_translate("frmCreacionTablas", "Agregar columna"))
        self.btnCrearBBDD.setText(_translate("frmCreacionTablas", "Crear Base de Datos"))
        self.lblInformacion.setText(_translate("frmCreacionTablas", "Información:"))

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Restaurante.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class frmRestaurante(object):
    def setupUi(self, frmRestaurante):
        frmRestaurante.setObjectName("frmRestaurante")
        frmRestaurante.resize(440, 170)
        self.tabRestaurante = QtWidgets.QTabWidget(frmRestaurante)
        self.tabRestaurante.setGeometry(QtCore.QRect(10, 10, 421, 151))
        self.tabRestaurante.setObjectName("tabRestaurante")
        self.tabMenu = QtWidgets.QWidget()
        self.tabMenu.setObjectName("tabMenu")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.tabMenu)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(10, 10, 111, 101))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.chkPizza = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkPizza.setObjectName("chkPizza")
        self.verticalLayout.addWidget(self.chkPizza)
        self.chkPasta = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkPasta.setObjectName("chkPasta")
        self.verticalLayout.addWidget(self.chkPasta)
        self.chkEspanola = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkEspanola.setObjectName("chkEspanola")
        self.verticalLayout.addWidget(self.chkEspanola)
        self.chkOriental = QtWidgets.QCheckBox(self.verticalLayoutWidget)
        self.chkOriental.setObjectName("chkOriental")
        self.verticalLayout.addWidget(self.chkOriental)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("menu.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabRestaurante.addTab(self.tabMenu, icon, "")
        self.tabFormaPago = QtWidgets.QWidget()
        self.tabFormaPago.setObjectName("tabFormaPago")
        self.verticalLayoutWidget_2 = QtWidgets.QWidget(self.tabFormaPago)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(10, 10, 101, 101))
        self.verticalLayoutWidget_2.setObjectName("verticalLayoutWidget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.rbnDebito = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbnDebito.setObjectName("rbnDebito")
        self.verticalLayout_2.addWidget(self.rbnDebito)
        self.rbnCredito = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbnCredito.setObjectName("rbnCredito")
        self.verticalLayout_2.addWidget(self.rbnCredito)
        self.rbnEfectivo = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbnEfectivo.setObjectName("rbnEfectivo")
        self.verticalLayout_2.addWidget(self.rbnEfectivo)
        self.rbnPaypal = QtWidgets.QRadioButton(self.verticalLayoutWidget_2)
        self.rbnPaypal.setObjectName("rbnPaypal")
        self.verticalLayout_2.addWidget(self.rbnPaypal)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("pago.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabRestaurante.addTab(self.tabFormaPago, icon1, "")
        self.tabDireccion = QtWidgets.QWidget()
        self.tabDireccion.setObjectName("tabDireccion")
        self.widget = QtWidgets.QWidget(self.tabDireccion)
        self.widget.setGeometry(QtCore.QRect(10, 10, 391, 74))
        self.widget.setObjectName("widget")
        self.formLayout = QtWidgets.QFormLayout(self.widget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.lblDireccion = QtWidgets.QLabel(self.widget)
        self.lblDireccion.setObjectName("lblDireccion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.lblDireccion)
        self.txtDireccion = QtWidgets.QLineEdit(self.widget)
        self.txtDireccion.setObjectName("txtDireccion")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txtDireccion)
        self.lblTelefono = QtWidgets.QLabel(self.widget)
        self.lblTelefono.setObjectName("lblTelefono")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.lblTelefono)
        self.txtTelefono = QtWidgets.QLineEdit(self.widget)
        self.txtTelefono.setObjectName("txtTelefono")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txtTelefono)
        self.lblEmail = QtWidgets.QLabel(self.widget)
        self.lblEmail.setObjectName("lblEmail")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.lblEmail)
        self.txtEmail = QtWidgets.QLineEdit(self.widget)
        self.txtEmail.setObjectName("txtEmail")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txtEmail)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("entrega.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.tabRestaurante.addTab(self.tabDireccion, icon2, "")

        self.retranslateUi(frmRestaurante)
        self.tabRestaurante.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(frmRestaurante)

    def retranslateUi(self, frmRestaurante):
        _translate = QtCore.QCoreApplication.translate
        frmRestaurante.setWindowTitle(_translate("frmRestaurante", "Restaurante"))
        self.chkPizza.setText(_translate("frmRestaurante", "Pizza"))
        self.chkPasta.setText(_translate("frmRestaurante", "Pasta"))
        self.chkEspanola.setText(_translate("frmRestaurante", "Comida Española"))
        self.chkOriental.setText(_translate("frmRestaurante", "Comida Oriental"))
        self.tabRestaurante.setTabText(self.tabRestaurante.indexOf(self.tabMenu), _translate("frmRestaurante", "Menú"))
        self.rbnDebito.setText(_translate("frmRestaurante", "Tarjeta Débito"))
        self.rbnCredito.setText(_translate("frmRestaurante", "Tarjeta Crédito"))
        self.rbnEfectivo.setText(_translate("frmRestaurante", "Efectivo"))
        self.rbnPaypal.setText(_translate("frmRestaurante", "PayPal"))
        self.tabRestaurante.setTabText(self.tabRestaurante.indexOf(self.tabFormaPago), _translate("frmRestaurante", "Forma de Pago"))
        self.lblDireccion.setText(_translate("frmRestaurante", "Dirección:"))
        self.lblTelefono.setText(_translate("frmRestaurante", "Teléfono:"))
        self.lblEmail.setText(_translate("frmRestaurante", "Email:"))
        self.tabRestaurante.setTabText(self.tabRestaurante.indexOf(self.tabDireccion), _translate("frmRestaurante", "Dirección de Entrega"))

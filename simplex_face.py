#Projeto de Otimização 1 - PPL(Python)
#Letícia Vitória Merss Moreira
#GES
#56

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(375, 214)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(170, 30, 113, 25))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_2.setGeometry(QtCore.QRect(170, 70, 113, 25))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 151, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 161, 17))
        self.label_2.setObjectName("label_2")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 160, 89, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_warning = QtWidgets.QLabel(Dialog)
        self.label_warning.setGeometry(QtCore.QRect(130, 160, 161, 17))
        self.label_warning.setText("")
        self.label_warning.setObjectName("label_warning")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(30, 130, 67, 17))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.radioButton_2 = QtWidgets.QRadioButton(Dialog)
        self.radioButton_2.setGeometry(QtCore.QRect(10, 110, 112, 23))
        self.radioButton_2.setObjectName("radioButton_2")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Simplex"))
        self.label.setText(_translate("Dialog", "Numero de variáveis:"))
        self.label_2.setText(_translate("Dialog", "Numero de restrições:"))
        self.pushButton.setText(_translate("Dialog", "Enviar"))
        self.radioButton_2.setText(_translate("Dialog", "Maximização"))
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitledSuzMQY.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import QMetaObject,QCoreApplication
from PySide2.QtGui import Qt
from PySide2.QtWidgets import QVBoxLayout,QSlider,QLabel,QDateTimeEdit,QLineEdit,QDialogButtonBox

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"GYM")
        Dialog.resize(424, 439)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.horizontalSlider = QSlider(Dialog)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setOrientation(Qt.Horizontal)

        self.verticalLayout.addWidget(self.horizontalSlider)

        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.dateTimeEdit_F = QDateTimeEdit(Dialog)
        self.dateTimeEdit_F.setObjectName(u"dateTimeEdit_F")
        self.dateTimeEdit_F.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateTimeEdit_F)

        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")

        self.verticalLayout.addWidget(self.label_4)

        self.dateTimeEdit_T = QDateTimeEdit(Dialog)
        self.dateTimeEdit_T.setObjectName(u"dateTimeEdit_T")
        self.dateTimeEdit_T.setContextMenuPolicy(Qt.NoContextMenu)
        self.dateTimeEdit_T.setCalendarPopup(True)

        self.verticalLayout.addWidget(self.dateTimeEdit_T)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.ID = QLineEdit(Dialog)
        self.ID.setObjectName(u"ID")
        self.ID.setInputMethodHints(Qt.ImhFormattedNumbersOnly)
        self.ID.setText()

        self.verticalLayout.addWidget(self.ID)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.pwd = QLineEdit(Dialog)
        self.pwd.setObjectName(u"pwd")
        self.pwd.setInputMethodHints(Qt.ImhHiddenText)

        self.verticalLayout.addWidget(self.pwd)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.verticalLayout.addWidget(self.buttonBox)


        self.retranslateUi(Dialog)
        self.dateTimeEdit_F.dateTimeChanged.connect(self.dateTimeEdit_T.setDateTime)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"Freq", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"From", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"To", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"ID", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"pwd", None))
    # retranslateUi
if __name__ == '__main__':
    print('该文件仅为ui，请打开main.py运行')


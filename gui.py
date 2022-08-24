# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'gymCNZCkG.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *
from time import sleep

class Ui_BNU_GYM(object):
    def __init__(self) -> None:
        self.flag = True
    def setupUi(self, BNU_GYM:QWidget):
        if not BNU_GYM.objectName():
            BNU_GYM.setObjectName(u"BNU_GYM")
        BNU_GYM.resize(814, 642)
        self.gridLayout = QGridLayout(BNU_GYM)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_8 = QLabel(BNU_GYM)
        self.label_8.setObjectName(u"label_8")

        self.gridLayout.addWidget(self.label_8, 3, 3, 1, 1)

        self.comboBox = QComboBox(BNU_GYM)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.gridLayout.addWidget(self.comboBox, 4, 1, 1, 1)

        self.line_2 = QFrame(BNU_GYM)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 5, 5, 1)

        self.label = QLabel(BNU_GYM)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.To = QDateTimeEdit(BNU_GYM)
        self.To.setObjectName(u"To")
        self.To.setDateTime(QDateTime(QDate(2022, 8, 23), QTime(0, 0, 0)))
        self.To.setCalendarPopup(True)

        self.gridLayout.addWidget(self.To, 2, 4, 1, 1)

        self.ID = QLineEdit(BNU_GYM)
        self.ID.setObjectName(u"ID")
        self.ID.setInputMethodHints(Qt.ImhFormattedNumbersOnly)

        self.gridLayout.addWidget(self.ID, 0, 1, 1, 1)

        self.Runtime = QLCDNumber(BNU_GYM)
        self.Runtime.setObjectName(u"Runtime")
        self.Runtime.setDigitCount(5)
        self.Runtime.setSegmentStyle(QLCDNumber.Flat)
        self.Runtime.setProperty("value", 0.000000000000000)
        self.Runtime.setProperty("intValue", 0)

        self.gridLayout.addWidget(self.Runtime, 3, 4, 1, 1)

        self.label_6 = QLabel(BNU_GYM)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout.addWidget(self.label_6, 2, 3, 1, 1)

        self.line = QFrame(BNU_GYM)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.VLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.gridLayout.addWidget(self.line, 0, 2, 5, 1)

        self.label_7 = QLabel(BNU_GYM)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout.addWidget(self.label_7, 3, 0, 1, 1)

        self.Num = QSpinBox(BNU_GYM)
        self.Num.setObjectName(u"Num")
        self.Num.setMaximum(5)
        self.Num.setValue(1)

        self.gridLayout.addWidget(self.Num, 3, 1, 1, 1)

        self.Tel = QLineEdit(BNU_GYM)
        self.Tel.setObjectName(u"Tel")
        self.Tel.setInputMethodHints(Qt.ImhDialableCharactersOnly)

        self.gridLayout.addWidget(self.Tel, 1, 4, 1, 1)

        self.Pwd = QLineEdit(BNU_GYM)
        self.Pwd.setObjectName(u"Pwd")
        self.Pwd.setInputMethodHints(Qt.ImhHiddenText)

        self.gridLayout.addWidget(self.Pwd, 1, 1, 1, 1)

        self.label_5 = QLabel(BNU_GYM)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 2, 0, 1, 1)

        self.From = QDateTimeEdit(BNU_GYM)
        self.From.setObjectName(u"From")
        self.From.setDateTime(QDateTime(QDate(2022, 8, 23), QTime(0, 0, 0)))
        self.From.setCalendarPopup(True)

        self.gridLayout.addWidget(self.From, 2, 1, 1, 1)

        self.textBrowser = QTextBrowser(BNU_GYM)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setContextMenuPolicy(Qt.NoContextMenu)

        self.gridLayout.addWidget(self.textBrowser, 0, 6, 5, 1)

        self.Rate = QSlider(BNU_GYM)
        self.Rate.setObjectName(u"Rate")
        self.Rate.setMinimum(1)
        self.Rate.setValue(50)
        self.Rate.setOrientation(Qt.Horizontal)
        self.Rate.setInvertedAppearance(False)
        self.Rate.setTickPosition(QSlider.TicksAbove)
        self.Rate.setTickInterval(10)

        self.gridLayout.addWidget(self.Rate, 4, 4, 1, 1)

        self.label_9 = QLabel(BNU_GYM)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout.addWidget(self.label_9, 4, 0, 1, 1)

        self.label_4 = QLabel(BNU_GYM)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 1, 3, 1, 1)

        self.label_3 = QLabel(BNU_GYM)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)

        self.label_2 = QLabel(BNU_GYM)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 0, 3, 1, 1)

        self.label_10 = QLabel(BNU_GYM)
        self.label_10.setObjectName(u"label_10")

        self.gridLayout.addWidget(self.label_10, 4, 3, 1, 1)

        self.Name = QLineEdit(BNU_GYM)
        self.Name.setObjectName(u"Name")

        self.gridLayout.addWidget(self.Name, 0, 4, 1, 1)

        self.label_11 = QLabel(BNU_GYM)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout.addWidget(self.label_11, 5, 6, 1, 1)

        self.Begin = QPushButton(BNU_GYM)
        self.Begin.setObjectName(u"Begin")

        self.gridLayout.addWidget(self.Begin, 5, 1, 1, 1)

        self.Cancel = QPushButton(BNU_GYM)
        self.Cancel.setObjectName(u"Cancel")

        self.gridLayout.addWidget(self.Cancel, 5, 4, 1, 1)

        QWidget.setTabOrder(self.ID, self.Name)
        QWidget.setTabOrder(self.Name, self.Pwd)
        QWidget.setTabOrder(self.Pwd, self.Tel)
        QWidget.setTabOrder(self.Tel, self.From)
        QWidget.setTabOrder(self.From, self.To)
        QWidget.setTabOrder(self.To, self.Num)
        QWidget.setTabOrder(self.Num, self.comboBox)
        QWidget.setTabOrder(self.comboBox, self.Rate)
        QWidget.setTabOrder(self.Rate, self.textBrowser)

        self.retranslateUi(BNU_GYM)
        self.From.dateTimeChanged.connect(self.To.setDateTime)
        self.comboBox.currentIndexChanged.connect(self.Num.clear)

        QMetaObject.connectSlotsByName(BNU_GYM)
        self.set_action(BNU_GYM)
    # setupUi

    def retranslateUi(self, BNU_GYM:QWidget):
        BNU_GYM.setWindowTitle(QCoreApplication.translate("BNU_GYM", u"Dialog", None))
        self.label_8.setText(QCoreApplication.translate("BNU_GYM", u"Runtime", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("BNU_GYM", u"\u7fbd\u6bdb\u7403", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("BNU_GYM", u"\u4e52\u4e53\u7403", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("BNU_GYM", u"\u7f51\u7403", None))

        self.label.setText(QCoreApplication.translate("BNU_GYM", u"ID", None))
        self.ID.setText("")
        self.ID.setPlaceholderText("")
        self.label_6.setText(QCoreApplication.translate("BNU_GYM", u"To", None))
        self.label_7.setText(QCoreApplication.translate("BNU_GYM", u"Num", None))
        self.Tel.setText("")
        self.Pwd.setText("")
        self.label_5.setText(QCoreApplication.translate("BNU_GYM", u"From", None))
        self.label_9.setText(QCoreApplication.translate("BNU_GYM", u"Type", None))
        self.label_4.setText(QCoreApplication.translate("BNU_GYM", u"Tel", None))
        self.label_3.setText(QCoreApplication.translate("BNU_GYM", u"Pwd", None))
        self.label_2.setText(QCoreApplication.translate("BNU_GYM", u"Name", None))
        self.label_10.setText(QCoreApplication.translate("BNU_GYM", u"Rate", None))
        self.Name.setText("")
        self.label_11.setText(QCoreApplication.translate("BNU_GYM", u"\u672cApp\u4ec5\u4f9b\u5b66\u4e60\uff0c\u4e0d\u5f97\u7528\u4f5c\u5546\u4e1a\u76ee\u7684", None))
        self.Begin.setText(QCoreApplication.translate("BNU_GYM", u"Begin", None))
        self.Cancel.setText(QCoreApplication.translate("BNU_GYM", u"Cancel", None))
    # retranslateUi
    def set_action(self,BNU_GYM:QWidget):
        self.Begin.clicked.connect(self.click_begin,Qt.UniqueConnection)
        self.Cancel.clicked.connect(self.click_cancel,Qt.UniqueConnection)
    def click_begin(self):
        while True:
            sleep(10)
            # params = {
            #     'id':self.ID.text().strip(),
            #     'pwd':self.Pwd.text().strip(),
            #     'name':self.Name.text().strip(),
            #     'tel':self.Tel.text().strip(),
            #     'rate':max(min(0.1,self.Rate.value()/10),min(self.Rate.value()/10,10.)),
            #     'type':self.comboBox.currentText(),
            # }
            if self.flag:
                self.textBrowser.append('k\talfmd'+'\n')
            else:
                self.textBrowser.append('---- end ----\n')
                self.flag=True
                break
    def click_cancel(self):
        self.flag = False






from sys import argv,exit
if __name__=='__main__':
    app = QApplication(argv)
    widget = QWidget()
    ui = Ui_BNU_GYM()
    ui.setupUi(widget)
    widget.show()
    exit(app.exec_())
from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(290, 432)
        Dialog.setMinimumSize(QSize(290, 432))
        Dialog.setMaximumSize(QSize(290, 432))
        icon = QIcon()
        icon.addFile(u"../../../Downloads/exe.ico",
                     QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setStyleSheet(u"background: #292929;")
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 80, 61, 61))
        font = QFont()
        font.setFamilies([u"Montserrat"])
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"border: 3px solid #616161;\n"
                                      "border-radius: 3px;\n"
                                      "color: #fff;")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 271, 61))
        font1 = QFont()
        font1.setFamilies([u"Montserrat"])
        font1.setPointSize(24)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border: 3px solid #616161;\n"
                                 "color: #e6e6e6;\n"
                                 "border-radius: 3px;\n"
                                 "background: #1f1f1f;\n"
                                 "\n"
                                 "")
        self.label.setAlignment(
            Qt.AlignRight | Qt.AlignTrailing | Qt.AlignVCenter)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(80, 80, 61, 61))
        font2 = QFont()
        font2.setPointSize(16)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(150, 80, 61, 61))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(220, 80, 61, 61))
        self.pushButton_4.setFont(font2)
        self.pushButton_4.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(10, 150, 61, 61))
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_6 = QPushButton(Dialog)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(80, 150, 61, 61))
        self.pushButton_6.setFont(font2)
        self.pushButton_6.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_7 = QPushButton(Dialog)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(150, 150, 61, 61))
        self.pushButton_7.setFont(font2)
        self.pushButton_7.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(220, 150, 61, 61))
        self.pushButton_8.setFont(font2)
        self.pushButton_8.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(10, 220, 61, 61))
        self.pushButton_9.setFont(font2)
        self.pushButton_9.setStyleSheet(u"border: 3px solid #616161;\n"
                                        "border-radius: 3px;\n"
                                        "color: #fff;")
        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(80, 220, 61, 61))
        self.pushButton_10.setFont(font2)
        self.pushButton_10.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")
        self.pushButton_11 = QPushButton(Dialog)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(150, 220, 61, 61))
        self.pushButton_11.setFont(font2)
        self.pushButton_11.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")
        self.pushButton_12 = QPushButton(Dialog)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(220, 220, 61, 61))
        self.pushButton_12.setFont(font2)
        self.pushButton_12.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")
        self.pushButton_14 = QPushButton(Dialog)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setGeometry(QRect(80, 290, 61, 61))
        self.pushButton_14.setFont(font2)
        self.pushButton_14.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")
        self.pushButton_15 = QPushButton(Dialog)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setGeometry(QRect(150, 290, 61, 61))
        self.pushButton_15.setFont(font2)
        self.pushButton_15.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")
        self.pushButton_16 = QPushButton(Dialog)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(220, 290, 61, 61))
        self.pushButton_16.setFont(font2)
        self.pushButton_16.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")
        self.pushButton_18 = QPushButton(Dialog)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(150, 360, 131, 61))
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "background: #1f1f1f;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")
        self.pushButton_20 = QPushButton(Dialog)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(10, 290, 61, 131))
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;\n"
                                         "background: #1f1f1f;")
        self.pushButton_21 = QPushButton(Dialog)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(80, 360, 61, 61))
        self.pushButton_21.setFont(font2)
        self.pushButton_21.setStyleSheet(u"border: 3px solid #616161;\n"
                                         "border-radius: 3px;\n"
                                         "color: #fff;")

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QCoreApplication.translate("Dialog", u"PyCalc", None))
        self.pushButton.setText(
            QCoreApplication.translate("Dialog", u"1", None))
        self.label.setText("")
        self.pushButton_2.setText(
            QCoreApplication.translate("Dialog", u"2", None))
        self.pushButton_3.setText(
            QCoreApplication.translate("Dialog", u"3", None))
        self.pushButton_4.setText(
            QCoreApplication.translate("Dialog", u"+", None))
        self.pushButton_5.setText(
            QCoreApplication.translate("Dialog", u"4", None))
        self.pushButton_6.setText(
            QCoreApplication.translate("Dialog", u"5", None))
        self.pushButton_7.setText(
            QCoreApplication.translate("Dialog", u"6", None))
        self.pushButton_8.setText(
            QCoreApplication.translate("Dialog", u"-", None))
        self.pushButton_9.setText(
            QCoreApplication.translate("Dialog", u"7", None))
        self.pushButton_10.setText(
            QCoreApplication.translate("Dialog", u"8", None))
        self.pushButton_11.setText(
            QCoreApplication.translate("Dialog", u"9", None))
        self.pushButton_12.setText(
            QCoreApplication.translate("Dialog", u"\u00d7", None))
        self.pushButton_14.setText(
            QCoreApplication.translate("Dialog", u"0", None))
        self.pushButton_15.setText(
            QCoreApplication.translate("Dialog", u"%", None))
        self.pushButton_16.setText(
            QCoreApplication.translate("Dialog", u"\u00f7", None))
        self.pushButton_18.setText(
            QCoreApplication.translate("Dialog", u"=", None))
        self.pushButton_20.setText(
            QCoreApplication.translate("Dialog", u"C", None))
        self.pushButton_21.setText(
            QCoreApplication.translate("Dialog", u".", None))

    def keyPressEvent(self, e):

        print(e)

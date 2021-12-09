# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Login.ui'
##
## Created by: Qt User Interface Compiler version 6.2.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(354, 478)
        self.frame = QFrame(Login)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(20, 130, 311, 321))
        self.frame.setStyleSheet(u"background-color: rgb(106, 108, 217);")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.txt_usuario = QLineEdit(self.frame)
        self.txt_usuario.setObjectName(u"txt_usuario")
        self.txt_usuario.setGeometry(QRect(50, 90, 211, 51))
        self.txt_usuario.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.txt_usuario.setAlignment(Qt.AlignCenter)
        self.txt_senha = QLineEdit(self.frame)
        self.txt_senha.setObjectName(u"txt_senha")
        self.txt_senha.setGeometry(QRect(50, 160, 211, 51))
        self.txt_senha.setStyleSheet(u"background-color: rgb(226, 226, 226);")
        self.txt_senha.setEchoMode(QLineEdit.Password)
        self.txt_senha.setAlignment(Qt.AlignCenter)
        self.btn_entrar = QPushButton(self.frame)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(154, 250, 101, 41))
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(17, 107, 16);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(50, 250, 101, 41))
        self.pushButton_2.setFont(font)
        self.pushButton_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgb(255, 75, 69);")

        self.retranslateUi(Login)
        self.pushButton_2.clicked.connect(Login.close)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.txt_usuario.setPlaceholderText(QCoreApplication.translate("Login", u"Digite o um nome de Usu\u00e1rio", None))
        self.txt_senha.setPlaceholderText(QCoreApplication.translate("Login", u"Digite a senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("Login", u"Entrar", None))
        self.pushButton_2.setText(QCoreApplication.translate("Login", u"Cancelar", None))
    # retranslateUi


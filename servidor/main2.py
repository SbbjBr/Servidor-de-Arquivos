from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(456, 260)
        MainWindow.setMinimumSize(QtCore.QSize(456, 260))
        MainWindow.setMaximumSize(QtCore.QSize(456, 260))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        MainWindow.setPalette(palette)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 20, 231, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")


        self.label_ip = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ip.setObjectName("label_ip")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ip)


        self.label_porta = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_porta.setObjectName("label_porta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_porta)


        self.textEdit_ip = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_ip.setObjectName("textEdit_ip")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_ip)


        self.textEdit_porta = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_porta.setObjectName("textEdit_porta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_porta)


        self.label_tempo_aberto_m = QtWidgets.QLabel(self.centralwidget)
        self.label_tempo_aberto_m.setGeometry(QtCore.QRect(30, 150, 158, 16))
        self.label_tempo_aberto_m.setObjectName("label_tempo_aberto_m")

        self.botao_parar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_parar.setGeometry(QtCore.QRect(10, 220, 158, 24))
        self.botao_parar.setObjectName("botao_parar")

        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(230, 150, 239, 16))
        self.label_status.setObjectName("label_status")

        self.label_ip_botao = QtWidgets.QLabel(self.centralwidget)
        self.label_ip_botao.setGeometry(QtCore.QRect(230, 180, 239, 16))
        self.label_ip_botao.setObjectName("label_ip_botao")

        self.botao_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_iniciar.setGeometry(QtCore.QRect(200, 220, 239, 24))
        self.botao_iniciar.setObjectName("botao_iniciar")

        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 411, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")

        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        self.textEdit_caminho = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit_caminho.setObjectName("textEdit_caminho")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_caminho)

        self.label_caminho = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_caminho.setObjectName("label_caminho")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_caminho)

        self.lcdnumero = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdnumero.setGeometry(QtCore.QRect(40, 180, 81, 23))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        self.lcdnumero.setPalette(palette)
        self.lcdnumero.setObjectName("lcdnumero")


        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 135, 531, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")


        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 180, 49, 16))
        self.label.setObjectName("label")


        self.spinBox_tempo = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_tempo.setGeometry(QtCore.QRect(35, 50, 81, 22))
        self.spinBox_tempo.setMaximum(99999)
        self.spinBox_tempo.setObjectName("spinBox_tempo")
        self.spinBox_tempo.setDisabled(True)

        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 131, 20))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.botao_iniciar.clicked['bool'].connect(self.textEdit_porta.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.textEdit_ip.setEnabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.textEdit_porta.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.textEdit_ip.setDisabled) # type: ignore
        self.checkBox.clicked['bool'].connect(self.spinBox_tempo.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.textEdit_caminho.setEnabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.textEdit_caminho.setDisabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.spinBox_tempo.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.checkBox.setEnabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.spinBox_tempo.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.checkBox.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit_ip, self.textEdit_porta)
        MainWindow.setTabOrder(self.textEdit_porta, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.spinBox_tempo)
        MainWindow.setTabOrder(self.spinBox_tempo, self.textEdit_caminho)
        MainWindow.setTabOrder(self.textEdit_caminho, self.botao_iniciar)
        MainWindow.setTabOrder(self.botao_iniciar, self.botao_parar)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Servidor de Arquivos - Lucas Rocha"))
        self.label_ip.setText(_translate("MainWindow", "IP:"))
        self.label_porta.setText(_translate("MainWindow", "Porta:"))
        self.label_tempo_aberto_m.setText(_translate("MainWindow", "Tempo Servidor Aberto:"))
        self.botao_parar.setText(_translate("MainWindow", "Parar"))
        self.label_status.setText(_translate("MainWindow", "Status:         Parado"))
        self.label_ip_botao.setText(_translate("MainWindow", "IP:"))
        self.botao_iniciar.setText(_translate("MainWindow", "Clique para iniciar"))
        self.label_caminho.setText(_translate("MainWindow", "Caminho:"))
        self.label.setText(_translate("MainWindow", "minutos"))
        self.checkBox.setText(_translate("MainWindow", "Com tempo limite?"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

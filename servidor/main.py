from threading import Thread
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox
import sys

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Servidor de Arquivos - Lucas Rocha")
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

        self.formLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget_2.setGeometry(QtCore.QRect(20, 100, 411, 31))
        self.formLayoutWidget_2.setObjectName("formLayoutWidget_2")

        self.formLayout_2 = QtWidgets.QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.formLayout_2.setObjectName("formLayout_2")

        
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 20, 231, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")

        
        #=================================== Label imutaveis =====================================

        self.label_ip = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ip.setObjectName("label_ip")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ip)
        self.label_ip.setText("IP:")


        self.label_porta = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_porta.setObjectName("label_porta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_porta)
        self.label_porta.setText("Porta:")

        self.label_tempo_aberto_m = QtWidgets.QLabel(self.centralwidget)
        self.label_tempo_aberto_m.setGeometry(QtCore.QRect(30, 150, 158, 16))
        self.label_tempo_aberto_m.setObjectName("label_tempo_aberto_m")
        self.label_tempo_aberto_m.setText("Tempo Servidor Aberto:")

        self.label_caminho = QtWidgets.QLabel(self.formLayoutWidget_2)
        self.label_caminho.setObjectName("label_caminho")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_caminho)
        self.label_caminho.setText("Caminho:")

        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(130, 180, 49, 16))
        self.label.setObjectName("label")
        self.label.setText("minutos")

        
        # ========================================================================================

        #=================================== Label mutaveis ======================================
        
        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(230, 150, 239, 16))
        self.label_status.setObjectName("label_status")
        self.label_status.setText("Status:         Parado")
        
        self.label_ip_botao = QtWidgets.QLabel(self.centralwidget)
        self.label_ip_botao.setGeometry(QtCore.QRect(230, 180, 239, 16))
        self.label_ip_botao.setObjectName("label_ip_botao")
        self.label_ip_botao.setText("IP:")
        # ========================================================================================

        #=================================== Text edit ======================================

        self.textEdit_ip = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_ip.setObjectName("textEdit_ip")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_ip)
        self.textEdit_ip.setPlaceholderText("'localhost' ou seu ipv4")


        self.textEdit_porta = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_porta.setObjectName("textEdit_porta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_porta)
        self.textEdit_porta.setPlaceholderText("8000")

        self.textEdit_caminho = QtWidgets.QTextEdit(self.formLayoutWidget_2)
        self.textEdit_caminho.setObjectName("textEdit_caminho")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_caminho)
        self.textEdit_caminho.setPlaceholderText("Caminho de uma pasta especifica ou deixe vazio")
        # ========================================================================================
        #=================================== Botão ======================================

        self.botao_parar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_parar.setGeometry(QtCore.QRect(10, 220, 158, 24))
        self.botao_parar.setObjectName("botao_parar")
        self.botao_parar.setText("Parar")
        self.botao_parar.setDisabled(True)

        self.botao_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_iniciar.setGeometry(QtCore.QRect(200, 220, 239, 24))
        self.botao_iniciar.setObjectName("botao_iniciar")
        self.botao_iniciar.setText("Clique para iniciar")
        # ========================================================================================

        #=================================== Widgets ======================================

        self.spinBox_tempo = QtWidgets.QSpinBox(self.centralwidget)
        self.spinBox_tempo.setGeometry(QtCore.QRect(35, 50, 81, 22))
        self.spinBox_tempo.setMinimum(1)
        self.spinBox_tempo.setMaximum(99999)
        self.spinBox_tempo.setObjectName("spinBox_tempo")
        self.spinBox_tempo.setDisabled(True)


        self.label_lado = QtWidgets.QLabel(self.centralwidget)
        self.label_lado.setObjectName("label_lado")
        self.label_lado.setGeometry(QtCore.QRect(125, 55, 10, 10))
        self.label_lado.setText("m")
        self.label_lado.setDisabled(True)


        
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(20, 20, 150, 20))
        self.checkBox.setObjectName("checkBox")
        MainWindow.setCentralWidget(self.centralwidget)
        self.checkBox.setText("Fechar automaticamente?")
        self.checkBox.clicked['bool'].connect(self.label_lado.setEnabled) # type: ignore

        
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
        # ========================================================================================

        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(-20, 135, 531, 21))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")

        self.botao_iniciar.clicked['bool'].connect(self.textEdit_porta.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.textEdit_ip.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.botao_iniciar.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.botao_parar.setDisabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.spinBox_tempo.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.checkBox.setEnabled) # type: ignore

        self.botao_iniciar.clicked['bool'].connect(self.label_lado.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.label_ip.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.label_porta.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.label_caminho.setEnabled) # type: ignore

        
        self.botao_parar.clicked['bool'].connect(self.textEdit_porta.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.textEdit_ip.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.textEdit_caminho.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.spinBox_tempo.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.checkBox.setDisabled) # type: ignore

        self.botao_parar.clicked['bool'].connect(self.label_lado.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.label_ip.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.label_porta.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.label_caminho.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.botao_iniciar.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.botao_parar.setEnabled) # type: ignore

        self.checkBox.clicked['bool'].connect(self.spinBox_tempo.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.textEdit_caminho.setEnabled) # type: ignore


        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.textEdit_ip, self.textEdit_porta)
        MainWindow.setTabOrder(self.textEdit_porta, self.checkBox)
        MainWindow.setTabOrder(self.checkBox, self.spinBox_tempo)
        MainWindow.setTabOrder(self.spinBox_tempo, self.textEdit_caminho)
        MainWindow.setTabOrder(self.textEdit_caminho, self.botao_iniciar)
        MainWindow.setTabOrder(self.botao_iniciar, self.botao_parar)

        #========================   Funções botões ============================================
        self.botao_iniciar.clicked.connect(self.click_abrir_servidor)
        self.botao_parar.clicked.connect(self.click_fechar_servidor)
        MainWindow.show()

    def abrir_servidor(self):
        import os
        import http.server
        import socketserver
        global httpd
        global servidor_aberto
        global IP, PORT


        if self.textEdit_ip.toPlainText() == "": # Ip
            IP = ""
        else:
            IP = self.textEdit_ip.toPlainText()
        

        if self.textEdit_ip.toPlainText() == "": #Porta
            PORT = 8000
        else:
            PORT = self.textEdit_ip.toPlainText()



        if self.textEdit_caminho.toPlainText() == "": #Caminho
            os.chdir(sys.path[0])
        else:
            try:
                os.chdir(self.textEdit_caminho.toPlainText())
            except:
                os.chdir(sys.path[0])

        Handler = http.server.SimpleHTTPRequestHandler
        httpd = socketserver.TCPServer((IP, PORT), Handler)

        if IP == "":
            self.label_ip_botao.setText(f"IP:    ipv4 ou 'localhost':{PORT}")
        else:
            self.label_ip_botao.setText(f"{IP}:{PORT}")
        self.label_status.setText("Status:         Iniciado")

        httpd.serve_forever()


    def cronometro(self):
        import time
        import os

        if self.checkBox.isChecked() != 0:
            time.sleep(int(self.spinBox_tempo.text())*60)
            os.system(f'cmd /c "taskkill /F /PID {os.getpid()}')

    def click_abrir_servidor(self):
        import threading
        global abrir_servidor

        abrir_servidor = threading.Thread(target=self.abrir_servidor)
        abrir_servidor.start()

        abrir_relogio = threading.Thread(target=self.relogio)
        abrir_relogio.start()

        abrir_cronometro = threading.Thread(target=self.cronometro)
        abrir_cronometro.start()


    def click_fechar_servidor(self):
        popup = QtWidgets.QMessageBox()
        popup.setWindowTitle("Confirmação")
        popup.setText("Para parar o servidor você precisa fechar o app. Confirmar?")
        popup.setIcon(QMessageBox.Warning)
        popup.setStandardButtons(QMessageBox.No|QMessageBox.Yes)
        popup.buttonClicked.connect(self.popup_button)
        popup.exec_()
    
    def popup_button(self, i):
        import os

        if i.text() == "&Yes":
            os.system(f'cmd /c "taskkill /F /PID {os.getpid()}')

    def relogio(self):
        import time

        self.minutos = 1

        while True:
            time.sleep(60)
            self.lcdnumero.display(self.minutos)
            self.minutos += 1
    
class MyWindow(QtWidgets.QMainWindow):
    def closeEvent(self,event):
        import os
        os.system(f'cmd /c "taskkill /F /PID {os.getpid()}')

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = MyWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    sys.exit(app.exec_())
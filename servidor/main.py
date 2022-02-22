from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):     
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowTitle("Servidor de Arquivos - Lucas Rocha")
        MainWindow.resize(456, 185)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(170, 20, 241, 61))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        MainWindow.setCentralWidget(self.centralwidget)


        # ================== Labels imutaveis ===========================================
        self.label_tempo_aberto_m = QtWidgets.QLabel(self.centralwidget)        
        self.label_tempo_aberto_m.setGeometry(QtCore.QRect(20, 20, 158, 16))
        self.label_tempo_aberto_m.setObjectName("label_tempo_aberto_m")
        self.label_tempo_aberto_m.setText("Tempo Servidor Aberto:")

        self.label_ip = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_ip.setObjectName("label_ip")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_ip)
        self.label_ip.setText("IP:")

        self.label_porta = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_porta.setObjectName("label_porta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_porta)
        self.label_porta.setText("Porta:")
        # =============================================================================


        # =================== Labels mutaveis =========================================
        self.label_minutos = QtWidgets.QLabel(self.centralwidget)
        self.label_minutos.setGeometry(QtCore.QRect(60, 50, 158, 16))
        self.label_minutos.setObjectName("label_minutos")
        self.label_minutos.setText("0 minutos")

        self.label_status = QtWidgets.QLabel(self.centralwidget)
        self.label_status.setGeometry(QtCore.QRect(240, 90, 239, 16))
        self.label_status.setObjectName("label_status")
        self.label_status.setText("Status:         Parado")

        self.label_ip_botao = QtWidgets.QLabel(self.centralwidget)
        self.label_ip_botao.setGeometry(QtCore.QRect(240, 120, 239, 16))
        self.label_ip_botao.setObjectName("label_ip_botao")
        self.label_ip_botao.setText("IP:")
        # =============================================================================


        # ========== Text Box =========================================================
        self.textEdit_ip = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_ip.setObjectName("textEdit_ip")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.textEdit_ip)
        self.textEdit_ip.setPlaceholderText("localhost")
        self.textEdit_ip.setReadOnly(True)

        self.textEdit_porta = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_porta.setObjectName("textEdit_porta")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_porta)
        self.textEdit_porta.setPlaceholderText("8000")
        self.textEdit_porta.setText("8000")
        # =============================================================================
        
        
        # ========================= Botões ============================================
        self.botao_iniciar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_iniciar.setGeometry(QtCore.QRect(200, 150, 239, 24))
        self.botao_iniciar.setObjectName("botao_iniciar")
        self.botao_iniciar.setText("Clique para iniciar")
        self.botao_iniciar.clicked.connect(self.click_iniciar)

        self.botao_parar = QtWidgets.QPushButton(self.centralwidget)
        self.botao_parar.setGeometry(QtCore.QRect(10, 150, 158, 24))
        self.botao_parar.setObjectName("botao_parar")
        self.botao_parar.setText("Parar")
        #self.botao_iniciar.clicked.connect(self.parar_servidor)
        # =============================================================================


        #signals
        self.botao_iniciar.clicked['bool'].connect(self.textEdit_porta.setEnabled) # type: ignore
        self.botao_iniciar.clicked['bool'].connect(self.textEdit_ip.setEnabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.textEdit_porta.setDisabled) # type: ignore
        self.botao_parar.clicked['bool'].connect(self.textEdit_ip.setDisabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(MainWindow)


    def click_iniciar(self):
        import threading

        thread = threading.Thread(target = self.iniciar_servidor)
        thread.start()

    def iniciar_servidor(self):
        import http.server
        import socketserver
        import time

        self.PORT = 8000

        self.Handler = http.server.SimpleHTTPRequestHandler
        self.httpd = socketserver.TCPServer(("", self.PORT), self.Handler)

        self.httpd.serve_forever()

        time.sleep(10)

        self.httpd.shutdown()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

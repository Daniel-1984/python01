# main.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QPushButton, QVBoxLayout, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QFile, QTextStream
from add_atendimento import AddAtendimentoWindow
from list_atendimentos import ListAtendimentosWindow
from models import Database

class MainApp(QMainWindow):
    def __init__(self, db):
        super().__init__()
        
        self.setWindowTitle("Interface Moderna")
        self.setGeometry(100, 100, 400, 200)
        # Carregar o arquivo de estilo
        style_file = QFile("style.css")
        style_file.open(QFile.ReadOnly | QFile.Text)
        style_stream = QTextStream(style_file)
        style = style_stream.readAll()
        self.setStyleSheet(style)
        style_file.close()
        # Botão personalizado
        button = QPushButton("Clique em Mim!", self)
        button.setGeometry(150, 80, 100, 40)
        button.setIcon(QIcon("icon.png"))  # Substitua "icon.png" pelo seu ícone personalizado
        button.clicked.connect(self.on_button_click)
    def on_button_click(self):
        print("Botão foi clicado!")


        self.db = db
        self.setWindowTitle("Gerenciador de Atendimentos")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.add_button = QPushButton("Adicionar Atendimento")
        self.add_button.clicked.connect(self.open_add_atendimento_window)

        self.list_button = QPushButton("Listar Atendimentos")
        self.list_button.clicked.connect(self.open_list_atendimentos_window)

        layout.addWidget(self.add_button)
        layout.addWidget(self.list_button)

        central_widget.setLayout(layout)

    def open_add_atendimento_window(self):
        self.add_window = AddAtendimentoWindow(self.db)
        self.add_window.show()

    def open_list_atendimentos_window(self):
        self.list_window = ListAtendimentosWindow(self.db)
        self.list_window.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = Database("db/mydatabase.db")
    window = MainApp(db)
    window.show()
    sys.exit(app.exec_())

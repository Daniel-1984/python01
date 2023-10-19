# add_atendimento.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
from models import Database, Atendimento

class AddAtendimentoWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()

        self.db = db
        self.setWindowTitle("Adicionar Atendimento")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.periodo_label = QLabel("Período:")
        self.periodo_entry = QLineEdit()

        self.assinatura_label = QLabel("Assinatura:")
        self.assinatura_entry = QLineEdit()

        self.data_label = QLabel("Data:")
        self.data_entry = QLineEdit()

        self.horario_label = QLabel("Horário:")
        self.horario_entry = QLineEdit()

        self.atendente_label = QLabel("Atendente:")
        self.atendente_entry = QLineEdit()

        self.comentario_label = QLabel("Comentário:")
        self.comentario_entry = QLineEdit()

        self.add_button = QPushButton("Adicionar Atendimento")
        self.add_button.clicked.connect(self.add_atendimento)

        layout.addWidget(self.periodo_label)
        layout.addWidget(self.periodo_entry)
        layout.addWidget(self.assinatura_label)
        layout.addWidget(self.assinatura_entry)
        layout.addWidget(self.data_label)
        layout.addWidget(self.data_entry)
        layout.addWidget(self.horario_label)
        layout.addWidget(self.horario_entry)
        layout.addWidget(self.atendente_label)
        layout.addWidget(self.atendente_entry)
        layout.addWidget(self.comentario_label)
        layout.addWidget(self.comentario_entry)
        layout.addWidget(self.add_button)

        central_widget.setLayout(layout)

    def add_atendimento(self):
        periodo = self.periodo_entry.text()
        assinatura = self.assinatura_entry.text()
        data = self.data_entry.text()
        horario = self.horario_entry.text()
        atendente = self.atendente_entry.text()
        comentario = self.comentario_entry.text()

        atendimento = Atendimento(periodo, assinatura, data, horario, atendente, comentario)
        self.db.insert_atendimento(atendimento)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = Database("db/mydatabase.db")
    window = AddAtendimentoWindow(db)
    window.show()
    sys.exit(app.exec_())


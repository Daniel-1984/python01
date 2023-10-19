# list_atendimentos.py
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QVBoxLayout, QWidget
from models import Database

class ListAtendimentosWindow(QMainWindow):
    def __init__(self, db):
        super().__init__()

        self.db = db
        self.setWindowTitle("Listar Atendimentos")

        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        layout = QVBoxLayout()

        self.atendimentos_label = QLabel("Lista de Atendimentos:")
        self.atendimentos_text = QLabel()
        self.update_atendimentos_text()

        layout.addWidget(self.atendimentos_label)
        layout.addWidget(self.atendimentos_text)

        central_widget.setLayout(layout)

    def update_atendimentos_text(self):
        atendimentos = self.db.get_all_atendimentos()
        text = "\n".join([f"Período: {atendimento[1]}, Assinatura: {atendimento[2]}, Data: {atendimento[3]}, Horário: {atendimento[4]}, Atendente: {atendimento[5]}, Comentário: {atendimento[6]}" for atendimento in atendimentos])
        self.atendimentos_text.setText(text)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    db = Database("db/mydatabase.db")
    window = ListAtendimentosWindow(db)
    window.show()
    sys.exit(app.exec_())

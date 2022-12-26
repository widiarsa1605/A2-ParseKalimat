from PyQt6.QtWidgets import (
    QApplication, QVBoxLayout, QWidget, QLabel, QPushButton, QLineEdit, QTextEdit, QGridLayout, QScrollArea, QGroupBox
)
from PyQt6.QtCore import Qt

import sys
import parsing
import konversiCNF

# set of rules Bahasa Indonesia yang sudah dalam bentuk Chomsky Normal Form
my_file = open("cfgRule.txt", "r")
data = my_file.read()
cfgRule = data.split("\n")
my_file.close()
rules = konversiCNF.cnf(cfgRule)
 
class CFG(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("A4")
        self.resize(400,200)

        layout = QVBoxLayout()
        self.setLayout(layout)

        self.inputLabel = QLabel("Masukkan kalimat")
        self.checkButton = QPushButton("Check Validasi")
        self.checkButton.clicked.connect(self.klik)
        self.kalimatEntry = QLineEdit()
        self.statusLabel = QLabel("Status:")
        layout.addWidget(self.inputLabel)
        layout.addWidget(self.kalimatEntry)
        layout.addWidget(self.statusLabel)
        layout.addWidget(self.checkButton)



    def klik(self):
        kalimat = self.kalimatEntry.text()
        
        if len(kalimat) == 0:
            self.statusLabel.setText("Masukkan kalimat terlebih dahulu.")
        elif parsing.tabelCYK(kalimat.lower().split(' '), rules, 'K'):
            self.statusLabel.setText("Status: Valid")
        else:
            self.statusLabel.setText("Status: Tidak Valid")
            
 
    def toggle_window1(self):
        if not self.window1.isVisible():
            self.window1.show()
   
app = QApplication(sys.argv)
window = CFG()
window.show()
sys.exit(app.exec())

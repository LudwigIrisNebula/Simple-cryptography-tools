import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QWidget
# from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QFont
import matplotlib.pyplot as plt

class VigenereCipher(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("VigenereCipher")
        self.setGeometry(100, 100, 400, 300)

        layout = QVBoxLayout()

        self.input_label = QLabel("Input：")
        self.input_text = QLineEdit()
        self.key_label = QLabel("key：")
        self.key_text = QLineEdit()
        self.encrypt_button = QPushButton("Encrypt")
        self.decrypt_button = QPushButton("Decrypt")
        self.output_label = QLabel("Output：")
        self.output_text = QLineEdit()
        self.show_tables_button = QPushButton("Show Vigenere Table")

        layout.addWidget(self.input_label)
        layout.addWidget(self.input_text)
        layout.addWidget(self.key_label)
        layout.addWidget(self.key_text)
        layout.addWidget(self.encrypt_button)
        layout.addWidget(self.decrypt_button)
        layout.addWidget(self.output_label)
        layout.addWidget(self.output_text)
        layout.addWidget(self.show_tables_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

        self.encrypt_button.clicked.connect(self.encrypt)
        self.decrypt_button.clicked.connect(self.decrypt)
        self.show_tables_button.clicked.connect(self.show_tables)

    def encrypt(self):
        input_text = self.input_text.text().upper()
        key = self.key_text.text().upper()
        output_text = ""

        for i in range(len(input_text)):
            if input_text[i].isalpha():
                char = chr((ord(input_text[i]) + ord(key[i % len(key)])) % 26 + ord('A'))
                output_text += char
            else:
                output_text += input_text[i]

        self.output_text.setText(output_text)
    
    def decrypt(self):
        input_text = self.input_text.text().upper()
        key = self.key_text.text().upper()
        output_text = ""

        for i in range(len(input_text)):
            if input_text[i].isalpha():
                char = chr((ord(input_text[i]) - ord(key[i % len(key)])) % 26 + ord('A'))
                output_text += char
            else:
                output_text += input_text[i]

        self.output_text.setText(output_text)

    def show_tables(self):
        plt.figure(figsize=(6, 6))

        # plt.subplot(121)
        plt.title("Vigenere Table", fontsize=14)
        plt.xlabel("Plain text", fontsize=12)
        plt.ylabel("Cipher text", fontsize=12)
        for i in range(26):
            for j in range(26):
                plt.text(j, i, chr((i + j) % 26 + ord('A')), ha='center', va='center', fontsize=10)
        plt.xticks(range(26), [chr(i + ord('A')) for i in range(26)], fontsize=10)
        plt.yticks(range(26), [chr(i + ord('A')) for i in range(26)], fontsize=10)
        plt.grid(True)

        plt.tight_layout()

        # plt.subplot(122)
        # plt.title("英文字母频率表")
        # plt.xlabel("letter")
        # plt.ylabel("频率")
        # letter_frequencies = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228, 2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507, 1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150, 1.974, 0.074]
        # letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        # plt.bar(letters, letter_frequencies)
        # plt.xticks(list(range(len(letters))), letters)
        plt.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = VigenereCipher()
    window.show()
    sys.exit(app.exec_())

from PyQt6.QtWidgets import QApplication,QMainWindow, QTextEdit, QLineEdit, QPushButton
from chatbot import Chatbot
import threading
import sys

class ChatbotWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.chatbot = Chatbot()
        self.setMinimumSize(700,500)
        #Chat Area
        self.chat_area = QTextEdit(self)
        self.chat_area.setGeometry(10,10,500,330)

        #Input field
        self.input_field = QLineEdit(self)
        self.input_field.setGeometry(10,350,500,40)
        self.input_field.returnPressed.connect(self.send_message)
        #Button
        self.button = QPushButton("Send",self)
        self.button.setGeometry(520,350,120,40)
        self.button.clicked.connect(self.send_message)

        self.show()

    def send_message(self):
        user_input = self.input_field.text().strip()
        self.chat_area.append(f"<p style='color:#333333'>Me: {user_input}</p>")
        self.input_field.clear()

        thread = threading.Thread(target=self.get_bot_response, args=(user_input, ))
        thread.start()
    def get_bot_response(self,user_input):
        response = self.chatbot.get_response(user_input)
        self.chat_area.append(f"<p style='color:#333333' background-colorL #E9E9E9>Bot: {response}</p>")

app = QApplication(sys.argv)
main = ChatbotWindow()
sys.exit(app.exec())
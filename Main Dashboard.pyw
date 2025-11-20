
import sys
import subprocess
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
    QHBoxLayout
)
from PyQt5.QtGui import QFont, QPainter, QPixmap
from PyQt5.QtCore import Qt


class GlowingCircle(QPushButton):
    def __init__(self):
        super().__init__()
        self.setFixedSize(100, 100)
        self.pixmap = QPixmap("Circluar Icon.png")  
        self.setStyleSheet("border: none; background-color: transparent;")  
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        if not self.pixmap.isNull():
            x = (self.width() - self.pixmap.width()) // 2
            y = (self.height() - self.pixmap.height()) // 2
            painter.drawPixmap(x, y, self.pixmap)


class AssistantUI(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Desktop Assistant")
        self.setFixedSize(300, 350)
        self.setStyleSheet("background-color: #F9F9F9;")

        self.setup_ui()

    def setup_ui(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        layout.setContentsMargins(20, 20, 20, 20)

        self.glow = GlowingCircle()
        self.glow.clicked.connect(self.run_backend)  
        layout.addWidget(self.glow, alignment=Qt.AlignHCenter)

        greet = QLabel("Hello Jahhan!")
        greet.setFont(QFont("Segoe UI", 19, QFont.Bold))
        greet.setStyleSheet("color: #222;")
        greet.setAlignment(Qt.AlignCenter)
        layout.addWidget(greet)

        input_box = QLineEdit()
        input_box.setPlaceholderText("Type a command...")
        input_box.setFixedHeight(35)
        input_box.setStyleSheet("""
            QLineEdit {
                background-color: white;
                border: 1px solid #ccc;
                border-radius: 10px;
                padding-left: 10px;
                font-size: 13px;
            }
        """)
        layout.addSpacing(15)
        layout.addWidget(input_box)

        icon_layout = QHBoxLayout()
        icon_layout.setSpacing(15)
        icons = [("Apps", "🧩"), ("Weather", "☁️"), ("Notes", "📝"),
                 ("Music", "🎵"), ("Settings", "⚙️")]

        for label, emoji in icons:
            btn = QPushButton(f"{emoji}\n{label}")
            btn.setFixedSize(50, 50)
            btn.setStyleSheet("""
                QPushButton {
                    background-color: white;
                    border-radius: 10px;
                    font-size: 10px;
                    padding: 4px;
                }
            """)
            icon_layout.addWidget(btn)

        layout.addSpacing(50)
        layout.addLayout(icon_layout)
        self.setLayout(layout)

    def run_backend(self):
        try:
            subprocess.Popen(["py", "backend2.py"], shell=True)
        except Exception as e:
            print("Error running backend2.py:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AssistantUI()
    window.show()
    sys.exit(app.exec_())

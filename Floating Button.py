import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QRectF

def open_main_dashboard():
    import sys
    from PyQt5.QtWidgets import (
        QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout,
        QHBoxLayout, QSpacerItem, QSizePolicy
    )
    from PyQt5.QtGui import QFont, QIcon, QPainter, QColor
    from PyQt5.QtCore import Qt
    from PyQt5.QtWidgets import QWidget
    from PyQt5.QtGui import QPainter, QPixmap
    from PyQt5.QtCore import Qt


    # class GlowingCircle(QWidget):
    #     def __init__(self):
    #         super().__init__()
    #         self.setFixedSize(100, 100)  # Increase the size of the widget

    #     def paintEvent(self, event):
    #         painter = QPainter(self)
    #         painter.setRenderHint(QPainter.Antialiasing)

    #         # Glow
    #         painter.setBrush(QColor(100, 170, 255, 100))
    #         painter.setPen(Qt.NoPen)
    #         painter.drawEllipse(10, 10, 80, 80)  # Adjust dimensions for the glow

    #         # Core Circle
    #         painter.setBrush(QColor(100, 170, 255))
    #         painter.drawEllipse(20, 20, 60, 60)  # Adjust dimensions for the core circle
    class GlowingCircle(QWidget):
        def __init__(self):
            super().__init__()
            self.setFixedSize(100, 100)  
            self.pixmap = QPixmap("Circluar Icon.png")  
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

            glow = GlowingCircle()
            layout.addWidget(glow, alignment=Qt.AlignHCenter)

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


    if __name__ == "__main__":
        app = QApplication(sys.argv)
        window = AssistantUI()
        window.show()
        sys.exit(app.exec_())

class FloatingButton(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.setGeometry(-30, 410, 120, 70) 

        self.button = QPushButton("", self)
        self.button.setGeometry(50, 5, 60, 60)  
        self.button.setStyleSheet("""
            QPushButton {
                background-color: #C5E1E6;
                border: 5px solid #6EB1C5;
                border-radius: 30px;
            }
            QPushButton:hover {
                background-color: #D6F2F6;
            }
        """)
        self.button.clicked.connect(self.on_click)

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setBrush(QColor(185, 225, 230)) 
        painter.setPen(Qt.NoPen)
        rect = QRectF(0, 5, 100, 60)  
        painter.drawRoundedRect(rect, 30, 30) 

    def on_click(self):
        os.startfile("Main Dashboard.pyw")
        # open_main_dashboard()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = FloatingButton()
    window.show()
    sys.exit(app.exec_())

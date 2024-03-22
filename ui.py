import sys
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Sleep Effectiveness Measurement")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        settings_button = QPushButton("Settings")
        layout.addWidget(settings_button)

        routine_button = QPushButton("Generate Daily Routine")
        layout.addWidget(routine_button)

        exercise_button = QPushButton("Random Exercise")
        layout.addWidget(exercise_button)

        self.setLayout(layout)
        self.show()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
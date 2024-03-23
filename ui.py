import sys
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
import json
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings_window = None

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

        settings_button.clicked.connect(self.open_settings_window)

    def open_settings_window(self):
        self.settings_window = SettingsWindow()


class SettingsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("Settings")
        self.setGeometry(200, 200, 400, 300)

        layout = QVBoxLayout()

        # Load options from config.json file
        with open('config.json') as f:
            config = json.load(f)

        # Create QLabel and QLineEdit for each option
        for option, value in config.items():
            print(option, value)
            label = QLabel(option)
            line_edit = QLineEdit(str(value))
            layout.addWidget(label)
            layout.addWidget(line_edit)

        # Create save button
        save_button = QPushButton("Save")
        layout.addWidget(save_button)

        # Save button click event handler
        def save_config():
            new_config = {}
            for i in range(layout.count() - 1):
                if i % 2 == 0:
                    option = layout.itemAt(i).widget().text()
                    value = layout.itemAt(i + 1).widget().text()
                    new_config[option] = value
            with open('config.json', 'w') as f:
                json.dump(new_config, f, indent=4)
            self.close()

        # Connect save button click event to save_config function
        save_button.clicked.connect(save_config)

        self.setLayout(layout)
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())

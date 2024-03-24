import sys
import json
from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton
from PySide6.QtWidgets import QLabel, QLineEdit, QPushButton

from random_exercise import generate_exercise_with_solution
from PySide6.QtWidgets import QMessageBox


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.settings_window = None
        self.exercise = None
        self.solution = None

    def initUI(self):
        self.setWindowTitle("Sleep Effectiveness Measurement")
        self.setGeometry(100, 100, 300, 200)

        layout = QVBoxLayout()

        settings_button = QPushButton("Settings")
        layout.addWidget(settings_button)

        routine_button = QPushButton("Generate Daily Routine")
        layout.addWidget(routine_button)

        self.exercise_button = QPushButton("Random Exercise")
        layout.addWidget(self.exercise_button)
        self.exercise_button.clicked.connect(self.generate_random_exercise)

        self.exercise_textbox = QLabel()
        self.exercise_textbox.hide()
        layout.addWidget(self.exercise_textbox)

        self.exercise_answer_textbox = QLineEdit()
        self.exercise_answer_textbox.hide()
        layout.addWidget(self.exercise_answer_textbox)

        self.check_button = QPushButton("Check Exercise")
        self.check_button.hide()
        layout.addWidget(self.check_button)

        self.setLayout(layout)
        self.show()

        settings_button.clicked.connect(self.open_settings_window)
        routine_button.clicked.connect(self.generate_daily_routine)
        self.check_button.clicked.connect(self.check_exercise)

    def open_settings_window(self):
        self.settings_window = SettingsWindow()

    def generate_random_exercise(self):
        self.exercise, self.solution = generate_exercise_with_solution()
        self.exercise_textbox.setText(self.exercise)
        self.exercise_answer_textbox.show()
        self.exercise_textbox.show()
        self.check_button.show()

    def generate_daily_routine(self):
        # Generate daily routine logic here
        pass

    def check_exercise(self):
        try:
            exercise = int(self.exercise_answer_textbox.text())
            if exercise == self.solution:
                self.show_success_message()
                self.exercise_textbox.hide()
                self.exercise_answer_textbox.hide()
                self.check_button.hide()
            else:
                self.show_failure_message()
        except ValueError:
            QMessageBox.information(self, "Error", "Please, type a number!")
        except Exception as e:
            QMessageBox.information(self, "Error", str(e))

    def show_success_message(self):
        QMessageBox.information(
            self, "Success", "Exercise is correct! Well done!")

    def show_failure_message(self):
        QMessageBox.information(self, "Failure", "Worng! Try again!")


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

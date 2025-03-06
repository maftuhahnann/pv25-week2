from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QFormLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QGroupBox, QComboBox
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt
import sys

class RegistrationForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Week 2 : Layout - User Registration Form")
        self.setGeometry(100, 100, 500, 400)
        self.setStyleSheet("background-color: grey;")

        main_layout = QVBoxLayout()

        identity_group = QGroupBox("Identitas")
        identity_group.setStyleSheet("background-color: lightgrey; color: black; font-weight: bold;")
        identity_layout = QVBoxLayout()
        identity_layout.addWidget(QLabel("Nama : Maftuh Ahnan Al-Kautsar"))
        identity_layout.addWidget(QLabel("Nim : F1D022135"))
        identity_layout.addWidget(QLabel("Kelas : C"))
        identity_group.setLayout(identity_layout)
        main_layout.addWidget(identity_group)

        nav_group = QGroupBox("Navigation")
        nav_group.setStyleSheet("background-color: lightgrey; color: black; font-weight: bold;")
        nav_layout = QHBoxLayout()

        home_btn = QPushButton("Home")
        home_btn.setStyleSheet("background-color: white; color: black; font-weight: bold;")
        about_btn = QPushButton("About")
        about_btn.setStyleSheet("background-color: white; color: black; font-weight: bold;")
        contact_btn = QPushButton("Contact")
        contact_btn.setStyleSheet("background-color: white; color: black; font-weight: bold;")

        nav_layout.addWidget(home_btn)
        nav_layout.addWidget(about_btn)
        nav_layout.addWidget(contact_btn)
        nav_group.setLayout(nav_layout)
        main_layout.addWidget(nav_group)

        form_group = QGroupBox("User Registration")
        form_group.setStyleSheet("background-color: lightgrey; color: black; font-weight: bold;")
        form_layout = QFormLayout()

        self.full_name = QLineEdit()
        self.full_name.setStyleSheet("background-color: white; color: black;")
        self.email = QLineEdit()
        self.email.setStyleSheet("background-color: white; color: black;")
        self.phone = QLineEdit()
        self.phone.setStyleSheet("background-color: white; color: black;")

        gender_layout = QHBoxLayout()
        self.male_radio = QRadioButton("Male")
        self.male_radio.setStyleSheet("color: black; font-weight: bold;")
        self.female_radio = QRadioButton("Female")
        self.female_radio.setStyleSheet("color: black; font-weight: bold;")
        gender_layout.addWidget(self.male_radio)
        gender_layout.addWidget(self.female_radio)

        self.country_combo = QComboBox()
        self.country_combo.setStyleSheet("background-color: white; color: black;")
        self.country_combo.addItems(["Select Country", "Indonesia", "Malaysia", "Germany", "USA"])

        form_layout.addRow("Full Name:", self.full_name)
        form_layout.addRow("Email:", self.email)
        form_layout.addRow("Phone:", self.phone)
        form_layout.addRow("Gender:", gender_layout)
        form_layout.addRow("Country:", self.country_combo)

        form_group.setLayout(form_layout)
        main_layout.addWidget(form_group)

        action_group = QGroupBox("Actions")
        action_group.setStyleSheet("background-color: lightgrey; color: black; font-weight: bold;")
        action_layout = QHBoxLayout()
        submit_btn = QPushButton("Submit")
        submit_btn.setStyleSheet("background-color: white; color: black; font-weight: bold;")
        cancel_btn = QPushButton("Cancel")
        cancel_btn.setStyleSheet("background-color: white; color: black; font-weight: bold;")
        action_layout.addWidget(submit_btn)
        action_layout.addWidget(cancel_btn)
        action_group.setLayout(action_layout)
        main_layout.addWidget(action_group)

        self.setLayout(main_layout)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RegistrationForm()
    window.show()
    sys.exit(app.exec())
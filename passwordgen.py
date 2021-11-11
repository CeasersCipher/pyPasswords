import random
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import os

import passwordgen_GUI

letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
numbers = '1234567890'
specialchars = '!@#$%^&*().,'

class PasswordGenQT(QDialog, passwordgen_GUI.Ui_PasswordGenerator):
    def __init__(self):
        QDialog.__init__(self)
        self.setupUi(self)

        # assign actions to all buttons
        self.start.clicked.connect(self.start_button)
        self.save.clicked.connect(self.save_button)

    def start_button(self):
        global password_list
        password_list = []
        number_of_pass = int(self.numberofpasswords.toPlainText())
        number_of_letters = int(self.numberofletters.toPlainText())
        number_of_numbers = int(self.numberofnumbers.toPlainText())
        number_of_specialchars = int(self.numberofspecialchar.toPlainText())

        for newpassword in range(number_of_pass):
            password = []
            password_string = ""
            for i in range(number_of_letters):
                password.append(random.choice(letters))

            for i in range(number_of_numbers):
                password.append(random.choice(numbers))

            for i in range(number_of_specialchars):
                password.append(random.choice(specialchars))

            random.shuffle(password)

            for element in password:
                password_string += element

            password_list.append(password_string)

        password_list = str(password_list)
        
        self.passwordlist.setText(password_list)

    def save_button(self):
        save_folder = QFileDialog.getExistingDirectory(self, "Where to Save")
        save_location = str(save_folder + "/password_dump.txt")
        file = open(save_location, 'w')
        text = password_list
        file.write(text)
        file.close()




app = QApplication(sys.argv)
passwordgenQT = PasswordGenQT()
passwordgenQT.show()
app.exec_()


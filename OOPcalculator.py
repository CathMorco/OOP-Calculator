#Imports necessary elements
from PyQt5.QtWidgets import QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox, QProgressDialog
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtCore import QTimer

#creates class for widgets
class Calculator(QWidget):
    def __init__(self, model, x, y):
        super().__init__()
        self.positionx = x
        self.positiony = y
        self.model = model
        self.initUI()
        self.on = False



#creates function for GUI

    def initUI(self):
        # Create QLabel for the operation selection
        self.operationLabel = QLabel('Please enter your number before choosing an operation:')
        self.operationLabel.setAlignment(Qt.AlignCenter)

        # Create QPushButton for addition operation
        self.addButton = QPushButton('+')

        # Create QPushButton for subtraction operation
        self.subButton = QPushButton('-')

        # Create QPushButton for multiplication operation
        self.mulButton = QPushButton('*')

        # Create QPushButton for division operation
        self.divButton = QPushButton('/')

        # Create QPushButton for power control
        self.powerButton = QPushButton('Power On')

        # Create QLabel and QLineEdit for the first number input
        self.num1Label = QLabel('Enter the first number:')
        self.num1Label.setAlignment(Qt.AlignCenter)
        self.num1LineEdit = QLineEdit()

        # Create QLabel and QLineEdit for the second number input
        self.num2Label = QLabel('Enter the second number:')
        self.num2Label.setAlignment(Qt.AlignCenter)
        self.num2LineEdit = QLineEdit()

        # Create QLabel for displaying the result
        self.resultLabel = QLabel()

        # Create QVBoxLayout and add widgets to it
        vbox = QVBoxLayout()
        vbox.addWidget(self.operationLabel)
        vbox.addWidget(self.addButton)
        vbox.addWidget(self.subButton)
        vbox.addWidget(self.mulButton)
        vbox.addWidget(self.divButton)
        vbox.addWidget(self.num1Label)
        vbox.addWidget(self.num1LineEdit)
        vbox.addWidget(self.num2Label)
        vbox.addWidget(self.num2LineEdit)
        vbox.addWidget(self.resultLabel)
        vbox.addWidget(self.powerButton)

        # Set layout for the window
        self.setLayout(vbox)

        # Connect signals and slots
        self.addButton.clicked.connect(lambda: self.addition())
        self.subButton.clicked.connect(lambda: self.subtraction())
        self.mulButton.clicked.connect(lambda: self.multiplication())
        self.divButton.clicked.connect(lambda: self.division())
        self.powerButton.clicked.connect(self.togglePower)

        self.screenDisplay = QLabel(self)

        self.screenDisplay.setGeometry(5, 5, 480, 50)

        self.screenDisplay.setWordWrap(True)

        self.screenDisplay.setAlignment(Qt.AlignRight)

        self.screenDisplay.setFont(QFont('Times', 20))
        self.screenDisplay.setStyleSheet("QLabel"
                                 "{"
                                 "border : 1px solid grey;"
                                 "background : grey;"
                                 "}")
        

# Set window properties
        self.setWindowTitle('Calculator ' + self.model)

        self.setGeometry(self.positionx, self.positiony, 500, 800)
        self.show()


    def togglePower(self):
        self.on = not self.on
        if self.on:
            self.powerButton.setText('Power Off')
            self.addButton.setEnabled(True)
            self.subButton.setEnabled(True)
            self.mulButton.setEnabled(True)
            self.divButton.setEnabled(True)
            self.progressDialog = QProgressDialog("Intializing " + self.model + " ...", "Cancel", 0, 100, self)
            self.progressDialog.setWindowModality(Qt.WindowModal)
            self.progressDialog.setWindowTitle("Progress")
            self.progressDialog.setAutoClose(True)
            self.progressDialog.show()
            self.progressTimer = QTimer()
            self.progressTimer.timeout.connect(self.updateProgress)
            self.progressTimer.start(10)
            
        else:
            self.powerButton.setText('Power On')
            self.addButton.setEnabled(False)
            self.subButton.setEnabled(False)
            self.mulButton.setEnabled(False)
            self.divButton.setEnabled(False)
            self.progressTimer.stop()
            self.progressDialog.close()

    def updateProgress(self):
            self.progressDialog.setValue(self.progressDialog.value() + 1)

    # Create a function for the addition operation
    def addition(self):
        if not self.on:
            return QMessageBox.information(self, 'Error Message', 'Please turn the Power On' , QMessageBox.Ok)
        num1 = self.num1LineEdit.text()
        num2 = self.num2LineEdit.text()
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
            return QMessageBox.information(self, 'Value Error', 'Invalid Input, Please Input Numbers Only', QMessageBox.Ok)
        result = num1 + num2
        self.displayResult(result)

    # Create a function for the subtraction operation
    def subtraction(self):
        if not self.on:
            return QMessageBox.information(self, 'Error Message', 'Please turn the Power On' , QMessageBox.Ok)
        num1 = self.num1LineEdit.text()
        num2 = self.num2LineEdit.text()
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
            return QMessageBox.information(self, 'Value Error', 'Invalid Input, Please Input Numbers Only', QMessageBox.Ok)
        result = num1 - num2
        self.displayResult(result)

    # Create a function for the multiplication operation
    def multiplication(self):
        if not self.on:
            return QMessageBox.information(self, 'Error Message', 'Please turn the Power On' , QMessageBox.Ok)
        num1 = self.num1LineEdit.text()
        num2 = self.num2LineEdit.text()
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
            return QMessageBox.information(self, 'Value Error', 'Invalid Input, Please Input Numbers Only', QMessageBox.Ok)
        result = num1 * num2
        self.displayResult(result)


    # Create a function for the division operation
    def division(self):
        if not self.on:
            return QMessageBox.information(self, 'Error Message', 'Please turn the Power On' , QMessageBox.Ok)
        num1 = self.num1LineEdit.text()
        num2 = self.num2LineEdit.text()
        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
            return QMessageBox.information(self, 'Value Error', 'Invalid Input, Please Input Numbers Only', QMessageBox.Ok)
        try:
            result = num1 / num2
            self.resultLabel.setText('Zero Division not allowed')
        except ZeroDivisionError:
            self.num2LineEdit.clear()
            return QMessageBox.information(self, 'Syntax Error', 'Zero Division not allowed', QMessageBox.Ok)

        self.displayResult(result)

    # Create a function to display the result
    def displayResult(self, result):
        self.screenDisplay.setText(str(result))

        # Asks user if they want to try again
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setText("Do you want to try again?")
        messageBox.setWindowTitle("Confirmation")
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        response = messageBox.exec_()
        # If yes, clears input fields
        if response == QMessageBox.Yes:
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
        # If no, displays thank you message and closes program
        else:
            Tymsg = QMessageBox()
            Tymsg.setWindowTitle("Message")
            Tymsg.setText("Thank you!")
            x = Tymsg.exec_()
            self.close()
from OOPcalculator import Calculator
import sys
from PyQt5.QtWidgets import QApplication, QMessageBox
from PyQt5.QtCore import QTimer
#Added a new class that inherits the existing class in my  calculator program
class NewCalculator(Calculator):
    def __init__(self, model, xAxis, yAxis):
        super().__init__(model, xAxis, yAxis)

    #Added new method that overrides an existing method
    def displayResult(self, result):
        self.screenDisplay.setText(str(result))
        #Calls the askTryAgain method and adds a delay
        QTimer.singleShot(2000, self.askTryAgain)

    #Added a new method in the class (Separated the message box from the displayresult method from the existing class)
    def askTryAgain(self):
        # Asks user if they want to try again
        messageBox = QMessageBox()
        messageBox.setIcon(QMessageBox.Question)
        messageBox.setText("You just overrode a method! Do you want to try again?")
        messageBox.setWindowTitle("Confirmation After Override")
        messageBox.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

        response = messageBox.exec_()
        # If yes, clears input fields
        if response == QMessageBox.Yes:
            self.screenDisplay.setText("Loading...")
            #Adds a delay to the loading screen before it clears the display
            QTimer.singleShot(3000, self.clearScreenDisplay)
            self.num1LineEdit.clear()
            self.num2LineEdit.clear()
        # If no, displays thank you message and closes program
        else:
            Tymsg = QMessageBox()
            Tymsg.setWindowTitle("Message")
            Tymsg.setText("Thank you!")
            x = Tymsg.exec_()
            self.close()
    #Added a new method that clears the screen display
    def clearScreenDisplay(self):
        self.screenDisplay.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc1 = NewCalculator("Casio", 100, 100)
    calc2 = NewCalculator("Samsung", 650, 100)
    calc3 = NewCalculator("Sony", 1200, 100)
    sys.exit(app.exec_())
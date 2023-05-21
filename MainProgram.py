from OOPcalculator import Calculator
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    Calculator("Casio")
    sys.exit(app.exec_())
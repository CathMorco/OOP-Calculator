from OOPcalculator import Calculator
import sys
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    calc1 = Calculator("Casio", 100, 100)
    calc2 = Calculator("Samsung", 650, 100)
    calc3 = Calculator("Sony", 1200, 100)
    sys.exit(app.exec_())
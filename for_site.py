from calc import *

class Main(Ui_Calc):
    def __init__(self):
        super().__init__()

# a = Main()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calc = QtWidgets.QMainWindow()
    ui = Ui_Calc()
    ui.setupUi(Calc)
    Calc.show()
    sys.exit(app.exec_())
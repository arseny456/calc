from calc import *

class Main(Ui_Calc):
    def __init__(self):
        super().__init__()

        self.add_functions()


    def write_number(self, number):
        print(self, number)

    def add_functions(self):
        self.pushButton_0.clicked.connect(lambda: self.write_number(self.pushButton_0.text()))
        self.pushButton_1.clicked.connect(lambda: self.write_number(self.pushButton_1.text()))



# a = Main()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calc = QtWidgets.QMainWindow()
    ui = Ui_Calc()
    ui.setupUi(Calc)
    Calc.show()
    # ui.tab_3.
    sys.exit(app.exec_())
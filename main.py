import numpy
import gdwngrade
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
import sys
import design


def gprice(x, y):
    a = (x + y + 1)**2
    b = 19 - 14*x + 3*x*x - 14*y + 6*x*y + 3*y*y
    c = (2*x-3*y)**2
    d = 18 - 32*x + 12*x*x + 48*y - 36*x*y + 27*y*y
    return (1+a*b)*(30+c*d)


def rastrigin(*args):
    a = 10
    n = len(args)
    return a*n+sum([x**2-a*numpy.cos(2*numpy.pi*x) for x in args])

class GDwngrade(QMainWindow, design.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # local attributes
        self.from_value = 0
        self.till_value = 0
        self.progressBar.setVisible(False)

        # widgets_configuration
        self.search_button.clicked.connect(self.search_button_pressed)
        # listeners

    # listeners' listing
    def search_button_pressed(self):
        if self.validate():
            self.progressBar.setVisible(True)
            progress = 0
            r = numpy.arange(self.from_value, self.till_value, 0.5)
            size = len(r)**2
            mins = set()
            for row in [[(y, x) for y in r] for x in r]:
                for cell in row:
                    mins.add(tuple(gdwngrade.minimum(rastrigin, *cell)))
                    last = min(mins, key=lambda a: a[0])
                    self.result_label.setText(str(round(last[0], 3))+" ["+",".join([str(round(a, 3)) for a in last[-1]])+"]")
                    progress = progress+1
                    self.progressBar.setValue(progress/size*100)
            self.progressBar.setVisible(False)


    def validate(self):
        res = True
        try:
            self.from_value = float(self.from_le.text())
            p = self.from_le.palette()
            p.setColor(self.from_le.foregroundRole(), Qt.black)
            p.setColor(self.from_le.backgroundRole(), Qt.white)
            self.from_le.setPalette(p)
        except ValueError:
            p = self.from_le.palette()
            p.setColor(self.from_le.foregroundRole(), Qt.darkRed)
            p.setColor(self.from_le.backgroundRole(), Qt.red)
            self.from_le.setPalette(p)
            res = False
        try:
            self.till_value = float(self.till_le.text())
            p = self.till_le.palette()
            p.setColor(self.till_le.foregroundRole(), Qt.black)
            p.setColor(self.till_le.backgroundRole(), Qt.white)
            self.till_le.setPalette(p)
        except ValueError:
            p = self.till_le.palette()
            p.setColor(self.till_le.foregroundRole(), Qt.darkRed)
            p.setColor(self.till_le.backgroundRole(), Qt.red)
            self.till_le.setPalette(p)
            res = False
        return res

# app execution
def main():
    app = QApplication(sys.argv)
    window = GDwngrade()
    window.show()
    app.exec_()

# check for target of execution
if __name__ == "__main__":
    main()
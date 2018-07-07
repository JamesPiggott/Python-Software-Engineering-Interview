import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

def app():
    my_app = QApplication(sys.argv)
    w = QWidget()
    w.setWindowTitle("Testing this PyQt5")
    w.setWindowIcon(QIcon('braincircles_small.png'))

    w.show()
    sys.exit(my_app.exec_())

app()

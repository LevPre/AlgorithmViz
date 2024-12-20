from canvasClass import *
from ToolBar import *
from Imports import *
from AlgorithmAnimations import *
#dark gray #393646
#light gray #4F4557
#lighter gray #6D5D6E
#Off white #F4EEE0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.timer = QTimer(self)
        
        
        
        self.setWindowTitle("Circle Drawing App")
        self.setGeometry(100, 100, 800, 400)  
        self.setStyleSheet("background-color: #222222;") 
        self.algoAnimate = AlgoAnimation(self.timer)
        self.MytoolBar = MyToolBar(self.algoAnimate)
        self.addToolBar(Qt.LeftToolBarArea, self.MytoolBar.toolBar)
        self.setCentralWidget(self.algoAnimate)
        

    



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show() 
    sys.exit(app.exec_()) 


if __name__ == "__main__":
    main()
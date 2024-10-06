from canvasClass import *
from ToolBar import *
from Imports import *

#dark gray #393646
#light gray #4F4557
#lighter gray #6D5D6E
#Off white #F4EEE0


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawing App")
        self.setGeometry(100, 100, 800, 400)  
        self.setStyleSheet("background-color: #222222;") 
        self.canvas = Canvas()
        self.MytoolBar = MyToolBar(self.canvas)
        self.addToolBar(Qt.LeftToolBarArea, self.MytoolBar.toolBar)
        
        
        
        self.setCentralWidget(self.canvas)
        
    
    



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Run the application


if __name__ == "__main__":
    main()
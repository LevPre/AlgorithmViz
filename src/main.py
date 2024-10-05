from canvasClass import *

#dark gray #393646
#light gray #4F4557
#lighter gray #6D5D6E
#Off white #F4EEE0

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawing App")
        self.setGeometry(100, 100, 800, 400)  # Adjusted window size for sidebar
        self.setStyleSheet("background-color: #222222;") 
        self.canvas = Canvas()
        
        
        self.toolBar = QToolBar("side", self)
        self.toolBar.setMinimumSize(int(self.width()*0.4),int(self.width()*0.4))
        
        self.addToolBar(Qt.LeftToolBarArea, self.toolBar)
        self.toolBar.addActions((self.add_action(text=text) 
                            for text in ["Clean"]))

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding,
                             QSizePolicy.Policy.Expanding)
        self.toolBar.addWidget(spacer)

 
        self.toolBar.addAction(self.add_action(
            icon=QIcon("apprendre_python\PyQT\close.png"),
            text="close"))
        
        
        self.setCentralWidget(self.canvas)
        
    
    def add_action(self,icon : QIcon = QIcon(),
                   text : str = "",
                   short_cut : str = ""):    
        action = QAction(icon=icon,text=text,parent=self)
        action.setShortcut(short_cut)
        action.setObjectName(text)
        action.triggered.connect(self.on_action_triggered)
        return action
    
    
    
    def on_action_triggered(self):
        match self.sender().objectName():
            case "Clean":
                self.canvas.circles.clear()
            case _:
                pass
        self.canvas.update()



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Run the application


if __name__ == "__main__":
    main()
from Imports import *

class MyToolBar(QWidget):
    def __init__(self,canvas):
        super().__init__()
        self.toolBar = QToolBar("side", self)
        self.toolBar.setMinimumSize(int(self.width()*0.4),int(self.width()*0.4))
        self.canvas = canvas
       
        self.toolBar.addActions((self.add_action(text=text) 
                            for text in ["Clean"]))

        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding,
                             QSizePolicy.Policy.Expanding)
        self.toolBar.addWidget(spacer)

 
        self.toolBar.addAction(self.add_action(
            icon=QIcon("apprendre_python\PyQT\close.png"),
            text="close"))
    
    
    
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
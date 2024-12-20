from Imports import *
from PyQt5.QtWidgets import QWidget, QToolBar, QAction, QToolButton, QSizePolicy


class MyToolBar(QWidget):
    def __init__(self,algorithms):
        super().__init__()
        self.algorithms = algorithms
        self.buttons = []
        self.toolBar = QToolBar("side", self)
        self.toolBar.setMinimumSize(int(self.width()*0.2), int(self.width()*0.2))
        self.toolBar.setStyleSheet("")
       
        self.create_action_button(text="Clean")  #0
        self.create_action_button(text="Directed")  #1
        self.create_action_button(text="BFS")  #2
        self.create_action_button(text="DFS")
        
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        spacer.setStyleSheet("background-color: #222222;")
        self.toolBar.addWidget(spacer)



    def create_action_button(self, text: str = ""):
        
        action = QAction(text, self)
        action.setObjectName(text)
        action.triggered.connect(self.on_action_triggered)

       
        button = QToolButton()
        button.setDefaultAction(action)
        button.setStyleSheet(f"background-color: #333333; color: white; border: none; padding: 5px; margin: 5px; width:100%")
    

   
        self.toolBar.addWidget(button)
        self.buttons.append(button)



    def on_action_triggered(self):
        match self.sender().objectName():
            case "Clean":
                self.algorithms.circles.clear()
                self.algorithms.Lines.clear()
                
            case "Directed":
                action = QAction("UnDirected", self)
                action.setObjectName("UnDirected")
                action.triggered.connect(self.on_action_triggered)
                self.buttons[1].setDefaultAction(action)
                self.algorithms.Directed = False
                
            case "UnDirected":
                action = QAction("Directed", self)
                action.setObjectName("Directed")
                action.triggered.connect(self.on_action_triggered)
                self.buttons[1].setDefaultAction(action)
                self.algorithms.Directed = True
                
            case "BFS":
                if self.algorithms.selected_circle != None:
                    self.algorithms.BFSAnimation()
                    
            case "DFS":
                if self.algorithms.selected_circle != None:
                    self.algorithms.DFSAnimation()

                
            case _:
                pass
        self.algorithms.update()
        
        
        
        

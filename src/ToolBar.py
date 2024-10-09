from Imports import *
from PyQt5.QtWidgets import QWidget, QToolBar, QAction, QToolButton, QSizePolicy
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize

class MyToolBar(QWidget):
    def __init__(self, canvas , algorithms):
        super().__init__()
        self.canvas = canvas
        self.algorithms = algorithms
        self.buttons = []
        self.toolBar = QToolBar("side", self)
        self.toolBar.setMinimumSize(int(self.width()*0.4), int(self.width()*0.4))
        
        # Create actions with different colors
        self.create_action_button(text="Clean")  #0
        self.create_action_button(text="BFS")  #1
        self.create_action_button(text="Directed")  #2
        
        # Add spacer to the toolbar
        spacer = QWidget()
        spacer.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        spacer.setStyleSheet("background-color: #222222;")
        self.toolBar.addWidget(spacer)



    def create_action_button(self, icon: QIcon = QIcon(), text: str = "", short_cut: str = "", color: str = ""):
        
        action = QAction(icon, text, self)
        action.setShortcut(short_cut)
        action.setObjectName(text)
        action.triggered.connect(self.on_action_triggered)

        # Create a QToolButton for the action
        button = QToolButton()
        button.setDefaultAction(action)
        button.setStyleSheet(f"background-color: #333333; color: white; border: none; padding: 5px;")
        button.setIconSize(QSize(24, 24))  # Adjust icon size as needed

        # Add the styled button to the toolbar
        self.toolBar.addWidget(button)
        self.buttons.append(button)



    def on_action_triggered(self):
        match self.sender().objectName():
            case "Clean":
                self.canvas.circles.clear()
                
            case "Directed":
                action = QAction(QIcon(), "UnDirected", self)
                action.setShortcut("")
                action.setObjectName("UnDirected")
                action.triggered.connect(self.on_action_triggered)
                self.buttons[2].setDefaultAction(action)
                self.canvas.Directed = False
                
            case "UnDirected":
                action = QAction(QIcon(), "Directed", self)
                action.setShortcut("")
                action.setObjectName("Directed")
                action.triggered.connect(self.on_action_triggered)
                self.buttons[2].setDefaultAction(action)
                self.canvas.Directed = True
                
            case "BFS":
                if self.canvas.Directed and self.canvas.selected_circle != None : 
                    self.algorithms.start()
                else:
                    pass

                
            case _:
                pass
        self.canvas.update()
        
        
        
        

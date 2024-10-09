from Imports import *
from PyQt5.QtCore import Qt, QPoint, QTimer

class AlgoAnimation:
    def __init__(self, canvas, interval, timer):
        self.canvas = canvas
        self.interval = interval
        self.timer = timer
        self.timer.timeout.connect(self.pr1)

    def start(self):
        self.timer.start(1000)
        self.timer.timeout.connect(self.pr1)
        

    def pr1(self):
        print("hello")

        
        
    """def BfsAnimation(self):
        self.queue = [self.canvas.selected_circle]
        self.visited = []
        self.canvas.is_animating = True
        
        self.timer.timeout.connect(self.pr)
        self.timer.start(1000) 
        print (self.timer.isActive())
        
    def run_bfs_step(self):
        while(len(self.queue) != 0):
            for circle in self.queue[0].lines:
                if circle not in self.visited and circle not in self.queue:
                    self.queue.append(circle)
             
            self.visited.append(self.queue[0])
            self.queue.pop(0)
        
        print(self.visited)"""
    
    
        
        
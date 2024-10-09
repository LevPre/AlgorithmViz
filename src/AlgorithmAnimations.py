from Imports import *
from PyQt5.QtCore import Qt, QPoint, QTimer

class AlgoAnimation:
    def __init__(self, canvas, interval, timer):
        self.canvas = canvas
        self.interval = interval
        self.timer = timer
        self.Animating = False
        self.circleSave = canvas.circles
        
        
    def BfsAnimation(self):
        
        
        if(self.Animating):
            self.canvas.circles = self.circleSave
            self.timer.disconnect()
            self.timer.stop()
            self.Animating = False
            self.canvas.is_animating =False
            self.canvas.AnimatedLines = []
            for circle in self.canvas.circles:
                circle.color = "#505050"
        else:
            self.circleSave = self.canvas.circles
            self.timer.start(1000)
            self.timer.timeout.connect(self.run_bfs_step)
            self.Animating = True
            self.canvas.is_animating =True
        
        self.queue = [self.canvas.selected_circle]
        self.visited = []
        self.canvas.update()


        
    def run_bfs_step(self):
        if(len(self.queue) != 0):
            for circle in self.queue[0].lines:
                if circle not in self.visited and circle not in self.queue:
                    self.queue.append(circle)
                    self.canvas.AnimatedLines.append([self.queue[0],circle])
             
            self.visited.append(self.queue[0])
            self.queue.pop(0)
            self.drawVisitedCircles()
            self.drawQueueCircles()
        else:
            self.queue = [self.canvas.selected_circle]
            self.visited = []
            self.canvas.AnimatedLines = []
            for circle in self.canvas.circles:
                circle.color = "#505050"
            
        
        
        
        self.canvas.update()
        
    def drawVisitedCircles(self):
        for circle in self.visited:
            circle.color = "#713a7e"
    def drawQueueCircles(self):
        for circle in self.queue:
            circle.color = "#e475ff"
 
    
        
        
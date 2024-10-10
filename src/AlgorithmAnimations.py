from Imports import *
from canvasClass import Canvas
from PyQt5.QtCore import Qt, QPoint, QTimer

class AlgoAnimation(Canvas):
    def __init__(self, timer):
        super().__init__(timer)
        self.AnimatedLines = []
  
        
    def BfsAnimation(self):
        if(self.is_animating):
            self.timer.disconnect()
            self.timer.stop()
            self.is_animating =False
            for circle in self.circles:
                circle.color = "#505050"
            for line in self.Lines:
                line.color =  "#222222"
            
        else:
            self.timer.start(1500)
            self.timer.timeout.connect(self.run_bfs_step)
            self.is_animating =True
        
        self.queue = [self.selected_circle]
        self.visited = []
        self.update()


        
    def run_bfs_step(self):
        if(not self.is_animating):
            self.timer.disconnect()
            self.timer.stop()
            self.is_animating =False
            self.AnimatedLines = []
            for circle in self.circles:
                circle.color = "#505050"
            for line in self.Lines:
                line.color =  "#222222"    
            self.update()
            return
        
        if(len(self.queue) != 0):
            for line in self.Lines:
                if line.From == self.queue[0]:
                    self.queue.append(line.To)
                    self.AnimatedLines.append(line)
             
            self.visited.append(self.queue[0])
            self.queue.pop(0)
            self.drawVisitedCircles()
            self.drawQueueCircles()
            self.drawAnimatedLines()
        else:
            print("yo")
            self.queue = [self.selected_circle]
            
            for circle in self.visited:
                circle.color = "#505050"
            for line in self.AnimatedLines:
                line.color = "#222222"
            self.visited = []
            self.AnimatedLines = []
            
        
        
        
        self.update()
        
    def drawVisitedCircles(self):
        for circle in self.visited:
            circle.color = "#713a7e"
    def drawQueueCircles(self):
        for circle in self.queue:
            circle.color = "#e475ff"
    def drawAnimatedLines(self):
        for line in self.AnimatedLines:
            line.color = "#e475ff"
 

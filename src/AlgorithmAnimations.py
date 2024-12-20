from Imports import *
from canvasClass import Canvas
from PyQt5.QtCore import Qt, QPoint, QTimer

class AlgoAnimation(Canvas):
    def __init__(self, timer):
        super().__init__(timer)
 
 #BFS ----------------------------------------------------------------       
    def BFSAnimation(self):
        if(self.is_animating):
            self.StopAnimation()
            
        else:
            self.timer.start(1500)
            self.timer.timeout.connect(self.BFSStep)
            self.is_animating =True
        
        self.queue = [self.selected_circle]
        self.Finished = []
        self.AnimatedLines = []
        self.update()


        
    def BFSStep(self):
        if(not self.is_animating):
            self.ResetAnimation()
            return
        
        if(len(self.queue) != 0):
            for line in self.Lines:
                if line.From == self.queue[0]  and line.To not in self.queue and line.To not in self.Finished:
                    self.queue.append(line.To)
                    self.Started.append(line.To)
                    self.AnimatedLines.append(line)
                if line.To == self.queue[0]  and line.From not in self.queue and line.From not in self.Finished and not self.Directed : #if not directed it will check both sides of line
                    self.queue.append(line.From)
                    self.Started.append(line.From)
                    self.AnimatedLines.append(line)
             
            self.Finished.append(self.queue[0])
            self.queue.pop(0)
            self.drawFinishedCircles()
            self.drawQueueCircles()
            self.drawAnimatedLines()
        else:
            self.queue = [self.selected_circle]
            
            for circle in self.Finished:
                circle.color = "#505050"
            for line in self.AnimatedLines:
                line.color = "#222222"
            self.Finished = []
            self.AnimatedLines = []
            
        
        
        
        self.update()
 #BFS ----------------------------------------------------------------
 
 #DFS ----------------------------------------------------------------
    def DFSAnimation(self):
        if(self.is_animating):
           self.StopAnimation()
            
        else:
            self.timer.start(1500)
            self.timer.timeout.connect(self.DFSStep)
            self.is_animating =True
        
        self.queue = [self.selected_circle]
        self.Finished = []
        self.AnimatedLines = []
        self.update()


        
    def DFSStep(self):
        if(not self.is_animating):
            self.ResetAnimation()
            return
        
        if(len(self.queue) != 0):
            Top = self.queue[-1]
            for line in self.Lines:
                if line.From == Top and line.From not in self.Finished and line.To not in self.Finished and line.To not in self.queue:
                    self.queue.append(line.To)
                    self.Started.append(line.To)
                    self.AnimatedLines.append(line)
                    self.drawFinishedCircles()
                    self.drawQueueCircles()
                    self.drawAnimatedLines()
                    self.update()
                    return
                if line.To == Top and line.To not in self.Finished and line.From not in self.Finished and line.From not in self.queue and not self.Directed : #if not directed it will check both sides of line
                    self.queue.append(line.From)
                    self.Started.append(line.From)
                    self.AnimatedLines.append(line)
                    self.drawFinishedCircles()
                    self.drawQueueCircles()
                    self.drawAnimatedLines()
                    self.update()
                    return
            
               
            self.Finished.append(self.queue.pop())
                
            
            self.drawFinishedCircles()
            self.drawQueueCircles()
            self.drawAnimatedLines()
        else:
            self.queue = [self.selected_circle]
            
            for circle in self.Finished:
                circle.color = "#505050"
            for line in self.AnimatedLines:
                line.color = "#222222"
            self.Finished = []
            self.AnimatedLines = []
            
        self.update()
 #DFS ----------------------------------------------------------------
        
    def drawFinishedCircles(self):
        for circle in self.Finished:
            circle.color = "#713a7e"
    def drawQueueCircles(self):
        for circle in self.queue:
            circle.color = "#e475ff"
    def drawAnimatedLines(self):
        for line in self.AnimatedLines:
            line.color = "#e475ff"
 

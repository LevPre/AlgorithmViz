from Imports import *
from PyQt5.QtCore import Qt, QPoint
from AlgorithmAnimations import *
class Circle:
    def __init__(self, center: QPoint, radius: int):
        
        self.center = center
        self.radius = radius
        self.lines = []


    def contains(self, point: QPoint) -> bool:
        return (point.x() - self.center.x()) ** 2 + (point.y() - self.center.y()) ** 2 <= self.radius ** 2
    
    def overlap(self, point: QPoint) -> bool:
        return (point.x() - self.center.x()) ** 2 + (point.y() - self.center.y()) ** 2 < (2*self.radius) ** 2



class Canvas(QWidget):
    def __init__(self,timer):
        super().__init__()
        self.setMinimumSize(700, 400)  # Set minimum size for the canvas
        self.circles = []  # List to hold circles
        self.selected_circle = None  # Track the currently selected circle
        self.dragging = False
        self.dragged = False
        self.Directed = True
        self.AllLines = []
        self.is_animating = False
        self.timer = timer
        
        
        
        
    def drawDirectedLines(self,painter):
        ArrowSize = 30
        ArrowDegree = np.pi / 12
        for circle in self.circles:
            for line in circle.lines:
                
                deltaX = circle.center.x() - line.center.x()
                deltaY = circle.center.y() - line.center.y()
                
                Alpha = np.atan2(deltaY,deltaX)
                
                Point1 = [int(circle.center.x() - circle.radius * np.cos(Alpha) ), int(circle.center.y() - circle.radius * np.sin(Alpha)) ]
                Point2 = [int(line.center.x() + line.radius * np.cos(Alpha) ), int(line.center.y() + line.radius * np.sin(Alpha)) ]
                
                painter.setBrush(QColor("#393646"))  # Fill color
                painter.setPen(QPen(QColor("#222222"), 3))  # Outline color
                painter.drawLine(Point1[0],Point1[1],Point2[0],Point2[1])
                
                ArrowTip1 = [int(Point2[0]+ArrowSize*np.cos(Alpha + ArrowDegree)) ,int(Point2[1] + ArrowSize*np.sin(Alpha + ArrowDegree))]
                ArrowTip2 = [int(Point2[0]+ArrowSize*np.cos(Alpha - ArrowDegree)) ,int(Point2[1] + ArrowSize*np.sin(Alpha - ArrowDegree))]
                
                
                painter.drawLine(Point2[0],Point2[1],ArrowTip1[0],ArrowTip1[1])
                painter.drawLine(Point2[0],Point2[1],ArrowTip2[0],ArrowTip2[1])
                
                
                
    def drawUnDirectedLines(self,painter):
        for circle in self.circles:
            for line in circle.lines:
                
                deltaX = circle.center.x() - line.center.x()
                deltaY = circle.center.y() - line.center.y()
                
                Alpha = np.atan2(deltaY,deltaX)
                
                Point1 = [int(circle.center.x() - circle.radius * np.cos(Alpha) ), int(circle.center.y() - circle.radius * np.sin(Alpha)) ]
                Point2 = [int(line.center.x() + line.radius * np.cos(Alpha) ), int(line.center.y() + line.radius * np.sin(Alpha)) ]
                
                painter.setBrush(QColor("#393646"))  # Fill color
                painter.setPen(QPen(QColor("#222222"), 3))  # Outline color
                painter.drawLine(Point1[0],Point1[1],Point2[0],Point2[1])
                
                
    def drawCircles(self,painter):
        for circle in self.circles:
             
            if(circle == self.selected_circle):
                painter.setBrush(QColor("#6D5D6E"))  # Fill color
                painter.setPen(QPen(QColor("#222222"), 3))  # Outline color
                painter.drawEllipse(circle.center, circle.radius, circle.radius)  # Draw the circle
            else:
                painter.setBrush(QColor("#505050"))  # Fill color
                painter.setPen(QPen(QColor("#222222"), 3))  # Outline color
                painter.drawEllipse(circle.center, circle.radius, circle.radius)  # Draw the circle
                

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother circles
        
        painter.setBrush(QColor("#333333"))  # Fill color
        painter.setPen(QPen(QColor("#222222"), 3))  # Outline color
        painter.drawRect(0,0,self.width(),self.height())
        
        if(self.Directed):
            self.drawDirectedLines(painter)
        else:
            self.drawUnDirectedLines(painter)
        self.drawCircles(painter)
       
        
        
    def LeftButtonEve(self,event):
        # Check if we clicked on an existing circle
            for circle in self.circles:
                
                if circle.contains(event.pos()):
                    if(self.selected_circle == None):
                        self.selected_circle = circle
                        self.dragging = True
                    elif(self.selected_circle != circle and circle not in self.selected_circle.lines):
                        self.selected_circle.lines.append(circle)
                        self.AllLines.append([circle,self.selected_circle])
                        self.selected_circle = None
                    elif(self.selected_circle != circle and circle in self.selected_circle.lines):
                        self.selected_circle.lines.remove(circle)
                        self.AllLines.remove([circle,self.selected_circle])
                        self.selected_circle = None
                    else:
                        self.selected_circle = None
                    break
                
            else:
                if self.selected_circle != None:
                    self.selected_circle = None
                    return
                for circle in self.circles:
                    if(circle.overlap(event.pos())):
                        return
                # If no circle is selected, create a new one
                new_circle = Circle(event.pos(), 30)  # Create a circle with radius 30
                self.circles.append(new_circle)
                

    def RightButtonEve(self,event):
         for circle in self.circles:
                if circle.contains(event.pos()):
                    for circle2 in self.circles:
                        if circle in circle2.lines:
                            circle2.lines.remove(circle)
                    for line in self.AllLines:
                        if line[0] == circle or line[1] == circle:
                            self.AllLines.remove(line)
                        
                    self.circles.remove(circle)
                    self.dragging = True
                    break
        
             
    
    def OnScreen(self,event):
        if(0<event.pos().x()<self.width() and 0<event.pos().y()<self.height()):
            return True
        else:
            return False 

    def mousePressEvent(self, event):
        if(not self.OnScreen(event)):
            return
        
        if event.button() == Qt.LeftButton:
            self.LeftButtonEve(event)
                
        elif event.button() == Qt.RightButton:
           self.RightButtonEve(event)
                
        self.update()  # Repaint the canvas
        

    def mouseMoveEvent(self, event):
        if(not self.OnScreen(event)):
            return
        if self.dragging and self.selected_circle:
            for circle in self.circles:
                if circle.overlap(event.pos()) and circle != self.selected_circle:
                    return
            self.dragged = True
            self.selected_circle.center = event.pos()
        self.update()  # Repaint the canvas

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.dragging:
                if not self.dragged:
                    self.dragging = False  # Deselect the circle
                    self.update()  # Repaint the canvas
                else:
                    self.dragged = False
                    self.dragging = False
                    self.selected_circle = None  # Deselect the circle
                    self.update()  # Repaint the canvas
            
    
    

        
        
       
        
            
    
        

        
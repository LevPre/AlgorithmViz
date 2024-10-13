from Imports import *
from PyQt5.QtCore import Qt, QPoint



 #................................................................................................................................................................#   
 
class Circle:
    def __init__(self, center: QPoint, radius: int , color:str):
        
        self.center = center
        self.radius = radius
        self.color = color

    def contains(self, point: QPoint) -> bool:
        return (point.x() - self.center.x()) ** 2 + (point.y() - self.center.y()) ** 2 <= self.radius ** 2
    
    def overlap(self, point: QPoint) -> bool:
        return (point.x() - self.center.x()) ** 2 + (point.y() - self.center.y()) ** 2 < (2*self.radius) ** 2 
    
    
 #................................................................................................................................................................#   
 
 
 
 
class lines:
    def __init__(self, From:Circle, To: Circle ,  color:str):
        self.From = From
        self.To = To
        self.color = color
        
        
    def contains(self, point: QPoint) -> bool:
        Slope = (self.To.center.y() - self.From.center.y()) / (self.To.center.x() - self.From.center.x())
        return -4 < point.y() - Slope * (point.x() - self.From.center.x()) - self.From.center.y() < 4 and ((self.From.center.x() < point.x() < self.To.center.x() and self.From.center.y() < point.y() < self.To.center.y()) 
                                                                                     or (self.From.center.x() > point.x() > self.To.center.x() and self.From.center.y() < point.y() < self.To.center.y())
                                                                                     or (self.From.center.x() < point.x() < self.To.center.x() and self.From.center.y() > point.y() > self.To.center.y()) 
                                                                                     or (self.From.center.x() > point.x() > self.To.center.x() and self.From.center.y() > point.y() > self.To.center.y()))
        
    def DrawDirected(self,painter):
        ArrowSize = 30
        ArrowDegree = np.pi / 12
        deltaX = self.From.center.x() - self.To.center.x()
        deltaY = self.From.center.y() - self.To.center.y()
                
        Alpha = np.atan2(deltaY,deltaX)
                
        Point1 = [int(self.From.center.x() - self.From.radius * np.cos(Alpha) ), int(self.From.center.y() - self.From.radius * np.sin(Alpha)) ]
        Point2 = [int(self.To.center.x() + self.To.radius * np.cos(Alpha) ), int(self.To.center.y() + self.To.radius * np.sin(Alpha)) ]
                
                
        painter.setBrush(QColor(self.color))  
        painter.setPen(QPen(QColor(self.color), 3))  
        painter.drawLine(Point1[0],Point1[1],Point2[0],Point2[1])
                
        ArrowTip1 = [int(Point2[0]+ArrowSize*np.cos(Alpha + ArrowDegree)) ,int(Point2[1] + ArrowSize*np.sin(Alpha + ArrowDegree))]
        ArrowTip2 = [int(Point2[0]+ArrowSize*np.cos(Alpha - ArrowDegree)) ,int(Point2[1] + ArrowSize*np.sin(Alpha - ArrowDegree))]
                
                
        painter.drawLine(Point2[0],Point2[1],ArrowTip1[0],ArrowTip1[1])
        painter.drawLine(Point2[0],Point2[1],ArrowTip2[0],ArrowTip2[1])    
    
    def drawUnDirected(self,painter):
        deltaX = self.From.center.x() - self.To.center.x()
        deltaY = self.From.center.y() - self.To.center.y()
                
        Alpha = np.atan2(deltaY,deltaX)
                
        Point1 = [int(self.From.center.x() - self.From.radius * np.cos(Alpha) ), int(self.From.center.y() - self.From.radius * np.sin(Alpha)) ]
        Point2 = [int(self.To.center.x() + self.To.radius * np.cos(Alpha) ), int(self.To.center.y() + self.To.radius * np.sin(Alpha)) ]
                
                
        painter.setBrush(QColor(self.color))  
        painter.setPen(QPen(QColor(self.color), 3)) 
        painter.drawLine(Point1[0],Point1[1],Point2[0],Point2[1])
  #................................................................................................................................................................#      

class Canvas(QWidget):
    def __init__(self,timer):
        super().__init__()
        self.setMinimumSize(700, 400) 
        self.circles = [] 
        self.selected_circle = None  
        self.dragging = False
        self.dragged = False
        self.Directed = True
        self.Lines = []
        self.is_animating = False
        self.timer = timer
        self.AnimatedLines = []
        self.Started = []

        
        
        
    def drawDirectedLines(self,painter,color = "#222222"):
        for line in self.Lines:
            line.DrawDirected(painter)         
                
                
    def drawUnDirectedLines(self,painter):
        for line in self.Lines:
            line.drawUnDirected(painter) 
                
                       
    def drawCircles(self,painter):
        for circle in self.circles:
            if(circle == self.selected_circle):
                painter.setBrush(QColor("#ffffff"))  
            else:
                painter.setBrush(QColor(circle.color))  
            painter.setPen(QPen(QColor("#222222"), 3))  
            painter.drawEllipse(circle.center, circle.radius, circle.radius)


    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  
        
        painter.setBrush(QColor("#333333"))  
        painter.setPen(QPen(QColor("#222222"), 3))  
        painter.drawRect(0,0,self.width(),self.height())
    
       
        if(self.Directed):
            self.drawDirectedLines(painter)
        else:
            self.drawUnDirectedLines(painter)
       

        self.drawCircles(painter)
       
        
    def LineExists(self, From , To):
        for line in self.Lines:
            if(line.From ==  From and line.To == To):
                return [True , line]
        return False
    
    
    
    def LeftButtonEve(self,event):
        

       
        for circle in self.circles:
                
            if circle.contains(event.pos()):
                if(self.selected_circle == None):
                    self.selected_circle = circle
                    self.dragging = True
                elif(self.selected_circle != circle and not self.LineExists(self.selected_circle,circle)):
                    
                    self.Lines.append(lines(self.selected_circle , circle , "#222222" ))
                    self.selected_circle = None
                   
                elif(self.selected_circle != circle and self.LineExists(self.selected_circle,circle)[0]):
                    
                    self.Lines.remove(self.LineExists(self.selected_circle,circle)[1])
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
            
               
            new_circle = Circle(event.pos(), 30 , "#505050")  
            self.circles.append(new_circle)
                

    def RightButtonEve(self,event):
        for circle in self.circles:
             
                if circle.contains(event.pos()):
                    temp = []
                    for line in self.Lines:
                        if (line.From == circle or line.To == circle):
                            temp.append(line)
                            
                    for t in temp:
                        self.Lines.remove(t)
                            
                        
                    self.circles.remove(circle)
                    self.dragging = True
                    return
                
        for line in self.Lines:
            if(line.contains(event.pos())):
                self.Lines.remove(line)
                return
         
        
             
    
    def OnScreen(self,event):
        if(0<event.pos().x()<self.width() and 0<event.pos().y()<self.height()):
            return True
        else:
            return False 

    def mousePressEvent(self, event):
        
        
        if(not self.OnScreen(event)):
            return

        if(self.is_animating):
            self.StopAnimation()
            return
        
        if event.button() == Qt.LeftButton:
            self.LeftButtonEve(event)
                
        elif event.button() == Qt.RightButton:
           self.RightButtonEve(event)
                
        self.update()  
        

    def mouseMoveEvent(self, event):
        if(not self.OnScreen(event)):
            return
        if self.dragging and self.selected_circle:
            for circle in self.circles:
                if circle.overlap(event.pos()) and circle != self.selected_circle:
                    return
            self.dragged = True
            self.selected_circle.center = event.pos()
        self.update()  

    def mouseReleaseEvent(self, event):
        if event.button() == Qt.LeftButton:
            if self.dragging:
                if not self.dragged:
                    self.dragging = False  
                    self.update() 
                else:
                    self.dragged = False
                    self.dragging = False
                    self.selected_circle = None  
                    self.update()  
            
    
    def StopAnimation(self):
            self.timer.disconnect()
            self.timer.stop()
            self.is_animating =False
            for circle in self.circles:
                circle.color = "#505050"
            for line in self.Lines:
                line.color =  "#222222"
            self.update()

        
    def ResetAnimation(self):
        self.timer.disconnect()
        self.timer.stop()
        self.is_animating =False
        self.AnimatedLines = []
        for circle in self.circles:
            circle.color = "#505050"
        for line in self.Lines:
            line.color =  "#222222"    
        self.update()
       
        
            
    
        

        
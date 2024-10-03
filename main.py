import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout
from PyQt5.QtGui import QPainter, QColor, QPen
from PyQt5.QtCore import Qt, QPoint

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
    def __init__(self):
        super().__init__()
        self.setMinimumSize(400, 300)  # Set minimum size for the canvas
        self.circles = []  # List to hold circles
        self.selected_circle = None  # Track the currently selected circle
        self.dragging = False
        self.dragged = False

    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)  # Enable antialiasing for smoother circles
        
        for circle in self.circles:
            for line in circle.lines:
                painter.setBrush(QColor(255, 150, 255))  # Fill color
                painter.setPen(QPen(QColor(0, 0, 255), 2))  # Outline color
                print(line.center)
                print(circle.center.x(),circle.center.y(),line.center.x(),line.center.y())
                painter.drawLine(circle.center.x(),circle.center.y(),line.center.x(),line.center.y())
        
        

        for circle in self.circles:
            
                
            if(circle == self.selected_circle):
                painter.setBrush(QColor(255, 150, 255))  # Fill color
                painter.setPen(QPen(QColor(0, 0, 255), 2))  # Outline color
                painter.drawEllipse(circle.center, circle.radius, circle.radius)  # Draw the circle
            else:
                painter.setBrush(QColor(100, 150, 255))  # Fill color
                painter.setPen(QPen(QColor(0, 0, 255), 2))  # Outline color
                painter.drawEllipse(circle.center, circle.radius, circle.radius)  # Draw the circle
            

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            # Check if we clicked on an existing circle
            for circle in self.circles:
                
                if circle.contains(event.pos()):
                    if(self.selected_circle == None):
                        self.selected_circle = circle
                        self.dragging = True
                    elif(self.selected_circle != circle):
                        self.selected_circle.lines.append(circle)
                        self.selected_circle = None
                    else:
                        self.selected_circle = None
                    break
                
            else:
                for circle in self.circles:
                    if(circle.overlap(event.pos())):
                        return
                # If no circle is selected, create a new one
                new_circle = Circle(event.pos(), 30)  # Create a circle with radius 30
                self.circles.append(new_circle)
                
                
        elif event.button() == Qt.RightButton:
            for circle in self.circles:
                if circle.contains(event.pos()):
                    self.circles.remove(circle)
                    self.dragging = True
                    break
                
        self.update()  # Repaint the canvas
        

    def mouseMoveEvent(self, event):
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
            
                    
           
                
          
                
            


       

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Circle Drawing App")
        self.setGeometry(100, 100, 600, 400)  # Set window size

        # Create a canvas instance
        self.canvas = Canvas()
        self.setCentralWidget(self.canvas)  # Set the canvas as central widget

def main():
    app = QApplication(sys.argv)  
    window = MainWindow()
    window.show()  # Show the main window
    sys.exit(app.exec_())  # Run the application

if __name__ == "__main__":
    main()

import tkinter as tk
import numpy as np

# List to store the IDs and coordinates of the circles
circles = []
lines = []
pressed = [True,[],None]

# Function to check if there is already a circle at the clicked position
def circle_exists(x, y, r):
    for circle_id, (x1, y1, x2, y2) in circles:
        # Check if the click is inside the bounds of an existing circle
        if x1-r <= x <= x2+r and y1-r <= y <= y2+r:
            return [True,[x1, y1, x2, y2],circle_id]
    return [False,None,None]

# Function to create a circle on canvas at the clicked position (Button-1)
def draw_circle(event):
    
    x, y = event.x, event.y
    r = 20
    # radius of the circle
    # Check if a circle already exists at this position
    hel =  circle_exists(x, y, r)
    if hel[0]:
        if(pressed[0]):
            pressed[1] = hel[1]
            pressed[2] = hel[2]
            pressed[0] = False
        
            canvas.itemconfig(hel[2] , fill="pink")
            return
        else:
            line = canvas.create_line(hel[1][0]+r , hel[1][1]+r, pressed[1][0]+r , pressed[1][1]+r ,width=5)
            lines.append((line, hel[2] , pressed[2]))
            canvas.itemconfig(hel[2] , fill="white")
            canvas.itemconfig(pressed[2] , fill="white")
            pressed[0]= True
            return# Do nothing if there's already a circle

    # Draw the circle and store its ID and coordinates
    circle = canvas.create_oval(x - r, y - r, x + r, y + r, fill="white",width=5)
    circles.append((circle, (x - r, y - r, x + r, y + r)))


# Function to check if there is a circle at the clicked position (Button-2) and delete it
def delete_circle(event):
    delete = []
    x, y = event.x, event.y
    # Check if any circle exists at the clicked position
    
    
    for circle in circles:
        circle_id, coords = circle
        x1, y1, x2, y2 = coords
        # Check if the click is inside the circle
        if x1 <= x <= x2 and y1 <= y <= y2:
            canvas.delete(circle_id)  # Delete the circle
            if(circle_id == pressed[2]):
                pressed[0]=True
            circles.remove(circle)  # Remove it from the list
            for line in lines:
                if line[1] == circle_id or line[2] == circle_id :
                    canvas.delete(line[0])  # Delete the circle
                    delete.append(line)  # Remove it from the lis
            for dele in delete:
                lines.remove(dele)
    
                    
            

# Create the main window
root = tk.Tk()
root.title("Click to Draw/Delete Circle")

# Create a canvas widget
canvas = tk.Canvas(root, width=1920, height=1080, bg="white")
canvas.pack()

# Bind left mouse click (Button-1) to the draw_circle function
canvas.bind("<Button-1>", draw_circle)

# Bind middle mouse click (Button-2) to the delete_circle function
canvas.bind("<Button-3>", delete_circle)

# Start the Tkinter event loop
root.mainloop()

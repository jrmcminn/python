from graphics import * #importing graphics

datafile = open("data.txt",'r') #opening the grade datafile
window = GraphWin("onscreen", 800, 800) #setting the size of the window
window.setBackground("light blue") #setting the background to blue
lines = datafile.readlines() #reading the lines in the datafile

text = Text(Point(400,60),"Comet Grades!") #setting the text to cordinates of 400,60, and stating the title of this project
text.setFace("courier") #setting the text font to courier
text.setSize(30) #setting the text size to 30
text.setStyle("bold italic")#setting the text style to bold italic
text.setTextColor("White") #setting the text colour to white
text.draw(window) #drawing the text on the window

#this text structure is the same for all four text sections, im just changing its cordinates and text values such as size and colour.

text = Text(Point(400,110),"Red circles represent grades within the 30-50% boundary")
text.setFace("helvetica")
text.setSize(10)
text.setStyle("bold italic")
text.setTextColor("Red")
text.draw(window)

text = Text(Point(400,130),"Orange circles represent grades within the 51-70% boundary")
text.setFace("helvetica")
text.setSize(10)
text.setStyle("bold italic")
text.setTextColor("Orange")
text.draw(window)

text = Text(Point(400,150), "Green circles represent grades within the 71-90% boundary")
text.setFace("helvetica")
text.setSize(10)
text.setStyle("bold italic")
text.setTextColor("Dark Green")
text.draw(window)

for line in lines:
    line = float(line) #setting line to a float vairable
    ball = Circle(Point(100,100), line) #drawing the circles cordinates to 100,100 on the window
    time.sleep(0.3) #making the circles appear every 0.3 seconds so you can visualise the difference in people grades
    ball.setFill(color_rgb(49,66,149)) #setting the circle colour 
    ball.draw(window) #drawing the ball to the window

for line in datafile: print(line) #printing the grades
y = 100 #setting the cordinates for the circle at a point of 100
p = 2 #setting the size of the first circle to 2
for i in range (16): #starting the for loop and stating that i want 16 circle to be drawn
    ball= Circle(Point(y,y),p) #setting the circle at 100 by 100 and setting the size by 2, which is declared earlier in this for loop by setting these to y and p
    ball.setFill(color_rgb(200,50,50)) #filling each circle to red
    ball.draw(window) #drawing all 16 balls to the window
    y = y + 10 #stating that i want the cordinates to go up by 10 each time, for example, 100,100, 110,110, 120,120 and so on
    p = p + 2 #stating that i want each ball to go up by a size of 2 each time

j = 300 #setting the cordinates for the circle at a point of 300
m = 4 #setting the size of the first circle to 4
for i in range (9): #starting the for loop and stating that i want 9 balls to be drawn in this section
    ball= Circle(Point(j,j),m) #setting the circle at 300 by 300 and setting the size by 4, which is declared earlier in this for loop by setting these to j and m
    ball.setFill(color_rgb(230,151,14)) #filling each circle to orange
    ball.draw(window) #drawing the circle to the windopw
    j = j + 20 #stating that i want the cordinates to go up by 20 each time, for example, 300,300, 320,320, 340,340 and so on
    m = m + 4 #stating that i want each ball to go up by a size of 4 each time
    

a = 500 #setting the cordinates for the circle at a point of 500
d = 6 #setting the size of the first circle to 6
for i in range (6): #starting the for loop and stating that i want 6 circles to be drawn
    ball= Circle(Point(a,a),d) #setting the circle at 500 by 500 and setting the size by 6, which is declared earlier in this for loop by setting these to a and d
    ball.setFill(color_rgb(25,121,1)) #filling each circle to green
    ball.draw(window) #drawing each ball to the window
    a = a + 30 #stating that i want the cordinates to go up by 30 each time, for example, 500,500, 530,530, 560,560 and so on
    d = d + 6 #stating that i want each ball to go up by a size of 6 each time

#The idea of my visuliation is to show each grade as a moving black hole, and then shooting all the grades out of it!


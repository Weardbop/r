y_diff_of_sun = 1
y_of_sun = 480/2
x_of_sun = 480
r_of_sun = 50

def setup():
    size(690,690)
    background(255)
    
def draw():
    global y_diff_of_sun
    global y_of_sun
    global x_of_sun
    global r_of_sun
    y_of_sun += y_diff_of_sun 
    background(255)
    noStroke()
    fill(252, 212, 64)
    ellipse(x_of_sun, y_of_sun, 100, 100)
    ellipse(mouseX, height - 100,100, 100)
    if (abs(mouseX - x_of_sun) < r_of_sun) and (y_of_sun == height - 100):
        y_diff_of_sun *= -1
    

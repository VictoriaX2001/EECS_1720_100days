def setup():
    size(480, 480)

def draw():
    if  mousePressed:
        fill(3)
    else:
        fill(999)
    ellipse(mouseX, mouseY,50, 80)

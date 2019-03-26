def setup():
    size(400, 400)
    textSize(50)
    textAlign(CENTER)
def draw():
    text("ha", width/2, (height/3)*2)
    print(mouseX, mouseY)
    print(hex(get(100, 100)))
    print(CODED)
    if keyPressed:
        print(keyCode)
        text("O", width/2+75, (height/3)*2)
        
    s = createShape()
    s.beginShape()
    s.fill(0, 0, 255)
    s.noStroke()
    s.vertex(120, 300)
    s.vertex(56, 59)
    s.vertex(50, 50)
    s.vertex(50, 0)
    s.endShape(CLOSE)
    shape(s, 25, 25)
    
    
    
def setup():
    size(400,400)
    face_color = color(64, 224, 208)
    eye_color = color(255, 255, 255)
    pupil_color = color(0, 0, 0)
    smileyFace(eye_color, eye_color, eye_color, 400)
    smileyFace(face_color, eye_color, pupil_color, 200)
    
    
    
    
def smileyFace(face_color, eye_color, pupil_color, face_size):   
       #smiley starts here
    fill(face_color) #smiley background
    
    
    ellipse(200,200,200,200) #smiley head
    fill(eye_color) #eye color
    ellipse(160,160,20,50)
    ellipse(240,160,20,50)
    fill(pupil_color) #pupil color
    ellipse(160,170,10,10)
    ellipse(240,170,10,10)
    noFill()
    #smile
    arc(160,200, 200, 50, 0, PI / 2.0)

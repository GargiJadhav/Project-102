import cv2
import dropbox
import random
import time

startTime = time.time()

# -------------------------------- func to take multiplesnap snapshot ----------------------
def takeSnap():
    
    num =random.randint(1,10)

    cam = cv2.VideoCapture(0)

    result = True

    while result:
        dumy , image = cam.read()

        imgname = "gargi"+ str(num) + ".png"

        cv2.imwrite(imgname,image)
        
        startTime = time.time()

        result = False
      
    

    cam.release()
    cv2.destroyAllWindows()  


# ----------------------- func to upload the imgname to the dropbox ---------------------
def uploadImage(imgname):

    accessToken = "sl.BGuqxlbJSMEUxfPkBVmmK4AuYCtxF4i0FnBAhhJbwwNOHZrBWGy7y4eTuSpse9LWIfvEIxPVkVfxZO_aus8MfCQ7QOW1Ca-rrTbL1NSkaqsIZXwYay1XmkBT9AjWEY67ViZVXUjdH7CZ"

    source = imgname

    destination = "demo/"+ imgname 
    
    dbx = dropbox.Dropbox(accessToken)

    with open(source , 'rb') as a:
        dbx.files_upload(a.read() ,destination , mode = dropbox.files.WriteMode)

    
        
def main():
    while True :
        if ( (time.time() - startTime ) >= 5 ):
            name = takeSnap()
            uploadImage(name)  


main()    
        
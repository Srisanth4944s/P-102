import cv2

def takePic():
    VCobject = cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame = VCobject.read()
        cv2.imwrite("pict.jpg",frame)
        result = False
    VCobject.release()
    cv2.destroyAllWindows()

takePic()
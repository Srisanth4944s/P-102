import cv2
import time
import random
import dropbox

global start_time

def takeSnapshot():
    number=random.randint(0,100)
    videoCaptureObject =cv2.VideoCapture(0)
    result = True
    while(result):
        ret,frame =videoCaptureObject.read()
        img_name="srisanth"+str(number)+".png"
        cv2.imwrite(img_name,frame)
        result= False
   
    print("snapshotTaken")
    videoCaptureObject.release()
    cv2.destroyAllWindows()
    return img_name



def uploadFiles(img_name):
    access_token = 'iX6JRBgPleUAAAAAAAAAAToHuWyDGLona361JGPWhPUX8AO414w7K3KANgqF9LZL'
   
    file_from = 'C:/Users/sarav/Desktop/python/c-102/'+(img_name)
    file_to = '/whitehatC101/102/'+(img_name)

    dbx=dropbox.Dropbox(access_token)
    
    with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to,mode=dropbox.files.WriteMode.overwrite)
            print("file uploaded")

def main():
    start_time=time.time()
    while(True):
        
        print(time.time()-start_time)
        
        if((time.time()-start_time)>=10):
            name=takeSnapshot()
            print(name)
            uploadFiles(name)
            start_time=time.time()

main()

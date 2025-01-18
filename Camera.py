import cv2 
camera = cv2.VideoCapture(0) 

if (camera.isOpened()): 
    print("The camera is open lol")

else: 
    print("The camera is not open :(") 

frameWidth = int(camera.get(cv2.CAP_PROP_FRAME_WIDTH))
frameHEIGHT = int(camera.get(cv2.CAP_PROP_FRAME_HEIGHT)) 

frameRate = int(camera.get(cv2.CAP_PROP_FPS)) 

#fourccCode = cv2.VideoWriter_fourcc(*'DIVX')

#specificy video file name 
videoFileName = 'recordedVideo.avi'

videoDimension = (frameWidth,frameHEIGHT) 


recordedVideo = cv2.VideoWriter(videoFileName, frameRate, videoDimension) 

while True: 
    #capture the frame 
    success, frame = camera.read() 

    #if success: 
        #cv2.imshow('Captured Photo', frame)
    
    if not success: 
        print("Not able to read. End.") 
        break 
    #Display camera image 
    cv2.imshow('Camera Video', frame) 
    
#Display the camera image 
    recordedVideo.write(frame) 

    #stop camera recording w/ c 

    if cv2.waitKey(1) == ord ('c'): 
        break 
    #release capture 
    #close all windows 
recordedVideo.release()
camera.release()
cv2.destroyAllWindows() 
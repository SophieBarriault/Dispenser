import cv2
import numpy as np 
import os 

#button desc. specificy 
button_width = 200
button_height = 50
button_color = (255, 0, 0)  # button = Red 
button_text_color = (255, 255, 255)  # button text =  White 


    #button sizing 
button_x = 50
button_y = 50 




def mouse_callback(event, x, y, flags, param):
    global button_x, button_y, button_width, button_height

    if event == cv2.EVENT_LBUTTONDOWN:
        # Check if the click is inside the button area
        if button_x <= x <= button_x + button_width and button_y <= y <= button_y + button_height:
            capture_image()
            

















# Function = capture image when button is clicked
def capture_image():
    # Initialize webcam
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    
    if ret:
         # Create the full path for saving the image  
        image_path = os.path.join(r"\Downloads\New folder\c0a35e749b436348bc80c28207977cde.jpg", frame)

        # Save the captured image to the specified folder
        cv2.imwrite(image_path, frame)
        print("Image saved as captured_image.jpg")
    
    # Release the webcam
    cap.release() 



#save image as certain file 
save_folder = r"C:\Users\sophi\Downloads\New folder\c0a35e749b436348bc80c28207977cde.jpg"

# Create the folder if it doesn't exist
if not os.path.exists(save_folder):
    os.makedirs(save_folder) 













#background for window, necessary?
window = np.zeros((400, 600, 3), dtype=np.uint8)

# Display the button on the window
cv2.rectangle(window, (button_x, button_y), (button_x + button_width, button_y + button_height), button_color, -1)
cv2.putText(window, "Capture Photo", (button_x + 30, button_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, button_text_color, 2)

# Show the window
cv2.imshow("Capture Photo Button", window)

# Wait for a key event or mouse click
while True:
    key = cv2.waitKey(1) & 0xFF
    if key == 27:  # ESC key to exit
        break


# closing window clean up 
cv2.destroyAllWindows()

















# Create a black background for the window
window = np.zeros((400, 600, 3), dtype=np.uint8)

# Display the button on the window
cv2.rectangle(window, (button_x, button_y), (button_x + button_width, button_y + button_height), button_color, -1)
cv2.putText(window, "Capture Photo", (button_x + 30, button_y + 30), cv2.FONT_HERSHEY_SIMPLEX, 1, button_text_color, 2)

# Show the window
cv2.imshow("Capture Photo Button", window) 





















#camera stuff 

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

imageDimension = (frameWidth,frameHEIGHT) 


recordedImage = cv2.VideoWriter(videoFileName, frameRate, imageDimension) 



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
    recordedImage.write(frame) 

    #stop camera recording w/ c (don't need) 

    #if cv2.waitKey(1) == ord ('c'): 
        #break 
    #release capture 
    #close all windows 
#recordedImage.release()
#camera.release()
#cv2.destroyAllWindows() 
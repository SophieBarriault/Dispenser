import sys 
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout 
#from image_model import run_model #from image_model.py import function 

class MyApp(QWidget): 
    def __innit__(self): 
        super().__init__() 
        self.resize(600,300)  
        self.setWindowTitle ('Medication Application') 
        self.setContentsMargins(20, 20, 20, 20)  

        #first widget 
        #label = QLabel('Hi!!!', self) 
        #label.move(100,100) 

        # UI Elements: 

        #label/widget 
        self.label = QLabel('Running Image Recognition...', self) 
        self.label.move(200, 100) 

        #button 
        button = QPushButton('Start Webcam Feed', self)  
        button.clicked.connect(self.run_recognition) #run_recognition = defined later 
        button.move(20, 20) 

        #layout setup 

        #layout = QVBoxLayout()
        #layout.addWidget(self.label)
        #layout.addWidget(self.button)
        #self.setLayout(layout) 

    def run_recognition(self): 
         # Call the AI recognition function when the button is clicked
        #self.label.setText('Starting image recognition...') 
        #self.progress_bar.setVisible(True)  # Show progress bar during processing
        #self.progress_bar.setRange(0, 0)  # Set indeterminate progress bar 
        #model_path = './projectyolov8/runs/detect/yolov8n_custom7/weights/best.pt'  # Path to your YOLO model
        #run_model(model_path)  # Directly call the function that uses the webcam and performs inference
        #self.label.setText('Image recognition finished.') 
        #self.progress_bar.setVisible(False)  # Hide progress bar after completion 
        print("hi, sup!!!!!!!") 


#if __name__ == '__main__': 
 #   app = QApplication(sys.argv)
  #  window = MyApp()
   # window.show()
    #sys.exit(app.exec()) 

app = QApplication(sys.argv)
window = MyApp()
window.show()
sys.exit(app.exec()) 
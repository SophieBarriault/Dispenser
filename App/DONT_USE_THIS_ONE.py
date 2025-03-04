from kivy.app import App 
from kivy.lang import Builder 

class Main(App): 
    def build(self): 
        return Builder.load_file("cam.kv") 
    

    def picture_taken(self): 
        print("Got the picture!!!") 

    def change_camera(self, instance): 
        camera = instance.parent.ids.xcamera 
        if camera.index == 0: 
            camera.index = int(camera.index) + 1 
        elif camera.index == 1: 
            camera.index = int(camera.index) - 1 
        else: 
            camera.index = camera.index

Main().run() 
from kivy.app import App
from kivy.uix.label import Label 
from kivy.uix.image import Image 
from kivy.uix.camera import Camera 
from kivy.uix.boxlayout import BoxLayout 
from kivy.uix.button import Button 
from kivy.lang import Builder 
import flask 



class CameraApp(App): 

    camera_widget = '''
    MDBoxLayout:
        rows:2
        Camera:
            orientation: 'vertical'
            id: camera
            size:app.screen.size
            resolution:(720, 480)
            Rotate:
                origin:self.center
                angle:-90'''
    def menue_arabic_camera(self,*args):
        self.screen.clear_widgets()
        return_back = Button(text=self.ar_text("العودة للخلف"),
                                    pos_hint={'center_x': .5, 'center_y': .02},
                                    on_press=self.selection_load_cam_ar,
                                    font_name='DROIDKUFI-REGULAR.TTF')
        self.screen.add_widget(return_back)
        self.SHEET = Builder.load_string(camera_widget) 
        self.screen.add_widget(self.SHEET)
        CAPTURE = Button(text="Capture",
                                    pos_hint={'center_x': .5, 'center_y': .05},
                                    on_press=self.capture)
    def capture(self,*args):
            camera = self.SHEET.ids['camera']
            camera.play = not camera.play
            self.save_img()
            name = "User_sheet"
            camera.export_to_png("IMG_{}.png".format(name)) 

if __name__ == '__main__': 
    CameraApp().run()  
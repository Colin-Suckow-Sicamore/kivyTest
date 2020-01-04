from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.relativelayout import RelativeLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from network import getInfoFromCardId

import requests


class TestScreen(FloatLayout):

   def __init__(self, **kwargs):
       super(TestScreen, self).__init__(**kwargs)
      
   def quitApp(self):
       App.get_running_app().stop()

   

class ScanCard(RelativeLayout):
    def __init__(self, **kwargs):
        super(ScanCard, self).__init__(**kwargs)
        
    def showCardInfo(self, cardNumber):
       cardInfo = getInfoFromCardId(cardNumber)
       print("Got card info!")
       print(cardInfo)
       popup = Popup(title="Card Info", content=Label(text=str(cardInfo), size_hint=(70, None), height=40), size_hint=(None,None), size=(400,400))
       popup.open()
       
       
class ScanCardInfo(RelativeLayout):
    def __init__(self, **kwargs):
        super(ScanCard, self).__init__(**kwargs)

    


class KeyPad(BoxLayout):
     def __init__(self, **kwargs):
        super(KeyPad, self).__init__(**kwargs)

class MyApp(App):

    def build(self):
       Window.fullscreen = True
       Window.size = (1920, 1080)
       Window.show_cursor = 0
       return TestScreen()


if __name__ == '__main__':
    MyApp().run()





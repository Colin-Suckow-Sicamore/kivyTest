from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.button import Button


class TestScreen(BoxLayout):

   def __init__(self, **kwargs):
       super(TestScreen, self).__init__(**kwargs)
       self.orientation='horizontal'
       self.spacing=16
       quitButton = Button(text="Quit")
       quitButton.bind(on_press=self.quitApp)
       self.add_widget(quitButton)
   def quitApp(self):
      App.get_running_app().quit()

class MyApp(App):

    def build(self):
       Window.fullscreen = True
       Window.size = (1920, 1080)
       Window.show_cursor = 0
       return TestScreen()


if __name__ == '__main__':
    MyApp().run()


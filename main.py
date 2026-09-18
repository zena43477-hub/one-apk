from kivy.app import App
from kivy.uix.label import Label

class T(App):
    def build(self):
        print(1)
        return Label(text="1")

T().run()

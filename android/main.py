#!/usr/bin/pathon3

import kivy
from kivy.app import App
kivy.require('1.9.0')
from kivy.uix.widget import Widget
from kivy.uix.textinput import TextInput
from kivy.uix.label import Label

from kivy.uix.relativelayout import RelativeLayout
from kivy.lang import Builder
Builder.load_file("layout.kv")

class textinp(Widget):
    def __init__(self, **kwargs):
        super(textinp, self).__init__(**kwargs)
        self.add_widget(Label(text="Name: "))  # Add a label widget 

class MainApp(App):
    def build(self):
        return textinp()

    def process(self):
        input = self.root.ids.input.text
        it = 0
        if input[-1] == '\n':
            it += 1
            try:
                input = eval(self.root.ids.input.text)
            except:
                input = self.root.ids.input.text
            print(f"got: {input},nl: {it}")

if __name__ == "__main__":
    MainApp().run()

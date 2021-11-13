#https://kivycoder.com/how-to-update-labels-python-kivy-gui-tutorial-14/
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.lang import Builder

Builder.load_file('update_label.kv')

class MyLayout(Widget):
    def __init__(self):
        Widget.__init__(self)
        self.var = ""
        
    def process_text(self):
        input = self.ids.input_id.text
        res, text = 0, ""
        if len(input) > 1 and input[-1] == '=':#if '=' found
            self.var = input
            text += self.var
        if len(input) >= 1 and input[-1] == '\n':
            input = self.ids.input_id.text
            exp = input[len(self.var):].replace(" ", "")
            self.vars = input.split("=")
            try:
                res = eval(exp)
            except:
                res = exp[:-1] + "\t>[N/A]"
            print(f"got: {input}\n res: {res}\n exp: {exp}")
            print(f"vars: {self.vars}")
        self.ids.label_id.text = f"{text} => {res}"

class AwesomeApp(App):
    def build(self):
        return MyLayout()

if __name__ == '__main__':
    AwesomeApp().run()


from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput


class Interface(FloatLayout):
    def display_information(self):
        data=self.ids.textInput.text
        self.ids.label.text=data

    # def __init__(self,**kwargs):
    #     super().__init__(**kwargs)
    #     btn=Button(text="Hello_world",size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y":0.5})
    #     label = Label(text=" hello", font_size="32px", color=(0, 1, 0, 1,), size_hint=(0.5, 0.5),
    #                   pos_hint={"center_x": 0.5, "center_y": 0.6})
    #     text_input=TextInput(size_hint=(0.5,0.1),pos_hint={"center_x":0.5,"center_y":0.7})
    #
    #     self.add_widget(text_input)
    #     self.add_widget(label)
    #     self.add_widget(btn)
class projectapp(App):
    pass
        # return Interface()

projectapp().run()

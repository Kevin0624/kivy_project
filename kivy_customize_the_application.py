# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 14:18:34 2018

@author: nutn csie
"""

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
#
class LoginScreen(GridLayout):
    
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='User name'))
        self.username = TextInput(multiline=False)
        self.add_widget(self.username)
        self.add_widget(Label(text='password'))
        self.password=TextInput(password=True, multiline=False)
        self.add_widget(self.password)
        
class MyApp(App):
    
    def build(self):
        return LoginScreen()

if __name__ =='__main__':
    MyApp().run()


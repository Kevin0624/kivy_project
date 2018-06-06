# -*- coding: utf-8 -*-
"""
Created on Wed Jun  6 13:52:00 2018

@author: nutn csie
"""

import kivy
kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.label import Label

class MyApp(App):
    def build(self):
        return Label(text="Hello World")


if __name__ == '__main__':
    MyApp().run()
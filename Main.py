import kivy

kivy.require('1.11.1')  # replace with your current kivy version !
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen, FadeTransition
from kivy.uix.textinput import TextInput
from kivy.uix.behaviors import ButtonBehavior
from kivy.uix.image import Image, AsyncImage
from kivy.uix.gridlayout import GridLayout
from kivy.uix.dropdown import DropDown
from kivy.properties import ObjectProperty
from kivy.base import runTouchApp


class DropBut(Button):
    pass


# Workout class
class Workout:
    def __int__(self, name, sets, reps):
        self.name = name
        self.sets = sets
        self.reps = reps


# Screen Manager Class for multiple screens
class ScreenManagement(ScreenManager):
    def __init__(self, **kwargs):
        super(ScreenManagement, self).__init__(**kwargs)


# Image button class for button images
class ImageButton(ButtonBehavior, AsyncImage):
    pass


# First Page (Enter)
class FirstPage(Screen):
    def __init__(self, **kwargs):
        super(FirstPage, self).__init__(**kwargs)
        # Background image using AsyncImage
        aimg = AsyncImage(source="https://images4.alphacoders.com/805/805233.jpg", size_hint=(1, 1),
                          pos_hint={'x': .01, 'y': .01})
        aimg.opacity = .5
        self.add_widget(aimg)
        # Button image
        self.submit = ImageButton(source="https://www.philcooke.com/wp-content/uploads/2010/10/iu-1.png",
                                  size_hint=(.1, .1))
        self.add_widget(self.submit)
        # When button is pressed, transition to next screen
        self.submit.bind(on_press=self.screen_transition)

    # Screen transition method
    def screen_transition(self, *args):
        self.manager.current = 'Homepage'


# Second Page (Homepage)
class SecondPage(Screen):
    def __init__(self, **kwargs):
        super(SecondPage, self).__init__(**kwargs)
        # Background image using AsyncImage
        aimg = AsyncImage(source="https://www.sketchappsources.com/resources/source-image/geometry-background.png")
        aimg.opacity = .5
        self.add_widget(aimg)
        # Homepage label
        self.add_widget(Label(text='Homepage', size_hint=(.3, .1), pos_hint={'x': .01, 'y': .01}, font_size=12))
        # Widgets for workout inputs
        self.add_widget(Label(text='Workout 1', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .7}))
        self.workout1 = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .7})
        self.add_widget(self.workout1)
        self.add_widget(Label(text='Workout 2', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .5}))
        self.workout2 = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .5})
        self.add_widget(self.workout2)
        self.add_widget(Label(text='Workout 3', size_hint=(.45, .1), pos_hint={'x': .05, 'y': .3}))
        self.workout3 = TextInput(multiline=False, size_hint=(.45, .1), pos_hint={'x': .5, 'y': .3})
        self.add_widget(self.workout3)

        # Need to pass values to ThirdScreen
        # Need a monday-friday setup
        # Need sets and reps possibly can add as additional inputs in SecondPage and then append together self.workout1 + self.workout2 + self.workout3 where 1 is the exercise 2 is the sets 3 is the reps
        store = [self.workout1, self.workout2, self.workout3]

        # Button image and transition
        self.submit = ImageButton(
            source="http://www.clker.com/cliparts/1/f/a/2/1349807104707654381Next%20Button.svg.med.png",
            size_hint=(.1, .1))
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.screen_transition)

    # Method to go to next Screen
    def screen_transition(self, *args):
        self.manager.current = 'Schedule'


# ThirdPage (Schedule from inputs)
class ThirdPage(Screen):
    def __init__(self, **kwargs):
        super(ThirdPage, self).__init__(**kwargs)
        layout = GridLayout()
        self.add_widget(layout)


        # # create a dropdown with 10 buttons
        # dropdown = DropDown()
        # for index in range(3):
        #
        #     # Adding button in drop down list
        #     btn = Button(text='Value % d' % index, size_hint_y=None, height=40)
        #
        #     # binding the button to show the text when selected
        #     btn.bind(on_press=lambda btn: dropdown.select(btn.text))
        #
        #     # then add the button inside the dropdown
        #     dropdown.add_widget(btn)
        # # create a big main button
        # mainbutton = Button(text='Hello', size_hint=(None, None), pos=(350, 300))
        # mainbutton.bind(on_release=dropdown.open)
        # # dropdown list and assign the data to the button text.
        # dropdown.bind(on_select=lambda instance, x: setattr(mainbutton, 'text', x))
        #

        # Main class
class MyApp(App):
    def build(self):
        sm = ScreenManagement(transition=FadeTransition())
        sm.add_widget(FirstPage(name='Workout App'))
        sm.add_widget(SecondPage(name='Homepage'))
        sm.add_widget(ThirdPage(name='Schedule'))
        return sm


if __name__ == '__main__':
    MyApp().run()

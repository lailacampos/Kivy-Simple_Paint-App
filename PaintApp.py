# Useful links:
# https://kivy.org/doc/stable/tutorials/firstwidget.html

from random import random
from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import Color, Ellipse, Line


class MyPaintWidget(Widget):
    def on_touch_down(self, touch):

        # By using the with statement with it, all successive drawing commands that are properly indented will modify this canvas.
        with self.canvas:
            Color(random(), random(), random())

            # The diameter for the circle that will be drawn
            diameter = 30.

            # To draw a circle, we simply draw an Ellipse with equal width and height

            # We need to shift the ellipse by -d/2 in the x and y directions (i.e. left and downwards) because the position
            # specifies the bottom left corner of the ellipse’s bounding box, and we want it to be centered around our touch.
            Ellipse(pos=(touch.x - diameter/2, touch.y - diameter/2), size=(diameter, diameter))

            # touch.ud is a Python dictionary that allows for storing custom attributes for a touch
            # We want to modify the line later, so we store a reference to it in the touch.ud dictionary under named key ‘line’
            touch.ud['line'] = Line(points=(touch.x, touch.y))

    def on_touch_move(self, touch):

        # Add the current position of the touch as a new point
        touch.ud['line'].points += [touch.x, touch.y]


class MyApp(App):
    def build(self):

        # Create a dummy Widget() object as a parent for both our painting widget and the button we’re about to add.
        # This widget does  nothing except holding the two widgets we will now add to it as children
        parent = Widget()
        self.painter = MyPaintWidget()
        clearBtn = Button(text='Clear')

        # Bind the button’s on_release event (which is fired when the button is pressed and then released) to the callback function clear_canvas
        clearBtn.bind(on_release=self.clear_canvas)
        parent.add_widget(self.painter)
        parent.add_widget(clearBtn)
        return parent

    def clear_canvas(self, obj):
        self.painter.canvas.clear()


if __name__ == '__main__':
    MyApp().run()

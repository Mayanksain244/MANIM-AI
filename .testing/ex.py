from manim import *

class HelloManim(Scene):
    def construct(self):
        text = Text("Hello, Manim!")
        self.play(Write(text))

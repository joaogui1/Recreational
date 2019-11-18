import numpy as np
from manimlib.imports import *

class MoreShapes(Scene):
    def construct(self):
        circle = Circle(color=PURPLE_A)
        rectangle = Rectangle(height=2, width=3)
        ellipse = Ellipse(width=3, height=1, color=RED)
        ellipse.shift(2*DOWN+2*RIGHT)
        pointer = CurvedArrow(2*UP,4*RIGHT,color=MAROON_C)
        arrow = Arrow(LEFT,UP)
        arrow.next_to(circle,DOWN+LEFT)
        rectangle.next_to(arrow,DOWN+LEFT)
        ring = Annulus(inner_radius=np.sqrt(2), outer_radius=2, color=BLUE)
        # ring.next_to(ellipse, RIGHT)
        pentagon = Polygon(np.array([-0.8 ,-0.8 ,0]), np.array([-1.4 ,0.85, 0]), np.array([0,np.sqrt(2) + 0.4,0]), np.array([1.4, 0.85, 0]), np.array([0.8, -0.8, 0]))
        ring.surround(pentagon)
        
        self.add(pointer)
        self.play(FadeIn(pentagon))
        self.play(GrowArrow(arrow))
        self.play(GrowFromCenter(rectangle), GrowFromCenter(ellipse), GrowFromCenter(ring))
        self.play(Rotating(pentagon))

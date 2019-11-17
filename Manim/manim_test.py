from manimlib.imports import *

class Shapes(Scene):
    #A few simple shapes
    def construct(self):
        circle = Circle()
        square = Square()
        line = Line(np.array([3,0,0]),np.array([5,0,0]))
        triangle = Polygon(np.array([0,0,0]),np.array([1,1,0]),np.array([1,-1,0]))

        self.play(ShowCreation(circle))
        self.play(Transform(circle, square))
        # self.play(FadeOut(circle))
        self.add(line)
        self.play(Transform(circle, triangle))

from manimlib.imports import *

class BasicEquations(Scene):
    #A short script showing how to use Latex commands
    def construct(self):
        eq1 = TextMobject("$\\vec{X}_0 \\cdot \\vec{Y}_1 = 3$")
        eq1.shift(2*UP)
        #Using TexMobject instead of TextMobject and raw string instead of scaping
        eq2 = TexMobject(r"\vec{F}_{net} = \sum_i \vec{F}_i")
        eq2.shift(2*DOWN)

        self.play(Write(eq1))
        self.play(Write(eq2))
        self.wait(2)

class ColoringEquations(Scene):
    #Grouping and coloring parts of equations
    def construct(self):
        line1 = TexMobject(r"\text{The vector } \vec{F}_{net} \text{ is the net }", r"\text{force }", r"\text{on object of mass }")
        line1.set_color_by_tex("force", BLUE)
        line2 = TexMobject("m", "\\text{ and acceleration }", "\\vec{a}", ".  ")
        line2.set_color_by_tex_to_color_map({
            "m": YELLOW,
            "{a}": RED
        })
        sentence = VGroup(line1,line2)
        sentence.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        self.play(Write(sentence))
        self.wait(2)
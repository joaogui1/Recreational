from manimlib.imports import *

class ActionValue(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        # eq1_text=["4","x","+","3","y","=","0"]
        # eq2_text=["5","x","-","2","y","=","3"]
        eq1 = TexMobject(r"V_{\pi}(s)", r" = \mathbb{E}_{\pi}[G_t \vert S_t = s]")
        eq2 = TexMobject(r"Q_{\pi}(s, a)", r" = \mathbb{E}_{\pi}[G_t \vert S_t = s, A_t = a]")
        eqV = TexMobject(r"V_{\pi}(s)")
        eqE = TexMobject(r"=")
        eqSum = TexMobject(r"\sum_{a \in \mathcal{A}}", r"Q_{\pi}(s, a)",  r"\pi(a \vert s)")

        eqV.set_color(BLUE)
        eq1.set_color(BLUE)
        eq2.set_color(YELLOW)
        eqSum.set_color_by_tex("Q", YELLOW)

        eqE.shift(0.5*UP + LEFT)
        eqV.next_to(eqE, LEFT)
        eqSum.next_to(eqE, RIGHT)
        eqSum.shift(0.15*DOWN)
      
        for i, item in enumerate(eq1):
            item.align_to(eq2[i], LEFT)
        eq1.shift(0.7*RIGHT + UP)
        eq2.shift(0.7*RIGHT)
        eq_group = VGroup(eq1,eq2)
        braces = Brace(eq_group,LEFT)
        eq_text = braces.get_text("Value equations")

        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))
        self.wait(5)
        self.play(FadeOut(eq_text), FadeOut(braces))
        self.play(Transform(eq1, eqV), FadeIn(eqE), Transform(eq2, eqSum))
        self.wait(3)

class ActionState(Scene):
    #A more concise block of code with all columns aligned
    def construct(self):
        eq1 = TexMobject(r"V_{\pi}(s)", r" = \mathbb{E}_{\pi}[G_t \vert S_t = s]")
        eq2 = TexMobject(r"Q_{\pi}(s, a)", r" = \mathbb{E}_{\pi}[G_t \vert S_t = s, A_t = a]")
        eqV = TexMobject(r"V_{\pi}(s)")
        eqE = TexMobject(r"=")
        eqSum = TexMobject(r"\sum_{a \in \mathcal{A}}", r"Q_{\pi}(s, a)",  r"\pi(a \vert s)")

        eqV.set_color(BLUE)
        eq1.set_color(BLUE)
        eq2.set_color(YELLOW)
        eqSum.set_color_by_tex("Q", YELLOW)

        eqE.shift(0.5*UP + LEFT)
        eqV.next_to(eqE, LEFT)
        eqSum.next_to(eqE, RIGHT)
        eqSum.shift(0.15*DOWN)
      
        for i, item in enumerate(eq1):
            item.align_to(eq2[i], LEFT)
        eq1.shift(0.7*RIGHT + UP)
        eq2.shift(0.7*RIGHT)
        eq_group = VGroup(eq1,eq2)
        braces = Brace(eq_group,LEFT)
        eq_text = braces.get_text("Value equations")

        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))
        self.wait(5)
        self.play(FadeOut(eq_text), FadeOut(braces))
        self.play(Transform(eq1, eqV), FadeIn(eqE), Transform(eq2, eqSum))
        self.wait(3)

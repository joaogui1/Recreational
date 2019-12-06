from manimlib.imports import *

class Marginalization(Scene):
    def construct(self):
        title = Title("Marginal Distribution @iugoaoj")

        line_1_1 = TextMobject("We can rewrite the probability mass function of a random variable Y as")
        line_1_2 = TextMobject("the marginal probability of Y given the the joint distribution of X and Y")
        line_1 = VGroup(line_1_1, line_1_2)
        line_1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

        line_2_1 = TextMobject("Then we can use the definition of conditional probability to remove")
        line_2_2 = TextMobject("the dependency on the joint distribution")
        line_2 = VGroup(line_2_1, line_2_2)
        line_2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

        line_3_1 = TextMobject("The expected value of Y is a weigthed average")
        line_3_2 = TextMobject("of Y's possible values given their probabilities")
        line_3 = VGroup(line_3_1, line_3_2)
        line_3.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

        line_4_1 = TextMobject("We can combine those equations and get")
        line_4_2 = TextMobject("Y's expected value without referencing Y's distribution")
        line_4 = VGroup(line_4_1, line_4_2)
        line_4.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

        line_5 = TextMobject("Changing the order of the summations...")

        line_6 = TextMobject("And finally, using the definition of expected value we get:")

        eq1 = TexMobject(r"\mathbb P (Y = y) = p_{Y}(y) = ", r"\sum_{x \in \mathcal{R_X}} p_{X, Y}(x, y)")
        eq2 = TexMobject(r"p_{Y}(y) = ", r"\sum_{x \in \mathcal{R_X}} p_{Y \vert X}(y \vert x) \cdot p_{X}(x)")
        eq3 = TexMobject(r"\mathbb E(Y) = \sum_{y \in \mathcal{R_Y}} y \cdot p_{Y}(y)")
        eq_group = VGroup(eq2, eq3)
        eq4 = TexMobject(r"\mathbb E(Y) = \sum_{y \in \mathcal{R_Y}} y \sum_{x \in \mathcal{R_X}} p_{Y \vert X}(y \vert x) \cdot p_{X}(x)")
        eq5 = TexMobject(r"\mathbb E(Y) = \sum_{x \in \mathcal{R_X}} p_{X}(x) \sum_{y \in \mathcal{R_Y}} y \cdot p_{Y \vert X}(y \vert x)")
        eq6 = TexMobject(r"\mathbb E(Y) = \sum_{x \in \mathcal{R_X}} p_{X}(x) \cdot \mathbb E(Y \vert X)")


        line_1.next_to(title, DOWN)
        line_1.scale(0.7)

        line_2.next_to(title, DOWN)
        line_2.scale(0.7)

        line_3.next_to(title, DOWN)

        line_4.next_to(title, DOWN)

        line_5.next_to(title, DOWN)

        line_6.next_to(title, DOWN)


        # for i, item in enumerate(eq1):
        #     item.align_to(eq2[i], LEFT)    

        self.add(title)
        self.play(FadeIn(line_1))
        self.play(Write(eq1))
        self.wait(5)

        self.remove(line_1)
        self.play(Write(line_2))
        self.play(Transform(eq1, eq2))
        self.wait(5)

        self.remove(eq1)
        self.play(ApplyMethod(eq2.to_corner, DOWN))
        self.play(ApplyMethod(eq2.scale, 0.7))
        self.remove(line_2)
        self.play(Write(line_3))
        self.play(Write(eq3))
        self.wait(5)

        self.remove(line_3)
        self.play(Write(line_4))
        self.play(Transform(eq_group, eq4))
        self.wait(6)

        self.remove(line_4)
        self.play(Write(line_5))
        self.play(Transform(eq4, eq5))
        self.wait(6)
        
        self.remove(eq_group)
        self.remove(line_5)
        self.play(Write(line_6))
        self.play(Transform(eq5, eq6))
        self.remove(eq4)
        self.wait(6)


class StateValue(Scene):
    def construct(self):
        title = Title("RL State Value @iugoaoj")

        line_1 = TextMobject("The ", "state-value function", " is the")
        line_2 = TextMobject("expected value of the ", "return", " given a state under a policy")
        eq1 = TexMobject(r"V_{\pi}(s)", r" = \mathbb{E}_{\pi}[", r"G_t", r"\vert S_t = s]")
        eqG = TexMobject(r"G_t", r"= \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}")
        eq2 = TexMobject(r"V_{\pi}(s)", r"= \mathbb{E}_{\pi} \Bigg[\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \vert S_t = s \Bigg]")
        
        line_1.next_to(title, DOWN)
        line_1[1].set_color(BLUE)
        line_2.next_to(line_1, DOWN)
        line_2[1].set_color(RED)

        eq1.set_color_by_tex("V", BLUE)
        eqG.set_color_by_tex("G", RED)
        eq2.set_color_by_tex("V", BLUE)
        eq_group = VGroup(eq1, eqG)
        eq_group.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

                
        self.add(title)
        self.play(FadeIn(line_1), FadeIn(line_2))
        self.play(Write(eq_group))
        self.wait(3)
        self.play(Transform(eq_group, eq2))
        self.wait(5)

class ActionValue(Scene):
    def construct(self):
        title = Title("RL Action Value @iugoaoj")

        line_1 = TextMobject("The ", "action-value function", " is the expected value of ")
        line_2 = TextMobject("the ", "return", " if you take action a in state s under a policy")
        eq1 = TexMobject(r"Q_{\pi}(s, a)", r" = \mathbb{E}_{\pi}[", r"G_t", r"\vert S_t = s, A_t = a]")
        eqG = TexMobject(r"G_t", r"= \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}")
        eq2 = TexMobject(r"Q_{\pi}(s, a)", r"= \mathbb{E}_{\pi} \Bigg[\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \vert S_t = s, A_t = a \Bigg]")
        
        line_1.next_to(title, DOWN)
        line_1[1].set_color(YELLOW)
        line_2.next_to(line_1, DOWN)
        line_2[1].set_color(RED)

        eq1.set_color_by_tex("Q", YELLOW)
        eqG.set_color_by_tex("G", RED)
        eq2.set_color_by_tex("Q", YELLOW)
        eq_group = VGroup(eq1, eqG)
        eq_group.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)


        self.add(title)
        self.play(FadeIn(line_1), FadeIn(line_2))
        self.play(Write(eq_group))
        self.wait(3)
        self.play(Transform(eq_group, eq2))
        self.wait(5)

class ActionState(Scene):
    def construct(self):
        title = Title("RL Action-State relation @iugoaoj")
        line_1 = TextMobject("We can use the probability distribution given by the policy")
        line_2 = TextMobject("to relate these two functions")
        
        line_1.next_to(title, DOWN)
        line_2.next_to(line_1, DOWN)

        eq1 = TexMobject(r"V_{\pi}(s) = \mathbb{E}_{\pi}[G_t \vert S_t = s]")
        eq2 = TexMobject(r"Q_{\pi}(s, a) = \mathbb{E}_{\pi}[G_t \vert S_t = s, A_t = a]")
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
        braces = Brace(eq_group, LEFT)
        eq_text = braces.get_text("Value equations")

        self.add(title)
        self.play(FadeIn(line_1), FadeIn(line_2))
        self.wait(3)
        self.play(Write(eq1),Write(eq2))
        self.play(GrowFromCenter(braces),Write(eq_text))
        self.wait(5)
        self.play(FadeOut(eq_text), FadeOut(braces))
        self.play(Transform(eq1, eqV), FadeIn(eqE), Transform(eq2, eqSum))
        self.wait(5)

from manimlib.imports import *

class Policy(Scene):
    def construct(self):
        title = Title("RL Policy @iugoaoj")

        line_1 = TextMobject("The ", "policy", " is the function that given the state")
        line_2 = TextMobject("tells the agent what to do. It can be:")

        def_1 = TextMobject("Deterministic")
        def_2 = TextMobject("Probabilistic")
        
        eq1 = TexMobject(r"\pi(s)", r" = a")
        eq2 = TexMobject(r"\pi(a \vert s)", r"= \mathbb{P}_\pi [A=a \vert S=s]")


        line_1.next_to(title, DOWN)
        line_1[1].set_color(RED)
        line_2.next_to(line_1, DOWN)

        eq1.set_color_by_tex("pi", RED)
        eq2.set_color_by_tex("pi", RED)
        eq2.set_color_by_tex("P", WHITE)     
        eq2.next_to(eq1, DOWN)  

        for i, item in enumerate(eq1):
            item.align_to(eq2[i], LEFT)    

        def_1.next_to(eq1, LEFT)
        def_2.next_to(eq2, LEFT)
        def_2.align_to(def_1, LEFT)

        self.add(title)
        self.play(FadeIn(line_1), FadeIn(line_2))
        self.play(FadeIn(def_1))
        self.play(Write(eq1))
        self.wait(3)
        self.play(FadeIn(def_2))
        self.play(Write(eq2))
        self.wait(5)


class Return(Scene):
    def construct(self):
        title = Title("RL Return @iugoaoj")

        line_1 = TextMobject("The ", "return", " is the (exponentially )discounted average")
        line_2 = TextMobject("of the future rewards")
        
        eq1 = TexMobject(r"G_t", r"= R_{t+1} + \gamma R_{t+2} + \dots")
        eq2 = TexMobject(r"G_t", r"= \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}")
        

        line_1.next_to(title, DOWN)
        line_1[1].set_color(RED)
        line_2.next_to(line_1, DOWN)

        eq1.set_color_by_tex("G", RED)
        eq2.set_color_by_tex("G", RED)       

        self.add(title)
        self.play(FadeIn(line_1), FadeIn(line_2))
        self.play(Write(eq1))
        self.wait(3)
        self.play(Transform(eq1, eq2))
        self.wait(5)

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

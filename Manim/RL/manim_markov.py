from manimlib.imports import *

class MP(Scene):
   def construct(self):
        title = Title("Markov Process @iugoaoj")

        mp1 = TextMobject("A Markov Process (or Chain) is a tuple (S, P)")
        mp2 = TextMobject("where S is a sequence of states with the",  "Markov Property")
        mp3 = TextMobject("and P is a", "transition probability matrix")
        mp = VGroup(mp1, mp2, mp3)
        mp.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        mp.next_to(title, DOWN)
        mp2.set_color_by_tex("Markov", YELLOW)
        mp3.set_color_by_tex("transition", RED)

        mprop = TextMobject("A sequence of states is Markov if")
        mtext = TextMobject("The ", "future", " is independent of the ", "past", "given the",  "present")
        mtext.set_color_by_tex("future", YELLOW)
        mtext.set_color_by_tex("past", BLUE)
        mtext.set_color_by_tex("present", RED)
        mEq = TexMobject(r"P[", r"S_{t + 1}", r"\vert S_{t}", r"]= P[", r"S_{t + 1}", r"\vert S_1, S_2, \dots, ",  r"S_{t}", "]") 
        mEq.set_color_by_tex("S_{t + 1}", YELLOW, substring=False)
        mEq.set_color_by_tex("S_1", BLUE)
        mEq.set_color_by_tex("S_{t}", RED)

        mprop.next_to(title, DOWN)
        mtext.to_corner(DOWN)

        transtext = TextMobject("A transition probability matrix is a matrix with entries:")
        transtext.next_to(title, DOWN)
        transEq = TexMobject(r"P_{i, j} = P[S_{t + 1} = S_j \vert S_t = S_i]")

        self.add(title)
        self.play(Write(mp))
        self.wait(5)
        self.play(FadeOut(mp1), FadeOut(mp3))
        self.play(Transform(mp2, mprop))
        self.play(Write(mEq))
        self.play(FadeIn(mtext))
        self.wait(5)
        self.remove(mp2)
        self.play(FadeOut(mEq))
        self.play(FadeOut(mtext))
        self.play(Write(transtext))
        self.play(Write(transEq))
        self.wait(6)


class MRP(Scene):
    def construct(self):
        title = Title("Markov Reward Process @iugoaoj")

        mp1 = TextMobject(r"A Markov Reward Process is a tuple (S, P, R, $\gamma$)")
        mp2 = TextMobject("where S is a sequence of states with the",  "Markov Property")
        mp3 = TextMobject("and P is a", "transition probability matrix")
        mp = VGroup(mp1, mp2, mp3)
        mp.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        mp.next_to(title, DOWN)
        mp2.set_color_by_tex("Markov", YELLOW)
        mp3.set_color_by_tex("transition", RED)

        mprop = TextMobject("A sequence of states is Markov if")
        mtext = TextMobject("The ", "future", " is independent of the ", "past", "given the",  "present")
        mtext.set_color_by_tex("future", YELLOW)
        mtext.set_color_by_tex("past", BLUE)
        mtext.set_color_by_tex("present", RED)
        mEq = TexMobject(r"P[", r"S_{t + 1}", r"\vert S_{t}", r"]= P[", r"S_{t + 1}", r"\vert S_1, S_2, \dots, ",  r"S_{t}", "]") 
        mEq.set_color_by_tex("S_{t + 1}", YELLOW, substring=False)
        mEq.set_color_by_tex("S_1", BLUE)
        mEq.set_color_by_tex("S_{t}", RED)

        mprop.next_to(title, DOWN)
        mtext.to_corner(DOWN)

        transtext = TextMobject("A transition probability matrix is a matrix with the entries:")
        transtext.next_to(title, DOWN)
        transEq = TexMobject(r"P_{i, j} = P[S_{t + 1} = S_j \vert S_t = S_i]")

        # line_1 = TextMobject("The ", "return", " is the (exponentially )discounted average")
        # line_2 = TextMobject("of the future rewards")
        
        # eq1 = TexMobject(r"G_t", r"= R_{t+1} + \gamma R_{t+2} + \dots")
        # eq2 = TexMobject(r"G_t", r"= \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}")
        

        # line_1.next_to(title, DOWN)
        # line_1[1].set_color(RED)
        # line_2.next_to(line_1, DOWN)

        # eq1.set_color_by_tex("G", RED)
        # eq2.set_color_by_tex("G", RED)       

        self.add(title)
        self.play(Write(mp))
        self.wait(5)
        self.play(FadeOut(mp1), FadeOut(mp3))
        self.play(Transform(mp2, mprop))
        self.play(Write(mEq))
        self.play(FadeIn(mtext))
        self.wait(5)
        self.remove(mp2)
        self.play(FadeOut(mEq))
        self.play(FadeOut(mtext))
        self.play(Write(transtext))
        self.play(Write(transEq))
        self.wait(6)

class MDP(Scene):
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

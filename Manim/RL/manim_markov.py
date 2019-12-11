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


class MDP(Scene):
    def construct(self):
        title = Title("Markov Decision Process @iugoaoj")

        mp1 = TextMobject(r"A Markov Decision Process is a tuple (S, P, A, R, $\gamma$) where")
        mp2 = TextMobject("S is defined as in Markov Chains, A is (finite) a set of actions...")
        mp = VGroup(mp1, mp2)
        mp.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        mp.next_to(title, DOWN)
        # mp3.set_color_by_tex("reward", YELLOW)
        # mp3.set_color_by_tex("discount", RED)

        ptext = TextMobject("P is augmented, now being a transition probability tensor...")
        ptext.next_to(title, DOWN)
        peq = TexMobject(r"P^{a}_{i, j} = P[S_{t + 1} = S_j \vert S_t = S_i, A_t = a]")

        # mp4 = TextMobject("R is a reward function", r"and $\gamma$", "is a discount factor")
        rewardtext = TextMobject("R is a reward function, that gives the expected immediate reward...")
        rewardtext.next_to(title, DOWN)
        rewardtext.scale(0.8)
        rewardeq = TexMobject(r"R(s, a) = \mathbb E[R_{t + 1} \vert S_t = s, A_t = a]")


        discounttext1 = TextMobject(r"and $\gamma$", "is a discount factor, used")
        discounttext2 = TextMobject(r"to compute the return or cumulative reward $G_t$")
        discounttext = VGroup(discounttext1, discounttext2)
        discounttext.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        discounttext.next_to(title, DOWN)
        returnEq1 = TexMobject(r"G_t", r"= R_{t+1} + \gamma R_{t+2} + \dots")
        returnEq2 = TexMobject(r"G_t", r"= \sum_{k=0}^{\infty} \gamma^k R_{t+k+1}")

        self.add(title)
        self.play(Write(mp))
        self.wait(5)

        self.play(FadeOut(mp))
        self.play(Write(ptext))
        self.play(Write(peq))
        self.wait(5)

        self.play(FadeOut(ptext), FadeOut(peq))
        self.play(Write(rewardtext))
        self.play(Write(rewardeq))
        self.wait(5)

        self.play(FadeOut(rewardtext), FadeOut(rewardeq))
        self.play(Write(discounttext))
        self.play(Write(returnEq1))
        self.wait(3)
        self.play(Transform(returnEq1, returnEq2))
        self.wait(3)
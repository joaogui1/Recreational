from manimlib.imports import *

class BellExp(Scene):
   def construct(self):
        title = Title("Bellman Expectation Equations @iugoaoj")

        deftxet = TextMobject("Let's remeber the definition of the value functions")
        deftxet.next_to(title, DOWN)
        eqV = TexMobject(r"V_{\pi}(s) = \mathbb{E}_{\pi}[G_t \vert S_t = s]")
        eqQ = TexMobject(r"Q_{\pi}(s, a) = \mathbb{E}_{\pi}[G_t \vert S_t = s, A_t = a]")
        eqGroup = VGroup(eqV, eqQ)
        eqGroup.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

        vq_Text = TextMobject("And the first equation relating them")
        vq_Text.next_to(title, DOWN)
        eqVQ = TexMobject(r"V_{\pi}(s) = \sum_{a \in \mathcal{A}}", r"Q_{\pi}(s, a)",  r"\pi(a \vert s)")

        q_Text = TextMobject("For the action value equation we can begin from it's definition")
        q_Text.next_to(title, DOWN)
        eqQ2 = TexMobject(r"Q_{\pi}(s, a) = \mathbb{E}_{\pi}\Bigg[\sum_{k=0}^{\infty} \gamma^k R_{t+k+1} \vert S_t = s, A_t = a\Bigg]")
        
        exp_Text = TextMobject("And then extract the first term")
        exp_Text.next_to(title, DOWN)
        eqQ_exp1 = TexMobject(r"Q_{\pi}(s, a) = \mathbb{E}_{\pi}\Big[R_{t+1} + \sum_{k=1}^{\infty} \gamma^k R_{t+k+1} \vert S_t = s, A_t = a \Big]")
        eqQ_exp2 = TexMobject(r"Q_{\pi}(s, a) = \mathbb{E}_{\pi}\Big[R_{t+1} + \gamma \sum_{k=0}^{\infty} \gamma^k R_{t+k+2} \vert S_t = s, A_t = a \Big]")

        ext_Text = TextMobject("This is the immediate reward plus the return of the next state")
        ext_Text.next_to(title, DOWN)
        eqq = TexMobject(r"Q_{\pi}(s, a) =")
        eqR = TexMobject(r"\mathbb{E}_{\pi}[R_{t+1}\vert S_t = s, A_t = a]")
        eqPlus = TexMobject(" + ")
        eqG = TexMobject(r"\gamma \mathbb{E}_{\pi}[G_{t + 1} \vert S_t = s, A_t = a]")

        eq_ext = VGroup(eqq, eqR, eqPlus, eqG)
        eq_ext.arrange_submobjects()

        bracesr = Brace(eqR)
        bracesg = Brace(eqG)
        r_text = bracesr.get_text(r"$R(s, a)$")
        g_text = bracesg.get_text("Average value over the next state")
        g_text.scale(0.7)

        eqQV = TexMobject(r"Q_{\pi}(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a V_{\pi} (s')")
      
        rec_Text = TextMobject("Now we can relate the value functions from two perspectives")
        rec_Text.next_to(title, DOWN)

        bell_Text1 = TextMobject("Plugging one equation into the other we get")
        bell_Text2 = TextMobject("Bellman's Expectation Equations")
        bell_Text = VGroup(bell_Text1, bell_Text2)
        bell_Text.arrange_submobjects(DOWN,  buff=MED_LARGE_BUFF)
        bell_Text.next_to(title, DOWN)

        bellEqV = TexMobject(r"V_{\pi}(s) = \sum_{a \in \mathcal{A}} \pi(a \vert s) \big( R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a V_{\pi} (s') \big)")
        bellEqQ = TexMobject(r"Q_{\pi}(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a \sum_{a' \in \mathcal{A}} \pi(a' \vert s') Q_{\pi} (s', a')")
        bellEqV.next_to(bellEqQ, DOWN)

        final_text = TextMobject("That defines recursively both $Q$ and $V$")
        final_text.next_to(title, DOWN)

        self.add(title)
        self.play(Write(deftxet))
        self.play(Write(eqGroup))
        self.wait(5)

        self.play(FadeOut(deftxet), FadeOut(eqGroup))
        self.remove(eqGroup)
        self.play(Write(vq_Text))
        self.play(Write(eqVQ))
        self.wait(5)

        self.play(FadeOut(vq_Text))
        self.play(FadeOut(eqVQ))
        self.remove(eqVQ)
        self.play(Write(q_Text))
        eqQ.move_to(0.1*UP)
        self.play(Write(eqQ))
        self.wait(2)
        self.play(Transform(eqQ, eqQ2))
        self.wait(2)


        self.play(FadeOut(q_Text))
        self.play(Write(exp_Text))
        self.play(Transform(eqQ, eqQ_exp1))
        self.wait(3)
        self.play(Transform(eqQ, eqQ_exp2))
        self.wait(3)


        self.play(FadeOut(exp_Text))
        self.play(Write(ext_Text))
        self.wait(1.5)
        self.play(Transform(eqQ, eq_ext))
        self.wait(2)
        self.play(GrowFromCenter(bracesr), Write(r_text))
        self.wait(2)
        self.play(GrowFromCenter(bracesg), Write(g_text))
        self.wait(4)
        
        eqVQ.next_to(eqQV, DOWN)
        self.play(FadeOut(bracesg), FadeOut(bracesr))
        self.play(FadeOut(g_text), FadeOut(r_text))
        self.play(Transform(eqQ, eqQV))
        self.wait(2.5)
      
        self.play(FadeOut(ext_Text))
        self.play(Write(rec_Text))
        self.play(Write(eqVQ))
        self.wait(4)

        self.play(FadeOut(rec_Text))
        self.play(Write(bell_Text))
        self.play(Transform(eqQ, bellEqQ), Transform(eqVQ, bellEqV))
        self.wait(3)
        self.play(FadeOut(bell_Text))
        self.play(Write(final_text))

        self.wait(4)


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
from manimlib.imports import *

class DP(Scene):
   def construct(self):
        title = Title("Dynamic Programming @iugoaoj")

        def_text1 = TextMobject("Dynamic Programming is a method for solving")
        def_text2 = TextMobject("complex problems, also considered a programming paradigm")
        def_text = VGroup(def_text1, def_text2)
        def_text.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        def_text.next_to(title, DOWN)
        def_text.scale(0.8)
        
        informal_text1 = TextMobject("It can be understood as simplifying a decision")
        informal_text2 = TextMobject("by breaking it down into a sequence of decision steps over time")
        informal_text = VGroup(informal_text1, informal_text2)
        informal_text.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        informal_text.next_to(title, DOWN)
        informal_text.scale(0.8)

        cond_text1 = TextMobject("It needs 2 conditions to work:")
        cond_text1.next_to(title, DOWN)
        
        cond_text2_1 = TextMobject("1. Optimal substructure")
        cond_text2_2 = TextMobject("2. Overlapping subproblems")
        cond_text2 = VGroup(cond_text2_1, cond_text2_2)
        cond_text2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        cond_text2.scale(0.8)


        opt_text1_1 = TextMobject("Optimal substructure means that an optimal solution")
        opt_text1_2 = TextMobject("can be constructed from optimal solutions of its subproblems")
        opt_text1 = VGroup(opt_text1_1, opt_text1_2)
        opt_text1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        opt_text1.next_to(title, DOWN)

        opt_text2_1 = TextMobject("So we can decompose our problem in smaller subproblems")
        opt_text2_2 = TextMobject("and use their solutions to solve the original major problem")
        opt_text2 = VGroup(opt_text2_1, opt_text2_2)
        opt_text2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        opt_text2.next_to(title, DOWN)

        overlap_text1_1 = TextMobject("Overlapping subproblems means that the problem can be")
        overlap_text1_2 = TextMobject("broken down into subproblems which are reused several times")
        overlap_text1 = VGroup(overlap_text1_1, overlap_text1_2)
        overlap_text1.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        overlap_text1.next_to(title, DOWN)

        overlap_text2_1 = TextMobject("Which means we can canche the solutions of the")
        overlap_text2_2 = TextMobject("subproblems and reuse them to find the solution far faster")
        overlap_text2 = VGroup(overlap_text2_1, overlap_text2_2)
        overlap_text2.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)
        overlap_text2.next_to(title, DOWN)

        self.add(title)
        self.play(Write(def_text))
        self.wait(4)

        self.play(FadeOut(def_text))
        self.play(Write(informal_text))
        self.wait(4)

        self.play(FadeOut(informal_text))
        self.play(Write(cond_text1))
        self.play(Write(cond_text2))
        self.wait(4)

        self.play(FadeOut(cond_text1), FadeOut(cond_text2))
        self.play(Write(opt_text1))
        self.wait(4)
        self.play(Transform(opt_text1, opt_text2))
        self.wait(4)

        self.play(FadeOut(opt_text1), FadeOut(opt_text2))
        self.play(Write(overlap_text1))
        self.wait(4)
        self.play(Transform(overlap_text1, overlap_text2))
        self.wait(5)

class PolicyIt(Scene):
   def construct(self):
        title = Title("Policy Iteration @iugoaoj")

        intro_text1 = TextMobject("We can apply dynamic programming to the")
        intro_text2 = TextMobject("Bellman Equations to find an optimal policy for a given MDP")
        intro_text = VGroup(intro_text1, intro_text2)
        intro_text.arrange_submobjects(DOWN)
        intro_text.next_to(title, DOWN)


        alg_text1 = TextMobject("The algorithm is defined in 3 parts:")
        alg_text2_1 = TextMobject("1. Compute the state-value of our policy", "(Policy evaluation)")
        alg_text2_2 = TextMobject("2. Generate a greedy function based on V", "(Policy  improvement)")
        alg_text2_3 = TextMobject("3. If the policy hasn't converged, go back to 1", "(Policy iteration)")
        
        alg_text2_1.set_color_by_tex("(", BLUE)
        alg_text2_2.set_color_by_tex("(", YELLOW)
        alg_text2_3.set_color_by_tex("(", RED)

        alg_text2 = VGroup(alg_text2_1, alg_text2_2, alg_text2_3)
        alg_text1.next_to(title, DOWN)
        alg_text2.arrange_submobjects(DOWN)
        alg_text2.scale(0.8)


        eval_text = TextMobject("To evaluate a policy we use Bellman Expectation Equation")
        eval_text.next_to(title, DOWN)
        eval_eq = TexMobject(r"V_{t + 1}(s) = \sum_a \pi(a \vert s) \sum_{s', r} P(s', r \vert s, a) (r + \gamma V_t(s'))")


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
        self.play(Write(intro_text))
        self.wait(5)

        self.play(FadeOut(intro_text))
        self.play(Write(alg_text1))
        self.play(Write(alg_text2))
        self.wait(5)

        self.play(FadeOut(alg_text1), FadeOut(alg_text2))
        self.play(Write(eval_text))
        self.play(Write(eval_eq))


        # self.play(FadeOut(q_Text))
        # self.play(Write(exp_Text))
        # self.play(Transform(eqQ, eqQ_exp1))
        # self.wait(3)
        # self.play(Transform(eqQ, eqQ_exp2))
        # self.wait(3)


        # self.play(FadeOut(exp_Text))
        # self.play(Write(ext_Text))
        # self.wait(1.5)
        # self.play(Transform(eqQ, eq_ext))
        # self.wait(2)
        # self.play(GrowFromCenter(bracesr), Write(r_text))
        # self.wait(2)
        # self.play(GrowFromCenter(bracesg), Write(g_text))
        # self.wait(4)
        
        # eqVQ.next_to(eqQV, DOWN)
        # self.play(FadeOut(bracesg), FadeOut(bracesr))
        # self.play(FadeOut(g_text), FadeOut(r_text))
        # self.play(Transform(eqQ, eqQV))
        # self.wait(2.5)
      
        # self.play(FadeOut(ext_Text))
        # self.play(Write(rec_Text))
        # self.play(Write(eqVQ))
        # self.wait(4)

        # self.play(FadeOut(rec_Text))
        # self.play(Write(bell_Text))
        # self.play(Transform(eqQ, bellEqQ), Transform(eqVQ, bellEqV))
        # self.wait(3)
        # self.play(FadeOut(bell_Text))
        # self.play(Write(final_text))

        self.wait(4)


class BellOpt(Scene):
    def construct(self):
        title = Title("Bellman Optimality Equations @iugoaoj")

        deftext = TextMobject("Let's define the optimal value functions")
        deftext.next_to(title, DOWN)
        eqV = TexMobject(r"V_{*}(s) = \max_{\pi} V_{\pi}(s)")
        eqQ = TexMobject(r"Q_{*}(s, a) = \max_{\pi} Q_{\pi}(s, a)")
        eqGroup = VGroup(eqV, eqQ)
        eqGroup.arrange_submobjects(DOWN, buff=MED_LARGE_BUFF)

        exptext = TextMobject("They give us the maximal amount of expected reward")
        exptext.next_to(title, DOWN)

        optpoltext = TextMobject("But how do you get this maximal reward? By following an optimal policy!")
        optpoltext.next_to(title, DOWN)
        optpoltext.scale(0.8)
        eqpi1 = TexMobject(r"\pi_{*} = \arg\max_{\pi} V_{\pi}(s)")
        eqpi2 = TexMobject(r"\pi_{*} = \arg\max_{\pi} Q_{\pi}(s, a)")
        eqpi = VGroup(eqpi1, eqpi2)
        eqpi.arrange_submobjects(DOWN)

        rectext1 = TextMobject("Using the definitions of the optimal value functions and an")
        rectext2 = TextMobject("analogous reasoning we can obtain relationships between them")
        rectext = VGroup(rectext1, rectext2)
        rectext.arrange_submobjects(DOWN)
        rectext.next_to(title, DOWN)

        receq1 = TexMobject(r"V_*(s) = \max_{a \in \mathcal{A}} Q_*(s,a)")
        receq2 = TexMobject(r"Q_*(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a V_*(s')")
        receq = VGroup(receq1, receq2)
        receq.arrange_submobjects(DOWN)
        receq.move_to(DOWN)

        bell_Text1 = TextMobject("Plugging one equation into the other we get")
        bell_Text2 = TextMobject("Bellman's Optimality Equations")
        bell_Text = VGroup(bell_Text1, bell_Text2)
        bell_Text.arrange_submobjects(DOWN)
        bell_Text.next_to(title, DOWN)

        bellEqV = TexMobject(r"V_*(s) = \max_{a \in \mathcal{A}} \big( R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a V_*(s') \big)")
        bellEqQ = TexMobject(r"Q_*(s, a) = R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a \max_{a' \in \mathcal{A}} Q_*(s', a')")
        bellEqG = VGroup(bellEqV, bellEqQ)
        bellEqG.arrange_submobjects(DOWN)
        bellEqG.move_to(DOWN)

        self.add(title)
        self.play(Write(deftext))
        self.play(Write(eqGroup))
        self.wait(5)

        self.play(FadeOut(deftext))
        self.play(Write(exptext))
        self.wait(3)

        self.play(FadeOut(exptext))
        self.play(Write(optpoltext))
        self.play(Transform(eqGroup, eqpi))
        self.wait(5)

        self.play(FadeOut(optpoltext), FadeOut(eqGroup))
        self.play(Write(rectext))
        self.play(Write(receq))
        self.wait(5)

        self.play(FadeOut(rectext))
        self.play(Write(bell_Text))
        self.play(Transform(receq, bellEqG))
        self.wait(5)

      
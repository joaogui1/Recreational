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

        alg_text1 = TextMobject("One way to do this is through Policy Iteration:")
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

        improv_text = TextMobject("To get a better policy from V we take the greedy policy")
        improv_text.next_to(title, DOWN)
        improv_eq = TexMobject(r"\pi'(s) = \arg\max_{a \in \mathcal{A}} Q_{\pi}(s, a)")
        improv_eq2 = TexMobject(r"\pi'(s) = \arg\max_{a \in \mathcal{A}} R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a V_{t + 1} (s')")
       
        iter_text = TextMobject(r"Why is $\pi'$ better than $\pi$?")
        iter_text.next_to(title, DOWN)
        iter_eq1 = TexMobject(r"\pi'(s) = \arg\max_{a \in \mathcal{A}} Q_{\pi}(s, a)")
        iter_eq2 = TexMobject(r"Q_{\pi}(s, \pi'(s)) = \max_{a \in \mathcal{A}} \geq Q_{\pi}(s, \pi(s)) = V_{pi}(s)")
        

        equi_text1 = TextMobject("What happens once the state-value stops improving (converges)?")
        equi_text1.next_to(title, DOWN)
        equi_eq1 = TexMobject(r"Q_{\pi}(s, \pi'(s)) = \max_{a \in \mathcal{A}} Q_{\pi}(s, a) = V_{\pi}(s)")

        equi_text2 = TextMobject(r"But that's Bellman Optimality Equation, and so $\pi$ is optimal")
        equi_text2.next_to(title, DOWN)
        equi_eq2 = TexMobject(r"V_{\pi}(s) = \max_{a \in \mathcal{A}} Q_{\pi}(s, a)")
        
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
        self.wait(5)

        self.play(FadeOut(eval_text), FadeOut(eval_eq))
        self.play(Write(improv_text))
        self.play(Write(improv_eq))
        self.wait(4)
        self.play(Transform(improv_eq, improv_eq2))
        self.wait(5)

        self.play(FadeOut(improv_text), FadeOut(improv_eq))
        self.play(Write(iter_text))
        self.play(Write(iter_eq1))
        self.wait(4)
        self.play(Transform(iter_eq1, iter_eq2))
        self.wait(4)

        self.play(FadeOut(iter_text), FadeOut(iter_eq1))
        self.play(Write(equi_text1))
        self.play(Write(equi_eq1))
        self.wait(4)
        self.play(Transform(equi_eq1, equi_eq2))
        self.wait(3)
        self.play(Transform(equi_text1, equi_text2))
        self.wait(3)



class ValueIt(Scene):
   def construct(self):
        title = Title("Value Iteration @iugoaoj")

        intro_text1 = TextMobject("Another algorithm coming from the idea of applying")
        intro_text2 = TextMobject("dynamic programming tp Bellman Equations is Value Iteration")
        intro_text = VGroup(intro_text1, intro_text2)
        intro_text.arrange_submobjects(DOWN)
        intro_text.next_to(title, DOWN)

        alg_text1 = TextMobject("The algorithm is defined in 2 parts:")
        alg_text2_1 = TextMobject(r"1. For all states $s$, use BOE to update V")
        alg_text2_2 = TextMobject("2. If the state-value hasn't converged, go back to 1")
        
        alg_text2 = VGroup(alg_text2_1, alg_text2_2)
        alg_text1.next_to(title, DOWN)
        alg_text2.arrange_submobjects(DOWN)
        alg_text2.scale(0.8)

        improv_text1 = TextMobject("More specifically we do:")
        improv_text1.next_to(title, DOWN)
        improv_eq1 = TexMobject(r"V_{t + 1}(s) = \max_{a \in \mathcal{A}} R(s, a) + \gamma \sum_{s' \in \mathcal{S}} P_{ss'}^a V_{t} (s')")

        improv_text2 = TextMobject("Or in matrix form:")
        improv_text2.next_to(title, DOWN)
        improv_eq2 = TexMobject(r"\bold{V}_{t + 1} = \max_{a \in \mathcal{A}} \bold{R}(a) + \gamma \bold{P}^a \bold{V}_{t}")
       

        equi_text1 = TextMobject("What happens once the state-value stops improving (converges)?")
        equi_text1.next_to(title, DOWN)
        equi_eq1 = TexMobject(r"Q_{\pi}(s, \pi'(s)) = \max_{a \in \mathcal{A}} Q_{\pi}(s, a) = V_{\pi}(s)")

        equi_text2 = TextMobject(r"But that's Bellman Optimality Equation, and so $\pi$ is optimal")
        equi_text2.next_to(title, DOWN)
        equi_eq2 = TexMobject(r"V_{pi}(s) = \max_{a \in \mathcal{A}} Q_{\pi}(s, a)")
        
        self.add(title)
        self.play(Write(intro_text))
        self.wait(5)

        self.play(FadeOut(intro_text))
        self.play(Write(alg_text1))
        self.play(Write(alg_text2))
        self.wait(5)

        self.play(FadeOut(alg_text1), FadeOut(alg_text2))
        self.play(Write(improv_text1))
        self.play(Write(improv_eq1))
        self.wait(4)
        self.play(Transform(improv_text, improv_text2))
        self.play(Transform(improv_eq1, improv_eq2))
        self.wait(4)

        # self.play(FadeOut(improv_text), FadeOut(improv_eq))
        # self.play(Write(equi_text))
        # self.play(Write(equi_eq1))
        # self.wait(4)
        # self.play(Transform(equi_eq1, equi_eq2))
        # self.wait(6)

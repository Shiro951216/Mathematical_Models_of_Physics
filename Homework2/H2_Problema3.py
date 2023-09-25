from manim import *
from manim_physics import *

class Ex1(Scene):

    def construct(self):
        unit_circle = Circle(radius=2.5).set_color(GREEN)
        n1 = 12
        points = [unit_circle.point_from_proportion(i / n1) for i in range(n1)]
        dots = [Charge(1, add_glow=False).move_to(points[i]) for i in range(len(points))]
        dots = VGroup(*dots)
        dotc = Charge(-1, add_glow=False).move_to(unit_circle.get_center())
        vecs = [Arrow(start=dotc.get_center(), end=dots[i],
                      max_tip_length_to_length_ratio=0.04,
                      max_stroke_width_to_length_ratio=0.4) for i in range(len(points))]
        vecs = VGroup(*vecs)

        cg = VGroup(unit_circle, dots, dotc, vecs).to_edge(4*LEFT)

        t1 = Tex(r"Dado que están distribuidos como vértices de un polígono regular,").scale(0.4)
        t2 = Tex(r"los vectores formarán un polígono cerrado").scale(0.4)
        t3 = MathTex(r'\therefore \sum_{i=1}^{12} F_i = 0').scale(0.4)
        t4 = Tex(r'Luego, si eliminamos una carga, podemos plantearlo así:').scale(0.4)
        t5 = MathTex(r'\sum_{i=1}^{12} F_i = \sum_{i=2}^{12} + F_1').scale(0.4)
        t6 = MathTex(r'F_R = \sum_{i=2}^{12} = -F_1').scale(0.4)
        t7 = Tex(r'donde la magnitud de la fuerza resultante será: $\|F_R\| = F_1 = \dfrac{kqQ}{r^2}$ ').scale(0.4)

        txgroup = VGroup(t1,t2,t3,t4,t5,t6,t7).arrange(direction=DOWN, aligned_edge = LEFT).to_edge(16*LEFT + 3*UP)
        
        self.play(Create(unit_circle), run_time=1)
        self.play(FadeIn(dots, dotc), run_time=1)
        self.play(FadeIn(vecs), run_time=1)

        self.play(Write(t1),run_time=1)
        self.play(Write(t2),run_time=1)
        self.play(Write(t3),run_time=1)

        self.wait(2)

        self.play(Write(t4),
                  FadeOut(dots[0], vecs[0]),run_time=1)
        dots = dots[1:]
        vecs = vecs[1:]
        self.play(Write(t5),run_time=1)
        self.play(Write(t6),run_time=1)
        self.play(Write(t7),run_time=1)
        self.play(FadeOut(dots, unit_circle, dotc, vecs, txgroup))

        unit_circle = Circle(radius=2.5).set_color(GREEN)
        n1 = 13
        points = [unit_circle.point_from_proportion(i / n1) for i in range(n1)]
        dots = [Charge(1, add_glow=False).move_to(points[i]) for i in range(len(points))]
        dots = VGroup(*dots)
        dotc = Charge(-1, add_glow=False).move_to(unit_circle.get_center())
        vecs = [Arrow(start=dotc.get_center(), end=dots[i],
                      max_tip_length_to_length_ratio=0.04,
                      max_stroke_width_to_length_ratio=0.4) for i in range(len(points))]
        vecs = VGroup(*vecs)

        cg = VGroup(unit_circle, dots, dotc, vecs).to_edge(4*LEFT)

        t8 = Tex(r'Del mismo modo para $n=13$ cargas se cumple:').scale(0.4)
        t9 =Tex(r"Los vectores formarán un polígono cerrado").scale(0.4)
        t10 = MathTex(r'\therefore \sum_{i=1}^{13} F_i = 0').scale(0.4)
        t11 = Tex(r'Nuevamente, si eliminamos una carga, podemos plantearlo así:').scale(0.4)
        t12 = MathTex(r'\sum_{i=1}^{13} F_i = \sum_{i=2}^{13} + F_1').scale(0.4)
        t13 = MathTex(r'F_R = \sum_{i=2}^{13} = -F_1').scale(0.4)
        t14 = Tex(r'donde la magnitud de la fuerza resultante será: $\|F_R\| = F_1 = \dfrac{kqQ}{r^2}$ ').scale(0.4)
        t15 = MathTex(r'\therefore F_R = \dfrac{kqQ}{r^2}')

        tx2group = VGroup(t8,t9,t10,t11,t12,t13,t14,t15).arrange(direction=DOWN, aligned_edge = LEFT).to_edge(16*LEFT + 3*UP)

        self.play(Create(unit_circle), run_time=1)
        self.play(FadeIn(dots, dotc), run_time=1)
        self.play(FadeIn(vecs), run_time=1)
        self.play(Write(t8),run_time=1)
        self.play(Write(t9),run_time=1)
        self.play(Write(t10),run_time=1)

        self.wait(2)
        
        self.play(Write(t11),
                  FadeOut(dots[0], vecs[0]),run_time=1)
        dots = dots[1:]
        vecs = vecs[1:]
        self.play(Write(t12),run_time=1)
        self.play(Write(t13),run_time=1)
        self.play(Write(t14),run_time=1)
        self.wait(4)
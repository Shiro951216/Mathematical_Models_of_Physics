from manim import *

class Ejercicio2c(Scene):

    def construct(self):

        t1 = Tex(r'Hallamos los radio vectores para cada carga:').scale(0.45)
        t2 = MathTex(r'r_1 = (2,6) - (5,1) = (-3,5) \Longrightarrow \|r_1\| = \sqrt{34}').scale(0.45)
        t3 = MathTex(r'r_2 = (2,6) - (-3,4) = (5,2) \Longrightarrow \|r_1\| = \sqrt{29}').scale(0.45)
        t4 = Tex(r'Luego hallamos el campo de forma vectorial para cada carga:').scale(0.45)
        t5 = MathTex(r'E_1 = \dfrac{10^{-9}}{4 \pi \epsilon_0} \dfrac{(-3,5)}{(\sqrt{34})^3} = (-0.1360,0.2267) \text{ N/C} ').scale(0.45)
        t6 = MathTex(r'E_2 = \dfrac{2 \cdot 10^{-9}}{4 \pi \epsilon_0} \dfrac{(5,2)}{(\sqrt{29})^3} = (0.5757,0.2303) \text{ N/C}').scale(0.45)
        t7 = Tex(r'Sumamos las contribuciones de cada carga al campo eléctrico:').scale(0.45)
        t8 = MathTex(r'E = E_1 + E_2 = (0.4397,0.4570) \text{ N/C}').scale(0.45)
        t9 = Tex(r'Magnitud del campo eléctrico:').scale(0.45)
        t10 = MathTex(r'\|E\| = \sqrt{(0.4397)^2+(0.4570)^2} =',r'0.6342 \text{ N/C}').scale(0.45)
        t11 = Tex(r'Ángulo que forma con el eje $X$').scale(0.45)
        t12 = MathTex(r'\theta = \arctan{\left(\dfrac{0.4570}{0.4397}\right)} =', r'46.11^{\circ}').scale(0.45)
        rec1 = SurroundingRectangle(t10[1], buff = .05).set_stroke(width=1)
        rec2 = SurroundingRectangle(t12[1], buff = .05).set_stroke(width=1)
       
        t_group = VGroup(t1,t2,t3,t4,t5,t6,t7,t8,t9,VGroup(t10,rec1),t11,VGroup(t12,rec2)).arrange(direction=DOWN, aligned_edge = LEFT)
        self.add(t_group)
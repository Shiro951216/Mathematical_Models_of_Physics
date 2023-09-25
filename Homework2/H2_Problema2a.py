from manim import *
from manim_physics import *


class Anim3a(Scene):

    def construct(self):
        text1 = Tex(r"En la figura se muestran dos cargas positivas fijas $+q$ y una carga negativa").set_width(7)
        text2 = Tex(r"$-Q$ que puede moverse libremente y que se encuentra inicialmente en reposo.").set_width(7)
        text3 = Tex(r"a) Determinar las posiciones y velocidades del electrón en 30 o más ubicaciones").set_width(7)
        text4 = Tex(r"sucesivas a lo largo de su movimiento oscilatorio y graficar los resultados.").set_width(7)

        premiseGroup = VGroup(text1, text2, text3, text4).arrange(direction=0.3*DOWN).to_edge(UL) 

        ax = Axes(x_range=[0,2,1],
                  y_range=[-2,2,1],
                  x_length=4.5,
                  y_length=4,
                  tips=False,
                  axis_config={"tick_size": 0})
        
        label = ax.get_axis_labels(MathTex(r"x").scale(0.7), MathTex(r'y').scale(0.7))
        q1 = Charge(1, ax.coords_to_point(0,-1.5,0),add_glow=False)
        q2 = Charge(1, ax.coords_to_point(0,1.5,0),add_glow=False)
        q3 = Charge(-1, ax.coords_to_point(1, 0, 0),add_glow=False)
        tq1 = Tex(r"$+q$",font_size=22).next_to(q1,LEFT)
        tq2 = Tex(r"$+q$",font_size=22).next_to(q2,LEFT)
        tq3 = Tex(r"$-Q$",font_size=22).next_to(q3,UP)
        tx1 = Tex(r'$d/2$', font_size=22).next_to(ax.coords_to_point(0,0.75,0),LEFT, buff=0.1)
        tx2 = Tex(r'$d/2$', font_size=22).next_to(ax.coords_to_point(0,-0.75,0),LEFT, buff=0.1)
        tx3 = Tex(r"$x$", font_size=22).next_to(ax.coords_to_point(0.5,0,0),DOWN, buff=0.15)
        axgroup = VGroup(ax, label,q1,q2,q3,tq1,tq2,tq3,tx1,tx2,tx3).to_edge(2*LEFT+ 5*UP)

        #texto derecha
        s1 = Tex(r'La magnitud de la carga q ejercida sobre Q será:').scale(0.4) 
        s2 = MathTex(r'F_{qQ} = - k \dfrac{qQ}{r^2}').scale(0.4) 
        s3 = Tex(r'donde la distancia $r$ entre $+q$ y $-Q$ es:').scale(0.4) 
        s4 = MathTex(r'r = \sqrt{x^2+\left( \dfrac{d}{2} \right)^2}').scale(0.4) 
        s5 = Tex(r'La componente horizontal será: $F_x = F_{qQ} \cos{\theta}  = -k \dfrac{qQ}{r^2} \cos{\theta}$').scale(0.4) 
        s6 = Tex(r'Además: $\cos{\theta} = \dfrac{x}{r} = \dfrac{x}{\sqrt{x^2+\left( d/2 \right)^2}}$').scale(0.4) 
        s7 = MathTex(r'F_x = k \dfrac{qQx}{\left( x^2+\left( d/2 \right)^2 \right)^{3/2}}').scale(0.4) 
        s8 = Tex(r'La fuerza total será: $F_{total}=-2k\dfrac{qQx}{\left( x^2+\left( d/2 \right)^2 \right)^{(3/2)}}$').scale(0.4) 
        s9 = Tex(r'dado que $x \ll d: F_{total}=-2k\dfrac{qQx}{\left( d/2 \right)^3} = -16k \dfrac{qQx}{d^3}$').scale(0.4) 
        s10 = Tex(r'Por segunda Ley de Newton y movimiento armónico:').scale(0.4) 
        s11 = MathTex(r'm \ddot{x} + 16k \dfrac{qQ}{d^3} x= 0').scale(0.4) 
        s12 = Tex(r'donde $\omega = \sqrt{\dfrac{16kqQ}{md^3}}$').scale(0.4) 


        #2do texto derecha
        s01 = Tex(r'De la ecuación del movimiento con condiciones iniciales:').scale(0.4)
        s02 = Tex(r"$\ddot{x} + 16k \dfrac{qQ}{d^3} x= 0$, $x(0)=0.01$, $x'(0)=0$").scale(0.4)
        s03 = Tex(r'Donde la solución para la EDO es: $x(t)=A \cos{(\omega t)}$').scale(0.4)
        s04 = Tex(r'Consideramos los siguientes datos:').scale(0.4)
        s05 = MobjectTable(
            [[Tex(r'8.99 $\times$ ${10^9}$ N.C/m$^2$')],
            [Tex(r'9.11 $\times$ ${10^{-31}}$ kg')],
            [Tex(r'0.01 m')],
            [Tex(r'2 m')],
            [Tex(r'1 nC')],
            [Tex(r'1 nC')]],
            row_labels=[MathTex(r'K'),MathTex(r'm'),MathTex(r'x(0)'),MathTex(r'd'),MathTex(r'q'),MathTex(r'Q')],
            line_config={"stroke_width": 1}).scale(0.4)
        s06 = Tex(r'Con los datos obtenemos: $\omega = 1.4 \times 10^{11}$ rad/s').scale(0.4)
        s07 = Tex(r'Luego, la ecuación de la posición será:').scale(0.4)
        s08 = MathTex(r'x(t)=0.01 \cos{(1.4 \times 10^{11} t)}').scale(0.4)
        s09 = Tex(r'y la ecuación de la velocidad será su derivada:').scale(0.4)
        s010 = MathTex(r'v(t)= -1.4 \times 10^{9} \sin{(1.4 \times 10^{11} t)}').scale(0.4)

        #3group
        s31 = MobjectTable(
            [[Tex(r'0.01')],
       [Tex(r' 0.00958342')],
       [Tex(r' 0.0083684') ],
       [Tex(r'0.00645617')],
       [ Tex(r'0.00400604')],
       [ Tex(r'0.00122214')],
       [Tex(r'-0.00166358')],
       [Tex(r'-0.00441069')],
       [Tex(r'-0.00679033')],
       [Tex(r'-0.00860424')],
       [Tex(r'-0.00970127')],
       [Tex(r'-0.00999005')],
       [Tex(r'-0.0094465') ],
       [Tex(r'-0.00811592')],
       [Tex(r'-0.00610916')]],
            row_labels = [Tex(fr'{t}') for t in np.array([0.        , 0.20689655, 0.4137931 , 0.62068966, 0.82758621,
       1.03448276, 1.24137931, 1.44827586, 1.65517241, 1.86206897,
       2.06896552, 2.27586207, 2.48275862, 2.68965517, 2.89655172])],
            col_labels = [Tex(r'x(t) m')],
            top_left_entry = Tex(r't $(10^{-11})$s'),
            line_config={"stroke_width": 1}
        ).scale(0.4)


        s32 = MobjectTable( 
       [[Tex(r'-0.00359341')],
       [Tex(r'-0.00077827')],
       [Tex(r'0.0021017') ],
       [ Tex(r'0.00480657')],
       [ Tex(r'0.00711098')],
       [ Tex(r'0.00882294')],
       [ Tex(r'0.00979982')],
       [ Tex(r'0.00996022')],
       [ Tex(r'0.00929078')],
       [ Tex(r'0.00784728')],
       [ Tex(r'0.00574999')],
       [ Tex(r'0.00317363')],
       [ Tex(r'0.00033286')],
       [Tex(r'-0.00253564')],
       [Tex(r'-0.00519289')]],
            row_labels = [Tex(fr'{t}') for t in np.array([3.10344828, 3.31034483, 3.51724138, 3.72413793, 3.93103448,
       4.13793103, 4.34482759, 4.55172414, 4.75862069, 4.96551724,
       5.17241379, 5.37931034, 5.5862069 , 5.79310345, 6.        ])],
            col_labels = [Tex(r'x(t) m')],
            top_left_entry = Tex(r't $(10^{-11})$s'),
            line_config={"stroke_width": 1}
        ).scale(0.4)

        sv1 = MobjectTable(
            [[Tex(r'-0 ')],
       [Tex(r'-0.0039987')],
       [Tex(r'-0.00766426')],
       [Tex(r'-0.01069126')],
       [Tex(r'-0.01282752')],
       [Tex(r'-0.01389505')],
       [Tex(r'0.01380492')],
       [Tex(r'-0.01256462')],
       [Tex(r'-0.0102775')],
       [Tex(r'-0.00713411')],
       [Tex(r'-0.00339634')],
       [Tex(r'0.00062439')],
       [Tex(r'0.00459311')],
       [Tex(r'0.00817915')],
       [Tex(r'0.01108374')]],
            row_labels = [Tex(fr'{t}') for t in np.array([0.        , 0.20689655, 0.4137931 , 0.62068966, 0.82758621,
       1.03448276, 1.24137931, 1.44827586, 1.65517241, 1.86206897,
       2.06896552, 2.27586207, 2.48275862, 2.68965517, 2.89655172])],
            col_labels = [Tex(r'v(t) $(10^{11})$m/s')],
            top_left_entry = Tex(r't $(10^{-11})$s'),
            line_config={"stroke_width": 1}).scale(0.4)

        sv2 = MobjectTable([[Tex(r'0.01306489')],
       [ Tex(r'0.01395754')],
       [Tex(r'0.01368731')],
       [Tex(r'0.01227672')],
       [Tex(r'0.00984329')],
       [Tex(r'0.00658977')],
       [Tex(r'0.00278722')],
       [Tex(r'-0.00124754 ')],
       [Tex(r'-0.00517837')],
       [Tex(r'-0.00867776')],
       [Tex(r'-0.01145416')],
       [Tex(r'-0.01327626')],
       [Tex(r'-0.01399224 ')],
       [Tex(r'-0.01354246')],
       [Tex(r'-0.01196438')]],
            row_labels = [Tex(t) for t in np.array([3.10344828, 3.31034483, 3.51724138, 3.72413793, 3.93103448,
       4.13793103, 4.34482759, 4.55172414, 4.75862069, 4.96551724,
       5.17241379, 5.37931034, 5.5862069 , 5.79310345, 6.        ])],
            col_labels = [Tex(r'v(t) $(10^{11})$m/s')],
            top_left_entry = Tex(r't $(10^{-11})$s'),
            line_config={"stroke_width": 1}).scale(0.4)
        
        ax2 = Axes(x_range=[0,6.5,1],
                  y_range=[-0.015,0.015,0.005],
                  x_length=4.5,
                  y_length=4,
                  axis_config={"tick_size": 0.05,
                               'font_size': 18,
                               'tip_shape': StealthTip,
                               'tip_width': 0.03,
                               'tip_height': 0.03}).add_coordinates()
        label2 = ax2.get_axis_labels(Tex(r"$t (\times 10^{-11}$ s)").scale(0.4), MathTex(r'x(t)').scale(0.4))

        graph1 = ax2.plot(lambda x : 0.01*np.cos(1.4 * x), x_range=[0,6])

        ax3 = Axes(x_range=[0,6.5,1],
                  y_range=[-0.02,0.02,0.01],
                  x_length=4.5,
                  y_length=4,
                  axis_config={"tick_size": 0.05,
                               'font_size':18,
                               'tip_shape': StealthTip,
                               'tip_width': 0.03,
                               'tip_height': 0.03}).add_coordinates()

        label3 = ax3.get_axis_labels(Tex(r"$t (\times 10^{-11}$ s)").scale(0.4), Tex(r'$v(t)$ $(\times 10^{11}$ m/s)').scale(0.4))

        graph2 = ax3.plot(lambda x : -0.01*1.4*np.sin(1.4 * x), x_range=[0,6])

        sgroup = VGroup(s1,s2,s3,s4,s5,s6,s7,s8,s9,s10,s11,s12).arrange(direction=0.5*DOWN, aligned_edge=LEFT).to_edge(16*LEFT + UP)       
        s2goup = VGroup(s01,s02,s03,s04,s05,s06,s07,s08,s09, s010).arrange(direction=0.5*DOWN, aligned_edge=LEFT).to_edge(16*LEFT + UP)
        stgroup = VGroup(s31,s32).arrange(direction=RIGHT).to_edge(LEFT)
        st2group = VGroup(sv1,sv2).arrange(direction=RIGHT).to_edge(RIGHT)
        axg2 = VGroup(ax2,label2, graph1)
        axg3 = VGroup(ax3,label3, graph2)
        VGroup(axg2, axg3).arrange(direction=2*RIGHT)
        self.play(Write(premiseGroup),run_time=2)
        self.play(Create(ax),
                  Write(label),
                  FadeIn(q1,q2,q3,tq1,tq2,tq3,tx1,tx2,tx3), run_time=1)
        self.play(Write(s1), run_time = 1.5)
        self.play(Write(s2), run_time = 1.5)
        self.play(Write(s3), run_time = 1.5)
        self.play(Write(s4), run_time = 1.5)
        self.play(Write(s5), run_time = 1.5)
        self.play(Write(s6), run_time = 1.5)
        self.play(Write(s7), run_time = 1.5)
        self.play(Write(s8), run_time = 1.5)
        self.play(Write(s9), run_time = 1.5)
        self.play(Write(s10), run_time = 1.5)
        self.play(Write(s11), run_time = 1.5)        
        self.play(Write(s12), run_time = 1.5)
        self.wait(2)
        self.play(FadeOut(sgroup), run_time=1)
        self.play(Write(s01), run_time=1)
        self.play(Write(s02), run_time=1)
        self.play(Write(s03), run_time=1)
        self.play(Write(s04), run_time=1)
        self.play(Write(s05), run_time=1)
        self.play(Write(s06), run_time=1)
        self.play(Write(s07), run_time=1)
        self.play(Write(s08), run_time=1)
        self.play(Write(s09), run_time=1)
        self.play(Write(s010), run_time=1)
        self.wait(3)
        self.play(FadeOut(premiseGroup, axgroup, s2goup))
        self.play(Write(s31),run_time=1)
        self.play(Write(s32),run_time=1)
        self.play(Write(sv1),run_time=1)
        self.play(Write(sv2),run_time=1)
        self.wait(3.5)
        self.play(FadeOut(st2group, stgroup), run_time=1)
        self.play(Create(ax2),Create(ax3),run_time=1)
        self.play(Write(label2), Write(label3),run_time=1)
        self.play(Write(graph1), Write(graph2),run_time=1)
        self.wait(4)
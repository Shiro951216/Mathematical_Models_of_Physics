from manim import *
from manim_physics import *

class Ex1(Scene):

    def construct(self):
        text1 = Tex(r'Dos cargas positivas fijas $+Q$ se mantienen fijas a una distancia $d$ de').set_width(7)
        text2 = Tex(r'separación. Otra partícula de carga $+q$ y masa $m$ se coloca en el centro').set_width(7)
        text3 = Tex(r'de ellas, y luego se le da un pequeño desplazamiento a lo largo del eje').set_width(7)
        text4 = Tex(r'$\pm x$. Encontrar el periodo del movimiento armónico simple generado.').set_width(7)

        d = 1
        # GRUPO1
        ax1 = NumberLine(x_range = [-d, d+0.5, 1],
                         length = 6.5,
                         label_direction = UP,
                         include_tip= True,
                         tip_width=0.1,
                         tip_height=0.1,
                         tip_shape = StealthTip
                         ).add_labels(dict_values={-1: Tex('+Q'),
                                                   0: Tex('+q'),
                                                   1: Tex('+Q')},
                                      font_size=22)
        
        c1 = Charge(1,
                    ax1.number_to_point(-d),
                    add_glow=False)
        
        c2 = Charge(1,
                    ax1.number_to_point(d),
                    add_glow=False)
        
        c3 = Charge(1,
                    ax1.number_to_point(0),
                    add_glow=False)
        
        l1 = BraceBetweenPoints(c1.get_center(),
                                c2.get_center(),
                                stroke_width=0,
                                sharpness = 3,
                                buff=0.15)

        l1label = Tex(r'd', font_size=22).move_to(l1.get_center()+0.3*DOWN)

        soltext1 = Tex(r'Analizamos la carga central al ser desplazada a la derecha').scale(0.45).to_edge(LEFT + 6.2*UP)
        
        #GRUPO 2
        ax2 = NumberLine(x_range = [-d, d+0.5, 1],
                         length = 6.5,
                         label_direction = UP,
                         include_tip= True,
                         tip_width=0.1,
                         tip_height=0.1,
                         tip_shape = StealthTip,
                         tick_size=0
                         ).add_labels(dict_values={-1: Tex('+Q'),
                                                   1: Tex('+Q')},
                                      font_size=22)

        c11 = Charge(1,
                    ax2.number_to_point(-d),
                    add_glow=False)
        
        c21 = Charge(1,
                    ax2.number_to_point(d),
                    add_glow=False)
        
        circ = DashedVMobject(Circle(radius=0.1, color=RED), num_dashes=12).move_to(ax2.number_to_point(0))

        c4 = Charge(1,
                    ax2.number_to_point(0),
                    add_glow= False)
                    
        c4l = Tex("+q", font_size = 24).move_to(c4.get_center()+ 0.3 * UP)

        v1 = Vector([-1.5,0],
                    tip_length = 0.1,
                    stroke_width = 3,
                    buff=0,
                    color=RED
                    ).move_to(c4.get_left())
        
        v2 = Vector([0.7,0],
                    tip_length = 0.1,
                    stroke_width = 3,
                    buff=0,
                    color=RED
                    ).move_to(c4.get_right() + 0.7*RIGHT)
        
        v3 = Vector([-0.8,0],
                    tip_length = 0.1,
                    stroke_width = 4,
                    buff=0,
                    color=YELLOW
                    ).move_to(c4.get_left())
    
        brace = BraceBetweenPoints(circ.get_center(),
                                   circ.get_center() + 0.4*RIGHT,
                                   stroke_width=0,
                                   color = GREEN,
                                   sharpness = 3,
                                   direction= [0,1,0],
                                   buff=0.4)
        
        bracel = BraceBetweenPoints(c11.get_center(),
                                    circ.get_center() + 0.4*RIGHT,
                                    stroke_width=0,
                                    sharpness = 3,
                                    buff=0.15)
        
        bracer = BraceBetweenPoints(c4.get_center() + 0.4*RIGHT,
                                    c21.get_center(),
                                    stroke_width=0,
                                    sharpness = 3,
                                    buff=0.15)

        b_tex = brace.get_tex(r'x', buff=0.05).scale(0.45)
        bl_tex = bracel.get_tex(r'\dfrac{d}{2}+x', buff=-0.2).scale(0.45)
        br_tex = bracer.get_tex(r'\dfrac{d}{2}-x', buff=-0.2).scale(0.45)
        
        vt1 = MathTex(r"\overrightarrow{\text{F}}_1", font_size = 22).move_to(v1.get_end() + 0.2 * UL)
        vt2 = MathTex(r"\overrightarrow{\text{F}}_2", font_size = 22).move_to(v2.get_end() + 0.2 * UR)
        vt3 = MathTex(r"\overrightarrow{\text{F}}_{\text{R}}", font_size = 22).move_to(v3.get_end() + 0.25 * UL)

        soltext2 = MathTex(r'\text{donde:} ').scale(0.45).to_edge(LEFT + 12*UP)
        soltext2a = MathTex(r'\overrightarrow{\text{F}}_1 = -\dfrac{kQq}{\left(\frac{d}{2}-x \right)^2} \hat{\text{i}}').scale(0.45).next_to(soltext2, 2*RIGHT)
        soltext3 = MathTex(r'\overrightarrow{\text{F}}_2 = \dfrac{kQq}{\left(\frac{d}{2}+x \right)^2} \hat{\text{i}}').scale(0.45).next_to(soltext2a, 3*RIGHT)
        soltext4 = MathTex(r'\text{Luego: } \overrightarrow{\text{F}}_{\text{R}} = \overrightarrow{\text{F}}_1 - \overrightarrow{\text{F}}_2').scale(0.45).to_edge(LEFT + 13.5*UP)
        
        #texto solucion izq
        soltext5 = Tex(r'En el eje $X$ tenemos:').scale(0.45)
        soltext6 = MathTex(r'\text{F}_{\text{R}} = -\dfrac{kQq}{\left(\frac{d}{2}-x \right)^2} - \dfrac{kQq}{\left(\frac{d}{2}+x \right)^2}'
                          ).scale(0.45)
        soltext7 = Tex(r'$\text{F}_{\text{R}} = -kQq \left[\dfrac{1}{\left(\frac{d}{2}-x \right)^2} + \dfrac{1}{\left(\frac{d}{2}+ x \right)^2}\right]$').scale(0.45)
        soltext8 = Tex(r'$\text{F}_{\text{R}} = -\dfrac{2kQqd}{\left(\frac{d^2}{4}-x^2 \right)^2}x$').scale(0.45)
        soltext9 = Tex(r'Consideramos: $x<<d$:').scale(0.45)
        soltext10 = Tex(r'$\text{F}_{\text{R}} = -\dfrac{32kQqd}{d^4}$ $x=m \ddot{x}$').scale(0.45)
        soltext11 = Tex(r'$\ddot{x} + \dfrac{32kQq}{m d^3}$ $x = 0$').scale(0.45)
        soltext12 = Tex(r'donde: $\omega^2 = \dfrac{32kQq}{m d^3}$').scale(0.45)
        soltext13 = Tex(r'$\omega = \sqrt{\dfrac{32kQq}{m d^3}} = \dfrac{2 \pi}{T}$').scale(0.45)
        soltextf = Tex(r'$\therefore$ El periodo del M.A.S. es: $T=\dfrac{\pi}{2}\sqrt{\dfrac{m d^3}{2kQq}}$').scale(0.45)

        x = VGroup(text1, text2, text3, text4).arrange(direction = 0.3*DOWN, aligned_edge=LEFT).to_edge(UL)
        VGroup(ax1, c1, c2, c3, l1, l1label).to_edge(3.5*UP+LEFT)
        VGroup(v1, ax2, c11, c21, c4, v2, vt1, vt2, c4l, circ, brace, b_tex, bracer, bracel, bl_tex, br_tex, v3, vt3).to_edge(7*UP + LEFT)
        VGroup(soltext5, soltext6, soltext7, soltext8, soltext9, soltext10,
               soltext11,soltext12, soltext13, soltextf).arrange(direction=DOWN, aligned_edge = LEFT).to_edge(17*LEFT + UP)
        vg1 = VGroup(v1, v2)
        vg1t = VGroup(vt1, vt2)

        self.play(Write(x, run_time=4))
        self.play(Create(ax1, run_time=1),
                  FadeIn(c1, c2, c3, run_time = 1))        
        self.play(FadeIn(l1, run_time = 1),
                  Write(l1label, run_time=1))
        self.play(Write(soltext1, run_time=1))
        self.play(Create(ax2, run_time=1),
                  FadeIn(c11,c21, run_time=1))
        self.play(FadeIn(circ, c4, run_time=1),
                  Write(c4l, run_time=1))
        self.play(Write(brace),
                  Write(b_tex),
                  c4.animate.shift(0.4*RIGHT),
                  c4l.animate.shift(0.4*RIGHT), run_time=0.5)
        self.play(Create(v1, run_time=1),
                  Create(v2, run_time=1))
        self.play(Write(vt1, run_time=0.5),
                  Write(vt2, run_time=0.5))
        self.play(Write(bracel),
                  Write(bl_tex),
                  Write(bracer),
                  Write(br_tex), run_time=1)
        self.play(Write(soltext2))
        self.play(Write(soltext2a),
                  Indicate(v1),
                  Indicate(vt1), run_time=1)
        self.play(Write(soltext3),
                  Indicate(v2),
                  Indicate(vt2), run_time=1)
        self.play(Transform(vg1, v3),
                  Transform(vg1t, vt3), run_time=1)
        self.play(Write(soltext4))
        self.play(Write(soltext5))
        self.play(Write(soltext6))
        self.play(Write(soltext7))
        self.play(Write(soltext8))
        self.play(Write(soltext9))
        self.play(Write(soltext10))
        self.play(Write(soltext11))
        self.play(Write(soltext12))
        self.play(Write(soltext13))
        self.play(Write(soltextf))
        self.wait(2)

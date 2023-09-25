from manim import *
from manim_physics import *

class Hm(Scene):

    def construct(self):

        ke = 8.99 * 10 ** 9      # Coulomb's constant:                       K = 8.99*10^9 N*m^2/C^2
        m = 9.11 * 10 ** -31   # mass of the oscillating electron:         me = 9.11 * 10^-31
        A = 0.01               # Amplitud of the oscillation:              A = 1cm = 10^-2 m
        d = 2                  # Distance between the two fixed charges:   d = 2m
        Q = q = 10**-9         # Charges of the 3 charges:                 1 nC = 10^-9 C
        
        w = np.sqrt((16*ke*Q*q)/(m*d**3))       # Angular speed w calculated

        e = ValueTracker(0.001)  #Set the time value 
        font_size = 30

        axes = NumberPlane(x_range = [-3*A/2, 3*A/2, 0.005],
                           x_length = 14.222222222222222,
                           y_range = [-3*d/4, 3*d/4, 1],
                           y_length = 8,
                           x_axis_config = {"numbers_to_include": np.arange(-3*A/2, 3*A/2 + 0.005, 0.005),
                                            "font_size":20},
                           y_axis_config = {"numbers_to_include": np.arange(-d, d+1, 1),
                                            "font_size":20},
                           tips=False)
        
        c1 = Charge(1,
                    axes.coords_to_point(0,d/2),
                    add_glow=False)
        
        c2 = Charge(1,
                    axes.coords_to_point(0,-d/2),
                    add_glow=False)

        text1 = Tex("time: ",
                    font_size=font_size
                    ).to_edge(UL).add_background_rectangle(BLACK)
        
        time_value = always_redraw(lambda: DecimalNumber(num_decimal_places=1,
                                                         font_size=font_size)
                                   .set_value(e.get_value())
                                   .next_to(text1,
                                            RIGHT,
                                            buff=0.2)
                                   ).add_background_rectangle(BLACK)
        
        text2 = Tex("$\\times$ $10^{-11}$ s",
                    font_size=font_size
                    ).next_to(time_value,
                              RIGHT,
                              buff=0.2
                              ).add_background_rectangle(BLACK)
        
        graph = always_redraw(lambda: ParametricFunction(lambda t: axes.coords_to_point(A*np.cos(w*t*10**(-11)),0),
                                                         t_range=[0,e.get_value()],
                                                         color = WHITE))
        
        dot1 = always_redraw(lambda: Charge(-1,
                                            add_glow=False
                                            ).move_to(graph.get_end()))
        
        self.play(Write(axes))
        
        self.add(graph,
                 dot1,
                 c1,
                 c2,
                 text1,
                 time_value,
                 text2)

        self.play(e.animate.set_value(17.889),
                  run_time=8,
                  rate_func = linear)
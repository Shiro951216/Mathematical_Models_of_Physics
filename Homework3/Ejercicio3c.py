from manim import *
from manim_physics import *

class Ejercicio3c(Scene):
    def construct(self):
        axes = NumberPlane(x_range = [-3, 3, 1],
                           x_length = 14.222222222222222,
                           y_range = [-2, 2, 1],
                           y_length = 8,
                           x_axis_config = {"font_size":20},
                           y_axis_config = {"font_size":20},
                           tips=True).add_coordinates()

        c1 = Charge(1,
                    axes.coords_to_point(-1, -1),
                    add_glow=True)
        
        c2 = Charge(1,
                    axes.coords_to_point(1, 1),
                    add_glow=True)
        
        c3 = Charge(-1,
                    axes.coords_to_point(-1, 1),
                    add_glow=True)
        
        c4 = Charge(-1,
                    axes.coords_to_point(1, -1),
                    add_glow=True)
        
        field = ElectricField(c1, c2, c3, c4)
        self.add(axes)
        self.add(c1, c2, c3, c4)
        self.add(field)

if __name__ == "__main__":
    scene = Ejercicio3c()
    scene.render(preview=True)
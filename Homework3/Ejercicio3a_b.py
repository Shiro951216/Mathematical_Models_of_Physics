from manim import *
from manim_physics import *

class Ejercicio3a(Scene):
    def construct(self):
        axes = NumberPlane(x_range = [-3, 3, 1],
                           x_length = 14.222222222222222,
                           y_range = [-2.5, 2.5, 1],
                           y_length = 8,
                           x_axis_config = {"font_size":20},
                           y_axis_config = {"font_size":20},
                           tips=True).add_coordinates()
        def ingresar_cargas():
            cargas = []
            n_cargas = int(input('Ingrese el número de cargas: '))
            for i in range(n_cargas):
                print(f'Ingrese la magnitud (C) y las coordenadas (m) de la carga {i+1}:')
                qi = float(input(f'q{i+1} = '))
                xi = float(input(f'x{i+1} = '))
                yi = float(input(f'y{i+1} = '))
                print('-----------------------------------------------------------------')
                cargas.append({'qi': qi, 'xi': xi, 'yi': yi})
            return cargas

        cargas = ingresar_cargas()
        lista_carga = []

        for carga in cargas:
            qi = carga["qi"]
            xi = carga["xi"]
            yi = carga["yi"]
            lista_carga.append(Charge(qi,
                        axes.coords_to_point(xi, yi),
                        add_glow=True))
        
        field = ElectricField(*lista_carga)
        self.add(axes)
        self.add(*lista_carga)
        self.add(field)

if __name__ == "__main__":
    scene = Ejercicio3a()
    scene.render(preview=True)
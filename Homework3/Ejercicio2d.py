import math

def ingresar_cargas():
    cargas = []
    n_cargas = int(input('Ingrese el número de cargas: '))
    for i in range(n_cargas):
        print(f'Ingrese la magnitud (C) y las coordenadas (m) de la carga {i+1}:')
        qi = float(input(f'q{i+1} = '))
        xi = float(input(f'x{i+1} = '))
        yi = float(input(f'y{i+1} = '))
        zi = float(input(f'z{i+1} = '))
        print('-----------------------------------------------------------------')
        cargas.append({'qi': qi, 'xi': xi, 'yi': yi, 'zi': zi})
    return cargas

def hallar_campo_electrico(cargas):
    epsilon_0 = 8.85e-12
    print('Ingrese las coordenadas donde desea hallar el campo eléctrico:')
    x = float(input('x = '))
    y = float(input('y = '))
    z = float(input('z = '))
    print('-----------------------------------------------------------------')
    Ex = 0.0
    Ey = 0.0
    Ez = 0.0
    for carga in cargas:
        qi = carga["qi"]
        xi = carga["xi"]
        yi = carga["yi"]
        zi = carga["zi"]
        r = math.sqrt((x - xi)**2 + (y - yi)**2 + (z - zi)**2)

        if r == 0:
            continue
        
        Eix = (qi / (4 * math.pi * epsilon_0)) * (x - xi) / (r**3)
        Eiy = (qi / (4 * math.pi * epsilon_0)) * (y - yi) / (r**3)
        Eiz = (qi / (4 * math.pi * epsilon_0)) * (z - zi) / (r**3)        
        Ex += Eix
        Ey += Eiy
        Ez += Eiz

    E_magnitud = math.sqrt(Ex**2 + Ey**2 + Ez**2)
    angulo_direc_x = math.degrees(math.acos(Ex/E_magnitud)) if E_magnitud !=0 else 0
    angulo_direc_y = math.degrees(math.acos(Ey/E_magnitud)) if E_magnitud !=0 else 0
    angulo_direc_z = math.degrees(math.acos(Ez/E_magnitud)) if E_magnitud !=0 else 0
    print(f"Magnitud del campo eléctrico: |E| = {E_magnitud:.2e} N/C")
    print(f"Ángulo con el eje x (en grados): ángulo = {angulo_direc_x:.2f}º")
    print(f"Ángulo con el eje y (en grados): ángulo = {angulo_direc_y:.2f}º")
    print(f"Ángulo con el eje z (en grados): ángulo = {angulo_direc_z:.2f}º")

if __name__ == "__main__":
    print('\n***************** Calculadora de Campo Eléctrico en (x,y,z) *****************\n')
    try:
        cargas = ingresar_cargas()
        hallar_campo_electrico(cargas)
    except ValueError:
        print('Ingrese un numero valido.')
    print('\n ************************** Gracias por su visita **************************\n')
    input('Presione Enter para salir')
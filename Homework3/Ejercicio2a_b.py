import math

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

def hallar_campo_electrico(cargas):
    epsilon_0 = 8.85e-12
    print('Ingrese las coordenadas donde desea hallar el campo eléctrico:')
    x = float(input('x = '))
    y = float(input('y = '))
    print('-----------------------------------------------------------------')
    Ex = 0.0
    Ey = 0.0
    for carga in cargas:
        qi = carga["qi"]
        xi = carga["xi"]
        yi = carga["yi"]
        r = math.sqrt((x - xi)**2 + (y - yi)**2)
        if r == 0:
            continue
        Eix = (qi / (4 * math.pi * epsilon_0)) * (x - xi) / (r**3)
        Eiy = (qi / (4 * math.pi * epsilon_0)) * (y - yi) / (r**3)
        Ex += Eix
        Ey += Eiy

    E_magnitud = math.sqrt(Ex**2 + Ey**2)
    angulo_rad = math.atan2(Ey, Ex)
    angulo_grados = math.degrees(angulo_rad)
    print(f"Magnitud del campo eléctrico: |E| = {E_magnitud:.2e} N/C")
    print(f"Ángulo con el eje x (en grados): ángulo = {angulo_grados:.2f}º")

if __name__ == "__main__":
    print('\n***************** Calculadora de Campo Eléctrico en el plano *****************\n')
    try:
        cargas = ingresar_cargas()
        hallar_campo_electrico(cargas)
    except ValueError:
        print('Ingrese un numero valido.')
    print('\n *************************** Gracias por su visita ***************************\n')
    input('Presione Enter para salir')
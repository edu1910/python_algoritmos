def area_quadrado(lado):
    return lado*lado

def area_retangulo(base, altura):
    return base*altura

def area_circ(raio):
    return 3.1415 * raio * raio

def area_triangulo(base, altura):
    return (base * altura) / 2

def area_hexagono_regular(base, altura):
    return 6*area_triangulo(base, altura)
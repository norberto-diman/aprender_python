# Exercício 3 de POO: Crie uma classe filha `Bus` que herdará todas as variáveis e métodos da classe `Vehicle`.

class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class Bus(Vehicle):
    pass

school_bus = Bus('School Volvo', 180, 12)

print(f'Nome do veículo: {school_bus.name}')
print(f'Velocidade: {school_bus.max_speed}')
print(f'Quilometragem: {school_bus.mileage}')
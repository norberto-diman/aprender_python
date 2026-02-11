# Exercício 1 de POO: Crie uma classe com atributos de instância
# Escreva um programa em Python para criar uma classe `Vehicle` com max_speed atributos mileage de instância.

class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

model_x = Vehicle(240, 20)

print(f'Velocidade: {model_x.max_speed} | Quilometragem: {model_x.mileage}')
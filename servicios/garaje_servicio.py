# servicios/garaje_servicio.py

class GarajeServicio:
    def __init__(self):
        self.vehiculos = []

    def agregar_vehiculo(self, vehiculo):
        self.vehiculos.append(vehiculo)

    def obtener_vehiculos(self):
        return self.vehiculos
# classe para capacitores
from numpy import pi

class Capacitor:
    def __init__(self, capacitancia, frequencia):
        self.capacitancia = capacitancia
        self.frequencia = frequencia

    def reatancia(self):
        return 1/(2*pi*self.frequencia*self.capacitancia*1j)
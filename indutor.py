# classe para tratar dos indutores

from numpy import pi

class Indutor:
    def __init__(self,indutancia,frequencia):
        self.indutancia = indutancia
        self.frequencia = frequencia
    
    def reatancia(self):
        return 2*pi*self.frequencia*self.indutancia*1j
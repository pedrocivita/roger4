# arquivo de metodos auxiliares 
# calculo de reatancia em serie e paralelo

import cmath
import numpy as np
from numpy import pi
from numpy import sqrt
from numpy import linalg

def serie(*args):
    return np.sum(args)

def paralelo(*args):
    return 1/np.sum(1/arg for arg in args)

def retangular(zeq):
    return cmath.rect(abs(zeq),cmath.phase(zeq)*180/pi)

def polarGrau(zeq):
    return abs(zeq),cmath.phase(zeq)*180/pi

def eficaz(a):
    return a/sqrt(2)

def CalcularTransformador(v1, rc, r1, r2, xl1, xl2, xm):
    Z=np.array([[r1+xl1, -xm],[-xm, xl2+r2+rc]])
    V=np.array([v1,0])
    I=np.dot(linalg.inv(Z),V)
    return I[0], I[1]

def real(zeq):
    return abs(zeq)*np.cos(cmath.phase(zeq))

def imaginario(zeq):
    return abs(zeq)*np.sin(cmath.phase(zeq))

def fatorPotencia(zeq):
    return np.cos(cmath.phase(zeq))

def freqResonancia(l, c):
    return 1/(2*pi*sqrt(l*c))

def CalcularTransformadorProjeto(v1, rc, r, l, m, c, f):
    w = 2*pi*f

    xl = w*l*1j
    xc = 1/(w*c*1j)
    xm = m*w*1j
    
    Z=np.array([[r+xl+xc, -xm],[-xm, xl+r+1/(1/rc+1/xc)]])
    V=np.array([v1,0])
    I=np.dot(linalg.inv(Z),V)

    Zeq = 1/(1/rc+1/xc)
    V2 = I[1]*Zeq

    return abs(I[0]), abs(I[1]), V2

def capacitorPelaFreqReq(freq, indutancia):
    return 1/(4*pi**2*freq**2*indutancia)

l  = 0.1
c = 1e-9

freqRes = freqResonancia(l, c)
print("Frequencia de ressonancia: ", freqRes)

v1 = 10

rc = 500
r = 1

k = 0.5
m = k*l

frequencies = np.arange(1000, 50000, 100)

values = {"i1": [], "i2": [], "v2": []}

for f in frequencies:
    i1, i2, v2 = CalcularTransformadorProjeto(v1, rc, r, l, m, c, f)
    values["i1"].append(i1)
    values["i2"].append(i2)
    values["v2"].append(v2)

    print(values["i1"])
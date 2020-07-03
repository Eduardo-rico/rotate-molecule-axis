from sys import *
import numpy as np
from tinyQuaternion import Quaternion
# https://pypi.org/project/tinyquaternion/


def abrir_archivo(file):
    data = open(file, "r").readlines()
    return data


def to_arreglo(contenido):
    llamado = []
    each_linea = []
    algo = [linea.split("\t") for linea in contenido]
    for l in algo:
        ultima = float(l[-1])
        llamado.append(l[0])
        l = l[1:-1]
        l.append(ultima)
        each_linea.append(l)

    otro = []
    for liena in each_linea:
        otro.append([float(punto) for punto in liena])

    return otro, llamado


def a_np(matriz):
    nuevo_array_np = [np.array(vector)for vector in matriz]
    return nuevo_array_np


def rotar_prro(np_matriz, gradosX=0, gradosY=0, gradosZ=0):
    np_matriz_rotada = []
    radianesX, radianesY, radianesZ = gradosX*np.pi / \
        180, gradosY*np.pi/180, gradosZ*np.pi/180
    if gradosX > 0 and gradosY == 0 and gradosZ == 0:
        q = Quaternion(a=radianesX, n=np.array([1., 0., 0.]))
        for vector in np_matriz:
            nuevo_vector = q.rotatePoint(vector)
            np_matriz_rotada.append(nuevo_vector)
        return np_matriz_rotada

    elif gradosX == 0 and gradosY > 0 and gradosZ == 0:
        q = Quaternion(a=radianesY, n=np.array([0., 1., 0.]))
        for vector in np_matriz:
            nuevo_vector = q.rotatePoint(vector)
            np_matriz_rotada.append(nuevo_vector)
        return np_matriz_rotada
    elif gradosX == 0 and gradosY == 0 and gradosZ > 0:
        q = Quaternion(a=radianesZ, n=np.array([0., 0., 1.]))
        for vector in np_matriz:
            nuevo_vector = q.rotatePoint(vector)
            np_matriz_rotada.append(nuevo_vector)
        return np_matriz_rotada
    else:
        return "error"


def rehacer_XYZ(matriz, nombres):
    vector = []
    final = []
    lista = [list(vector) for vector in matriz]
    for vector in lista:
        vector_str = []
        for punto in vector:
            vector_str.append(str(np.float(punto)))
        final.append(vector)

    mtrx = []
    for index, i in enumerate(nombres):
        xyz = []
        xyz.append(i)
        for j in range(3):
            xyz.append(str(final[index][j]))
        mtrx.append(xyz)

    f = open("out.xyz", "a")
    for linea_string in mtrx:
        f = open("out.xyz", "a")
        f.write("\t".join(linea_string))
        f.write("\n")
        f.close()

def run():
    data = abrir_archivo(argv[1])
    equis = float(argv[2])
    ye = float(argv[3])
    zeta = float(argv[4])
    arreglo, nombre = to_arreglo(data)
    matriz_rotada = rotar_prro(
        arreglo, gradosX=equis, gradosY=ye, gradosZ=zeta)
    rehacer_XYZ(matriz_rotada, nombre)


run()

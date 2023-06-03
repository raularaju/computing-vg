from ts2vg import NaturalVG
import numpy as np
from scipy.sparse import coo_matrix
def cria_grafos_visibilidade(tracings):
    grafos_visibilidade = list() #TODO mudar para bitArray
    
    for leads in tracings.T: #pega a series transposta
        grafo = NaturalVG().build(leads).adjacency_matrix()
        grafo_esparso = coo_matrix(grafo)     
        grafos_visibilidade.append(grafo_esparso)
    return np.array(grafos_visibilidade)


def cria_matriz_features(features: np.array):
    matriz_features = np.zeros((8, 4096))
    for i in range(8):
        matriz_features[i] = features.T[i]

    return matriz_features
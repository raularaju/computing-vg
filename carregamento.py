import numpy as np
import h5py

def carrega_series(caminho_arquivo: str, inicio: int, fim: int):
    print("Inciando análise de dados")

    with h5py.File(caminho_arquivo,'r') as arquivo:
        print(f"Carregando as séries de {inicio} até {fim}")

        traces_ids = np.array(arquivo['exam_id'][inicio:fim])
        tracings = np.array(arquivo['tracings'][inicio:fim])
        print("Séries carregada com tamanho {}".format(fim-inicio))   
    tracings = np.delete(tracings,[2,3,4,5],axis = 2 ) # Remove dos LEADS as combinações Lineares DIII; AVR; AVL e AVF
    return traces_ids, tracings

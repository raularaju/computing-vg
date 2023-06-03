import argparse
import numpy as np
import h5py
from carregamento import carrega_series
from processamento import cria_grafos_visibilidade, cria_matriz_features
from armazenamento import armazena_grafos_visibilidade_e_features
from scipy.sparse import csr_matrix


parser = argparse.ArgumentParser(description="Utiliza uma base de dados de ECG para gerar grafos de visibilidade sobre os 12 LEADS")
parser.add_argument('--input', dest="input", required=True, type=str, help="caminho do arquivo de entrada que contém os dados a ser lidos")
parser.add_argument('--output', dest="output", required=True, type=str, help="caminho relativo seguido do nome do arquivo de armazenamento dos dados processados")
parser.add_argument('--init', dest="init", required=False, type=int, help="Valor de início do carregamento das séries.")
parser.add_argument('--end', dest="end", required=False, type=int, help="Valor de final do carregamento das séries.")



ARGUMENTOS = parser.parse_args()

if (ARGUMENTOS.init is None):
    index_incio = 0
else:
    index_incio = ARGUMENTOS.init

if (ARGUMENTOS.end is None):
    index_fim = 100
else:
    index_fim = ARGUMENTOS.end

id_exames, tracings = carrega_series(ARGUMENTOS.input, index_incio, index_fim)
lista_matriz_features = list()
lista_grafos_visibilidade = list()
num_exames = len(id_exames)



i = 1
nome_arq_saida = ARGUMENTOS.output
arq_saida_h5 = h5py.File(nome_arq_saida, 'w')
for id_exame, trace in zip(id_exames, tracings):
    print(trace.shape)
    print(f"Processando o exam id_exame: {id_exame}, exame nro {i}")
    grafos_comprimidos = cria_grafos_visibilidade(trace)
    matriz_features = cria_matriz_features(trace)
    armazena_grafos_visibilidade_e_features(arq_saida_h5, id_exame, matriz_features, grafos_comprimidos)
    i+=1
arq_saida_h5.close()
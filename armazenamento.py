import h5py

def armazena_grafos_visibilidade_e_features(arquivo_saida, id_exame, matriz_features,  grafos_visibilidade):
    print("Iniciando armazenamento de dados")
    grupo_exame = arquivo_saida.create_group('exame {}'.format(id_exame))
    for j in range(8):
        grupo_lead = grupo_exame.create_group('lead {}'.format(j))
        grupo_grafo = grupo_lead.create_group('grafo')
        grupo_grafo.create_dataset('data', data=grafos_visibilidade[j].data)
        grupo_grafo.create_dataset('row', data=grafos_visibilidade[j].row)
        grupo_grafo.create_dataset('col', data=grafos_visibilidade[j].col)
        grupo_lead.create_dataset('features', data=matriz_features[j])
    print("Dados armazenados com sucesso")
import json
import pandas as pd

with open('documentos_atualizados.json', 'r') as f:
    dados = json.load(f)

cnpj_para_limpar = pd.read_csv("base.csv", sep=";")
telefones = cnpj_para_limpar['telefone']

df_documentos_falso = pd.DataFrame(dados)
documentos_falso = df_documentos_falso[df_documentos_falso['sucesso'] == False]

cnpj_para_limpar['documento'] = cnpj_para_limpar['documento'].astype(str)
documentos_falso['documento'] = documentos_falso['documento'].astype(str)

df_merge = pd.merge(cnpj_para_limpar, documentos_falso, how='outer', on='documento', indicator = True )
df_merge = df_merge[df_merge['_merge'] == 'both']
df_merge.to_csv('documento_sem_sucesso_com_telefone.csv', sep =';')

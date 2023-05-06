import pandas as pd

documento = []  
sucesso = []

cnpj_para_limpar = pd.read_csv("base.csv", sep=";")
cnpjs = cnpj_para_limpar['documento']
telefones = cnpj_para_limpar['telefone']

documento_falso = []
indice = []
telefone = []

for i in range(len(sucesso)):
    if sucesso[i] == False:
        documento_falso.append(documento[i])
        indice.append(i+1)

for d in range(len(documento_falso)):
    for i in range(len(cnpjs)):
        if str(documento_falso[d]) == str(cnpjs[i]):
            print(documento_falso[d])
            telefone.append(telefones[i])
        
df = pd.DataFrame({
    'documento' : documento_falso,
    'telefone' : telefone,
    'indice' : indice
    
})

df.to_csv("documento_falso.csv", index=False)

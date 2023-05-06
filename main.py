import pandas as pd

documento = ["18815454000186", "5159730000153", "6201075000117", "5797375000229", "5809733000195", "34716900000151", "41861223000120", "41867835000120", "48861168000118", "3614334000143", "9564094000104", "11398190000163", "11464885000104", "54345772000194", "8341490000100", "8828114000136", "5528654000106", "29754935000145", "29856793000127", "26713877000113", "9550878000175", "1052773000184", "1360402000160", "44887764000116", "40695430000190", "23400953000142", "8256482000157", "21225023000174", "8668371000158", "11522296000127", "28909195000106", "55680466000177", "44538991000136", "31443488000155", "35926099000131", "64564784000163", "28177968000107", "46335496000155", "46509305000124", "5392678000180", "15723761000149", "36755672000154", "14853056000101", "24545328000151", "12340686000149", "12671903000183", "35951257000103", "24838200000186", "12557545000182", "40776490000137", "13447618000146", "65037624000129", "40100483000110", "17575107000160", "33352131000197", "33364836000124", "33432326000147", "1724868000105", "7940085000137", "60015310000101", "27049913000159", "41819406000188", "56975204000100", "57028615000143", "11066089000105", "20653907000167", "59589739000123", "24734613000110"]  
sucesso = [True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, True, True, True, True, True, False, True, True, False, True, True, False, True, True, False, True, True, True, True, True, True, True, False, True, True, True, True, False, True, True, True, True, True, True, False, True, True, True, True, True, True, False, True, False, True, True, True, True, True, True, True, True, True]

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

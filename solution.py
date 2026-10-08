import requests
from datetime import datetime, timedelta

def cotar(data):
    url = f"https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia(dataCotacao=@dataCotacao)?%40dataCotacao='{data}'&%24format=json"
    res = requests.get(url)
    res = res.json() #método .json transforma o JSON em um {dicionario} para conseguir ler os dados
    if res['value']:
        return res['value'][0]['cotacaoCompra']
    else:
        diaanterior = datetime.strptime(data, "%m-%d-%Y") - timedelta(1)
        diaanterior = datetime.strftime(diaanterior, "%m-%d-%Y")
        return cotar(diaanterior)

data = '08-10-2026'
lista = []
for i in range(366):
    data = datetime.strptime(data, "%m-%d-%Y") - timedelta(1)
    data = datetime.strftime(data, "%m-%d-%Y")
    lista.append(cotar(data))
print(lista)
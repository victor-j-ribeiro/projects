import pandas as pd 
#identificando a pasta numa variável
file_path = 'lista_pedido.xlsx'
#função para ler o arquivo em xlsx
df = pd.read_excel(file_path, engine='openpyxl')

print(df)
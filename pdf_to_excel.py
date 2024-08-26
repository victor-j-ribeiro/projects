import pdfplumber
import pandas as pd

def pdf_to_excel(pdf_path, excel_path):
    # Abre o arquivo PDF
    with pdfplumber.open(pdf_path) as pdf:
        # Lista para armazenar todas as tabelas extraídas
        all_tables = []

        # Itera por todas as páginas do PDF
        for page in pdf.pages:
            # Extrai tabelas da página
            tables = page.extract_tables()
            
            # Adiciona as tabelas extraídas à lista
            for table in tables:
                df = pd.DataFrame(table[1:], columns=table[0])  
            # Cria um DataFrame do Pandas
                all_tables.append(df)

        # Concatena todos os DataFrames em um único DataFrame
        full_df = pd.concat(all_tables, ignore_index=True)
        
        # Salva o DataFrame em um arquivo Excel
        full_df.to_excel(excel_path, index=False)

# Caminhos dos arquivos
pdf_path = 'suplementos_pdf.pdf'
excel_path = 'suplementos_xlsx.xlsx'

# Converte o PDF para Excel
pdf_to_excel(pdf_path, excel_path)
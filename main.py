import os
import json
from extractor import extract_cpfs

# Diretório contendo os arquivos PDF
pdf_directory = "pdfs"
# Nome do arquivo JSON de saída
json_path = "cpfs.json"

# Lista para armazenar todos os CPFs extraídos
all_cpfs = []

# Processa cada arquivo PDF no diretório
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        pdf_path = os.path.join(pdf_directory, filename)
        cpfs = extract_cpfs(pdf_path)
        all_cpfs.extend(cpfs)
        print(f"CPFs extraídos de {filename}: {cpfs}")

# Remove duplicatas e ordena os CPFs
all_cpfs = sorted(set(all_cpfs))

# Salva os CPFs no arquivo JSON
with open(json_path, 'w') as f:
    json.dump(all_cpfs, f, indent=4)

print(f"CPFs extraídos e salvos em {json_path}")

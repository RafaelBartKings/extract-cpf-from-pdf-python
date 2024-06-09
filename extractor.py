import re
import PyPDF2

def extract_cpfs(pdf_path):
    cpfs = []
    cpf_pattern = re.compile(r'\d{3}\.\d{3}\.\d{3}-\d{2}')

    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        for page in reader.pages:
            text = page.extract_text()
            cpfs.extend(cpf_pattern.findall(text))

    return cpfs

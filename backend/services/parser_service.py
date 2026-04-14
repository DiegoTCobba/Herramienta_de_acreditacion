import re

def extraer_tins(texto):
    regex = re.compile(r'\d{12}')
    return regex.findall(texto)

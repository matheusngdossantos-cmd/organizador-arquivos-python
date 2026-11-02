import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title= 'Selecione uma pasta')

lista_arquivos = os.listdir(caminho)

locais = {
    'imagens': ['.png', '.jpg'],
    'planilhas': ['.xlsx'],
    'pdfs': ['.pdf'],
    'csv': ['.csv'],
    'word': ['.docx'],
    'pptx': ['.pptx'],
    'python': ['.py']
}

for arquivo in lista_arquivos:
    #01. arquivo.pdf (nome e extensao)
    nome, extensão = os.path.splitext(f'{caminho}/{arquivo}')
    for pasta in locais:
        if extensão in locais[pasta]:
            if not os.path.exists(f'{caminho}/{pasta}'):
                os.mkdir(f'{caminho}/{pasta}')
            os.rename(f'{caminho}/{arquivo}', f'{caminho}/{pasta}/{arquivo}')
